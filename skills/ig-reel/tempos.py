#!/usr/bin/env python3
"""
tempos.py - transforma o roteiro de um Reel num mapa de tempos antes de gravar.

Estima quanto tempo cada fala leva, empilha em minutagem e aponta as quatro
coisas que matam um Reel na edição: gancho que passa dos três segundos, uma
fala longa o bastante para a pessoa sair, uma sequência de falas sem nada
concreto, e uma duração que não bate com o que você queria.

Os tempos são estimativa por contagem de palavras a um ritmo de palavras por
minuto. Servem para planejar a edição, não substituem gravar. Ajuste com --ppm
depois de cronometrar você lendo um roteiro em voz alta: em português a maioria
das pessoas fica entre 130 e 180. O padrão aqui é 150.

Uso
  python3 tempos.py roteiro.txt
  python3 tempos.py roteiro.txt --alvo 30
  python3 tempos.py roteiro.txt --ppm 170 --alvo 45
  python3 tempos.py roteiro.txt --json
"""

import argparse
import json
import re
import sys

WORD_RE = re.compile(r"[A-Za-zÀ-ÿ0-9$%'’-]+")
SENT_RE = re.compile(r"[^.!?]+[.!?]*")
CONCRETE_RE = re.compile(
    r"R\$\s?\d|\b\d[\d.,]*|(?<!^)(?<![.!?:] )\b[A-ZÀ-Ý][a-zà-ÿ]{2,}\b"
    r"|\b(?:dois|duas|três|quatro|cinco|seis|sete|oito|nove|dez|vinte|trinta|cem|mil|metade)\b",
    re.MULTILINE | re.IGNORECASE)
STOPWORDS = {
    "o", "a", "os", "as", "um", "uma", "uns", "umas", "e", "ou", "mas", "se",
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas", "por",
    "pra", "pro", "para", "com", "que", "isso", "esse", "essa", "isto", "é",
    "são", "foi", "era", "ser", "tá", "está", "você", "vc", "seu", "sua", "eu",
    "meu", "minha", "me", "te", "a gente", "nós", "eles", "elas", "ele", "ela",
    "não", "nao", "só", "já", "tem", "ter", "vai", "vou", "faz", "ao", "à",
    "mais", "muito", "bem", "como", "quando", "também", "lhe", "sem",
}

HOOK_WINDOW = 3.0        # segundos. Depois disso, o polegar já decidiu.
MAX_BEAT = 4.0           # segundos numa ideia sem mudança na tela.
ABSTRACT_RUN = 3         # falas seguidas sem nada verificável.


def words(text):
    return WORD_RE.findall(re.sub(r"(?<=\d)[.,](?=\d)", "", text))


def tc(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m)}:{s:04.1f}"


def split_beats(raw, wps):
    """Uma linha é uma fala, a não ser que seja longa demais para ser uma."""
    beats = []
    for line in [l.strip() for l in raw.splitlines()]:
        if not line:
            continue
        if len(words(line)) / wps <= MAX_BEAT * 1.5:
            beats.append(line)
            continue
        parts = [p.strip() for p in SENT_RE.findall(line) if p.strip()]
        buf = ""
        for part in parts:
            candidate = (buf + " " + part).strip()
            if buf and len(words(candidate)) / wps > MAX_BEAT:
                beats.append(buf)
                buf = part
            else:
                buf = candidate
        if buf:
            beats.append(buf)
    return beats


