#!/usr/bin/env python3
"""
legenda.py - revisa uma legenda de Instagram e mostra exatamente o que o feed
mostra antes do "... mais".

O Instagram mostra uns 125 caracteres da legenda no feed e esconde o resto
atrás de um toque. Quase toda legenda que falha, falha ali: o gancho está na
terceira frase, a primeira linha é um "Oi, gente!", ou tudo começa com hashtag.
Este script desenha essa janela como uma caixa, para você ler como um estranho
rolando o feed, e depois faz as checagens que valem a pena.

O corte de 125 é aproximado: muda com o aparelho, o tamanho da fonte e as
quebras de linha. Por isso o certo é ter folga, não uma legenda que termina
exatamente no 125. Mude com --corte para testar mais apertado.

Para a checagem do Código de Ética do nutricionista, rode também
ig-etica/etica.py na mesma legenda.

Uso
  python3 legenda.py legenda.txt
  python3 legenda.py legenda.txt --busca "nutricionista em Itaúna,emagrecimento"
  python3 legenda.py legenda.txt --json
"""

import argparse
import json
import re
import sys
import textwrap

LIMIT = 2200             # limite do Instagram.
TRUNCATE = 125           # onde o feed corta, aproximadamente.
HASHTAG_LIMIT = 5        # limite por post/Reel desde 18/12/2025 (antes eram 30).

HASHTAG_RE = re.compile(r"(?:^|\s)(#[\wÀ-ÿ]+)")
MENTION_RE = re.compile(r"(?:^|\s)(@[A-Za-z0-9_.]+)")
LINK_RE = re.compile(r"https?://\S+|\bwww\.\S+|\b[a-z0-9-]+\.(?:com|com\.br|br|io|net|org|app|me)/\S*",
                     re.IGNORECASE)
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿←-⇿️]")
CONCRETE_RE = re.compile(
    r"R\$\s?\d|\b\d[\d.,]*|(?<!^)(?<![.!?:] )\b[A-ZÀ-Ý][a-zà-ÿ]{2,}\b"
    r"|\b(?:dois|duas|três|quatro|cinco|seis|sete|oito|nove|dez|vinte|trinta|cem|mil|metade)\b",
    re.MULTILINE)

ASKS = [
    (re.compile(r"(?i)\bcomente?a?\s+(?:a palavra\s+|aqui\s+)?[\"“']?[A-ZÀ-Ý0-9]{3,}\b"), "comentar palavra-chave"),
    (re.compile(r"(?i)\b(?:me (?:chama|manda|envia)|manda|chama)\b[^.!?\n]{0,15}\b(?:dm|direct|mensagem|whats(?:app)?)\b"), "chamar na DM/WhatsApp"),
    (re.compile(r"(?i)\bsalv[ae]\b[^.!?\n]{0,15}\b(?:post|v[ií]deo|isso|esse|essa|pra depois|para depois)\b"), "salvar"),
    (re.compile(r"(?i)\b(?:compartilh[ae]|envi[ae]|manda (?:pra|para))\b[^.!?\n]{0,25}\b(?:algu[eé]m|amig[oa]|quem|m[aã]e|pai)\b"), "compartilhar"),
    (re.compile(r"(?i)\bme segu[ea]\b|\bsiga\b|\bsegue (?:o|a) @|\bsegue pra mais\b"), "seguir"),
    (re.compile(r"(?i)\blink (?:na|da) bio\b"), "link na bio"),
    (re.compile(r"(?i)\b(?:arrasta|deslize|desliza)\b"), "arrastar"),
    (re.compile(r"(?i)\bme (?:conta|conte|diz|diga)\b|\bqual (?:voc[eê]|vc)\b|\bvoc[eê] (?:j[aá] )?(?:faz|fez|come|toma)\b[^?\n]*\?"), "responder pergunta"),
    (re.compile(r"(?i)\b(?:agende|agenda|marque|marca|reserve)\b[^.!?\n]{0,20}\b(?:consulta|hor[aá]rio|avalia[cç][aã]o)\b"), "agendar consulta"),
]

FILLER_TAGS = {"#viral", "#fyp", "#explore", "#explorar", "#foryou", "#paravoce", "#paravocê",
               "#trending", "#instagood", "#love", "#amor", "#follow", "#sigo", "#sdv",
               "#seguidores", "#like", "#curtir", "#reels", "#reelsinstagram", "#viralreels",
               "#instadaily", "#tbt", "#fitness", "#saude", "#saúde", "#dieta", "#foco", "#vida"}


def visible_window(text, cut):
    flat = text.strip()
    return flat if len(flat) <= cut else flat[:cut]


def render_box(window, truncated, out=sys.stdout, width=52):
    print("\n  O QUE O FEED MOSTRA", file=out)
    print("  +" + "-" * (width + 2) + "+", file=out)
    lines = []
    for raw in window.split("\n"):
        lines.extend(textwrap.wrap(raw, width) or [""])
    for line in lines[:8]:
        print(f"  | {line:<{width}} |", file=out)
    tail = "... mais" if truncated else "(a legenda inteira cabe)"
    print("  +" + "-" * (width + 2 - len(tail) - 2) + f" {tail} " + "+", file=out)


def analyse(text, cut=TRUNCATE, keywords=None):
    stripped = text.strip()
    chars = len(stripped)
    lines = stripped.split("\n")
    first_line = lines[0].strip() if lines else ""
    tags = HASHTAG_RE.findall(stripped)
    mentions = MENTION_RE.findall(stripped)
    links = LINK_RE.findall(stripped)
    emoji = EMOJI_RE.findall(stripped)
    window = visible_window(stripped, cut)
    truncated = chars > cut
    asks = [name for pattern, name in ASKS if pattern.search(stripped)]
    filler = [t for t in tags if t.lower() in FILLER_TAGS]
    keywords = [k.strip() for k in (keywords or []) if k.strip()]

    checks = []

    def add(name, status, detail):
        checks.append({"checagem": name, "status": status, "detalhe": detail})

    add("TAMANHO", "FALHA" if chars > LIMIT else "OK",
        f"{chars} / {LIMIT} caracteres" + (f", {chars - LIMIT} acima do limite" if chars > LIMIT else ""))

    if not first_line:
        add("PRIMEIRA LINHA", "FALHA", "a legenda começa com linha em branco")
    elif first_line.startswith(("#", "@")):
        add("PRIMEIRA LINHA", "FALHA", "começa com hashtag ou menção, na única posição que vale uma frase")
    elif re.match(r"(?i)^\s*(?:oi|ol[aá]|oie|bom dia|boa tarde|boa noite|gente|pessoal|galera)\b", first_line):
        add("PRIMEIRA LINHA", "FALHA", "começa com saudação. Ninguém para o feed para ser cumprimentado")
    elif len(first_line) > cut:
        add("PRIMEIRA LINHA", "ATENÇÃO",
            f"{len(first_line)} caracteres, então é cortada em {cut} no meio do raciocínio. "
            "Tudo bem se o corte for um suspense, ruim se for no meio de uma oração")
    else:
        add("PRIMEIRA LINHA", "OK", f"{len(first_line)} caracteres, aparece inteira")

    n_conc = len(CONCRETE_RE.findall(window))
    add("GANCHO CONCRETO", "OK" if n_conc else "ATENÇÃO",
        f"{n_conc} número(s) ou nome(s) na parte visível"
        + ("" if n_conc else " - nada verificável antes do toque"))

    if len(tags) > HASHTAG_LIMIT:
        add("HASHTAGS", "FALHA", f"{len(tags)} hashtags, acima do limite de {HASHTAG_LIMIT} do Instagram. "
                                 "As que passam da quinta não contam e o bloco parece velho")
    elif filler:
        add("HASHTAGS", "ATENÇÃO", f"{len(tags)} hashtags, {len(filler)} genéricas "
                                   f"({', '.join(filler[:3])}). Essas não descrevem nada")
    else:
        add("HASHTAGS", "OK", f"{len(tags)} hashtag(s)" + (f": {' '.join(tags)}" if tags else ""))

    if not tags:
        add("POSIÇÃO DAS TAGS", "OK", "sem hashtags para posicionar")
    elif any(re.search(r"(?:^|\s)" + re.escape(t) + r"\b", window) for t in tags):
        add("POSIÇÃO DAS TAGS", "ATENÇÃO", "tem hashtag na parte visível, gastando espaço do feed com rótulo")
    else:
        add("POSIÇÃO DAS TAGS", "OK", "hashtags abaixo do corte")

    add("LINKS", "ATENÇÃO" if links else "OK",
        f"{len(links)} link(s) na legenda, e legenda não é clicável. Coloque na bio ou mande na DM"
        if links else "nenhum link morto no texto")

    if len(asks) == 1:
        add("UM PEDIDO", "OK", f"uma chamada para ação: {asks[0]}")
    elif not asks:
        add("UM PEDIDO", "ATENÇÃO", "nenhuma chamada para ação. Decida para que serve este post")
    else:
        add("UM PEDIDO", "ATENÇÃO", f"{len(asks)} pedidos ({', '.join(asks)}). Dois pedidos é o mesmo que nenhum")

    density = len(emoji) * 100 / max(chars, 1)
    add("EMOJI", "ATENÇÃO" if density > 4 else "OK",
        f"{len(emoji)} emoji, {density:.1f} a cada 100 caracteres"
        + (" - parece enfeite" if density > 4 else ""))

    if keywords:
        low = stripped.lower()
        found = [k for k in keywords if k.lower() in low]
        missing = [k for k in keywords if k.lower() not in low]
        in_window = [k for k in found if k.lower() in window.lower()]
        status = "OK" if not missing else ("ATENÇÃO" if found else "FALHA")
        add("TERMOS DE BUSCA", status,
            f"{len(found)}/{len(keywords)} presentes"
            + (f", {len(in_window)} na parte visível" if found else "")
            + (f". Faltando: {', '.join(missing)}" if missing else ""))

    fails = sum(1 for c in checks if c["status"] == "FALHA")
    warns = sum(1 for c in checks if c["status"] == "ATENÇÃO")
    verdict = "CORRIGIR" if fails else ("REVISAR" if warns else "PRONTA")

    return {
        "caracteres": chars, "limite": LIMIT, "corte": cut,
        "visivel": window, "cortada": truncated,
        "hashtags": tags, "mencoes": mentions, "links": links,
        "emoji": len(emoji), "pedidos": asks,
        "checagens": checks, "veredito": verdict,
    }