def analyse(raw, wpm=150, target=None):
    wps = wpm / 60.0
    beats = split_beats(raw, wps)
    if not beats:
        return None

    rows, clock = [], 0.0
    for i, text in enumerate(beats):
        n = len(words(text))
        dur = n / wps
        rows.append({
            "n": i + 1, "inicio": round(clock, 2), "duracao": round(dur, 2),
            "palavras": n, "texto": text,
            "concreto": len(CONCRETE_RE.findall(text)),
            "rotulo": "", "alertas": [],
        })
        clock += dur
    total = clock

    for r in rows:
        if r["n"] == 1 or r["inicio"] + r["duracao"] <= HOOK_WINDOW:
            r["rotulo"] = "GANCHO"
    rows[-1]["rotulo"] = "CTA" if rows[-1]["rotulo"] != "GANCHO" else "GANCHO/CTA"
    half = total / 2
    for r in rows:
        if not r["rotulo"] and r["inicio"] <= half < r["inicio"] + r["duracao"]:
            r["rotulo"] = "MEIO"

    notes = []
    if rows[0]["duracao"] > HOOK_WINDOW:
        rows[0]["alertas"].append(f"gancho leva {rows[0]['duracao']:.1f}s, passa dos {HOOK_WINDOW:.0f}s")
        notes.append(f"A fala 1 leva {rows[0]['duracao']:.1f}s. Corte para {int(HOOK_WINDOW * wps)} "
                     "palavras ou menos, senão o gancho chega depois que a pessoa já decidiu.")
    if rows[0]["concreto"] == 0:
        notes.append("A fala 1 não tem número nem nome. Gancho sem nada verificável é o que "
                     "mais é pulado.")

    for r in rows:
        if r["duracao"] > MAX_BEAT:
            r["alertas"].append(f"{r['duracao']:.1f}s numa fala só")
    long_beats = [r["n"] for r in rows if r["duracao"] > MAX_BEAT]
    if long_beats:
        notes.append(f"Fala(s) {', '.join(map(str, long_beats))} passam de {MAX_BEAT:.0f}s. "
                     "Divida a frase ou mude o que está na tela no meio dela. "
                     "Quadro parado é onde a pessoa sai.")

    run, start = 0, None
    for r in rows:
        if r["concreto"] == 0:
            run += 1
            start = start if start is not None else r["n"]
            if run == ABSTRACT_RUN:
                notes.append(f"As falas {start}-{r['n']} não têm nada concreto. "
                             "Coloque um número, uma quantidade, um alimento específico ou uma fonte.")
        else:
            run, start = 0, None

    first = {w.lower() for w in words(rows[0]["texto"]) if w.lower() not in STOPWORDS}
    last = {w.lower() for w in words(rows[-1]["texto"]) if w.lower() not in STOPWORDS}
    loop = sorted(first & last)
    if loop:
        notes.append(f"Loop: a última fala repete \"{', '.join(loop[:3])}\" do gancho. "
                     "Segunda visualização é alcance de graça.")
    else:
        notes.append("Sem loop. A última fala não repete nenhuma palavra do gancho, e o vídeo "
                     "termina chapado. Ecoar uma palavra da fala 1 é o replay mais barato que existe.")

    if target:
        delta = total - target
        if abs(delta) <= target * 0.1:
            notes.append(f"Duração no alvo ({total:.1f}s para {target:.0f}s).")
        elif delta > 0:
            notes.append(f"{delta:.1f}s acima do alvo. Corte umas {int(delta * wps)} palavras.")
        else:
            notes.append(f"{-delta:.1f}s abaixo do alvo. Acrescente {int(-delta * wps)} palavras "
                         "ou grave mais curto. Mais curto costuma ser o certo.")

    return {
        "ppm": wpm, "alvo": target,
        "total_segundos": round(total, 2),
        "total_palavras": sum(r["palavras"] for r in rows),
        "falas": rows, "notas": notes,
    }


def render(a, out=sys.stdout):
    head = (f"MAPA DE TEMPOS  ·  {a['total_palavras']} palavras  ·  ~{a['total_segundos']:.1f}s "
            f"a {a['ppm']:.0f} ppm" + (f"  ·  alvo {a['alvo']:.0f}s" if a["alvo"] else ""))
    print("\n" + head, file=out)
    print("=" * max(len(head), 72), file=out)
    for r in a["falas"]:
        label = f"{r['rotulo']:<11}" if r["rotulo"] else " " * 11
        print(f"  {tc(r['inicio'])}  {r['duracao']:4.1f}s  {label}{r['texto']}", file=out)
        for f in r["alertas"]:
            print(f"  {'':>6}  {'':>5}  {'':<11}^ {f}", file=out)
    print("-" * max(len(head), 72), file=out)
    for n in a["notas"]:
        print(f"  - {n}", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Cronometra um roteiro de Reel.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo do roteiro, ou -")
    ap.add_argument("--ppm", "--wpm", dest="ppm", type=float, default=150,
                    help="palavras por minuto (padrão 150)")
    ap.add_argument("--alvo", "--target", dest="alvo", type=float, help="duração alvo em segundos")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = analyse(raw, wpm=args.ppm, target=args.alvo)
    if not a:
        print("roteiro vazio", file=sys.stderr)
        sys.exit(2)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)


if __name__ == "__main__":
    main()