def render(a, out=sys.stdout):
    head = (f"REVISÃO DE LEGENDA  ·  {a['caracteres']} / {a['limite']} caracteres  ·  "
            f"{len(a['hashtags'])} hashtags  ·  {len(a['pedidos'])} pedido(s)")
    print("\n" + head, file=out)
    print("=" * max(len(head), 62), file=out)
    render_box(a["visivel"], a["cortada"], out=out)
    print("", file=out)
    for c in a["checagens"]:
        print(f"  {c['status']:<7} {c['checagem']:<17} {c['detalhe']}", file=out)
    print("-" * max(len(head), 62), file=out)
    print(f"  VEREDITO  {a['veredito']}\n", file=out)


def main():
    ap = argparse.ArgumentParser(description="Revisa uma legenda de Instagram.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo da legenda, ou -")
    ap.add_argument("--corte", "--truncate", dest="corte", type=int, default=TRUNCATE,
                    help=f"caracteres mostrados antes do '... mais' (padrão {TRUNCATE})")
    ap.add_argument("--busca", "--keywords", dest="busca", default="",
                    help="termos pelos quais você quer ser encontrado, separados por vírgula")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = analyse(raw, cut=args.corte, keywords=args.busca.split(","))
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    sys.exit(0 if a["veredito"] == "PRONTA" else 1)


if __name__ == "__main__":
    main()
