#!/usr/bin/env python3
"""
referencias.py - ranqueia os Reels que você coletou pelo quanto cada um superou
a própria conta, dá nome à fórmula de gancho que cada um usou e grava o
arquivo de referências.

A ideia central: view bruta não é evidência. Uma conta de 2 milhões fazendo
400 mil views teve um dia fraco. Uma conta de 4 mil fazendo 400 mil achou
alguma coisa. Este script ranqueia pelo múltiplo sobre a mediana da própria
conta, que é a única versão de "viralizou" que ensina algo copiável.

Entrada: um arquivo separado por TAB, preenchido enquanto você navega, um Reel
por linha, com cabeçalho:

    conta     seguidores   mediana   views    gancho
    @alguem   48000        11000     412000   ninguém te conta que...

`mediana` é a média típica recente de views da conta (olhe os últimos 12 Reels
e pegue o do meio). Se você só tiver `seguidores`, deixe a mediana em branco e
o script avisa. Também aceita cabeçalho em inglês (account, followers, median,
views, hook).

Uso
  python3 referencias.py coletados.tsv
  python3 referencias.py coletados.tsv --saida ~/.claude/instagram/referencias.md
  python3 referencias.py coletados.tsv --json
"""

import argparse
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.join(HERE, "..", "ig-reel", "ganchos.json")
WORD_RE = re.compile(r"[A-Za-zÀ-ÿ0-9$%'’-]+")
ALIASES = {"account": "conta", "followers": "seguidores", "median": "mediana", "hook": "gancho",
           "visualizacoes": "views", "visualizações": "views"}

try:
    sys.path.insert(0, os.path.join(HERE, "..", "ig-reel"))
    from nota_gancho import run as score_hook       # noqa: E402
except Exception:
    score_hook = None


def load_formulas(path):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        return None
    by_id = {h["id"]: h for h in d["hooks"]}
    order = d.get("classify_order") or sorted(by_id)
    return [(by_id[i]["id"], by_id[i]["name"], re.compile(by_id[i]["match"], re.IGNORECASE))
            for i in order if i in by_id]


def classify(hook, formulas):
    if not formulas:
        return None, "sem classificação"
    for fid, name, pattern in formulas:
        if pattern.search(hook):
            return fid, name
    return None, "sem classificação"


def read_rows(path):
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    lines = [l for l in raw.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    if not lines:
        return []
    head = [ALIASES.get(c.strip().lower(), c.strip().lower()) for c in lines[0].split("\t")]
    if "views" in head and "gancho" in head:
        cols, body = head, lines[1:]
    else:
        cols, body = ["conta", "seguidores", "views", "gancho"], lines
    rows = []
    for line in body:
        cells = line.split("\t")
        if len(cells) < len(cols):
            cells += [""] * (len(cols) - len(cells))
        r = dict(zip(cols, [c.strip() for c in cells]))
        r["views"] = int(re.sub(r"[^\d]", "", r.get("views", "")) or 0)
        for k in ("seguidores", "mediana"):
            digits = re.sub(r"[^\d]", "", r.get(k, "") or "")
            r[k] = int(digits) if digits else None
        if r["views"] and r.get("gancho"):
            rows.append(r)
    return rows


def analyse(rows, formulas):
    used_median = any(r.get("mediana") for r in rows)
    for r in rows:
        base = r.get("mediana") or r.get("seguidores") or 0
        r["base"] = base
        r["multiplo"] = round(r["views"] / base, 2) if base else None
        r["formula_id"], r["formula"] = classify(r["gancho"], formulas)
        r["palavras"] = len(WORD_RE.findall(r["gancho"]))
        if score_hook:
            _, overall, verdict, flags = score_hook(r["gancho"])
            r["nota_gancho"], r["veredito_gancho"] = round(overall, 1), verdict
            r["alerta_cfn"] = any(f.startswith("CFN") for f in flags)
        else:
            r["nota_gancho"], r["veredito_gancho"], r["alerta_cfn"] = None, None, False
    ranked = sorted(rows, key=lambda r: -(r["multiplo"] or 0))
    third = max(1, len(ranked) // 3)
    top, bottom = ranked[:third], ranked[-third:]

    def med(items, key):
        vals = [i[key] for i in items if i.get(key) is not None]
        return round(statistics.median(vals), 1) if vals else None

    counts = {}
    for r in top:
        counts[r["formula"]] = counts.get(r["formula"], 0) + 1
    return {
        "base": "mediana da conta" if used_median else "número de seguidores",
        "n": len(ranked),
        "contas": len({r.get("conta", "") for r in ranked}),
        "reels": ranked,
        "formulas_topo": sorted(counts.items(), key=lambda kv: -kv[1]),
        "nota_topo": med(top, "nota_gancho"),
        "nota_base": med(bottom, "nota_gancho"),
        "palavras_topo": med(top, "palavras"),
        "palavras_base": med(bottom, "palavras"),
        "sem_classificacao": sum(1 for r in ranked if r["formula"] == "sem classificação"),
        "alertas_cfn": sum(1 for r in ranked if r["alerta_cfn"]),
    }


def render(a, out=sys.stdout):
    head = f"REFERÊNCIAS  ·  {a['n']} reels  ·  {a['contas']} contas  ·  base: {a['base']}"
    print("\n" + head, file=out)
    print("=" * max(len(head), 78), file=out)
    for r in a["reels"]:
        mult = f"{r['multiplo']:.1f}x" if r["multiplo"] else "   ?"
        score = f"{r['nota_gancho']:.0f}" if r["nota_gancho"] is not None else " -"
        fid = f"#{r['formula_id']:<2}" if r["formula_id"] else "-  "
        cfn = "  [CFN!]" if r["alerta_cfn"] else ""
        print(f"  {mult:>7}  nota {score:>3}  {fid} {r['formula'][:24]:<24} "
              f"{r.get('conta', '')[:16]:<16} {r['views']:>9,}".replace(",", ".") + cfn, file=out)
        print(f"           \"{r['gancho'][:96]}\"", file=out)
    print("-" * max(len(head), 78), file=out)
    print("O QUE ESTÁ FUNCIONANDO NESTE LOTE", file=out)
    if a["formulas_topo"]:
        print("  terço de cima:          " + ", ".join(f"{n} x{c}" for n, c in a["formulas_topo"][:4]), file=out)
    if a["nota_topo"] is not None:
        print(f"  nota mediana do gancho: topo {a['nota_topo']:.0f}  vs  base {a['nota_base']:.0f}", file=out)
    print(f"  tamanho mediano:        topo {a['palavras_topo']} palavras  vs  base {a['palavras_base']} palavras", file=out)
    print(f"  sem classificação:      {a['sem_classificacao']} de {a['n']}. Leia esses à mão: é onde mora "
          "uma fórmula que você ainda não tem.", file=out)
    if a["alertas_cfn"]:
        print(f"  alertas CFN:            {a['alertas_cfn']} gancho(s) com promessa de resultado ou antes/depois. "
              "Viralizar não torna ético: não copie esse formato.", file=out)
    print("\n  Lote coletado à mão é evidência, não prova. Doze Reels não mostram nada;\n"
          "  quarenta em seis contas mostram alguma coisa. Colete mais antes de acreditar.\n", file=out)


def to_markdown(a):
    lines = ["# Referências", "",
             f"{a['n']} reels de {a['contas']} contas, ranqueados pelo múltiplo sobre {a['base']}.", ""]
    for r in a["reels"]:
        mult = f"{r['multiplo']:.1f}x" if r["multiplo"] else "?"
        lines += [f"## {mult}  {r['formula']}  ({r.get('conta', '')})" + ("  [ALERTA CFN]" if r["alerta_cfn"] else ""),
                  f"- views: {r['views']:,}  base: {r['base']:,}".replace(",", "."),
                  f"- nota do gancho: {r['nota_gancho']}  palavras: {r['palavras']}",
                  f"- gancho: \"{r['gancho']}\"", ""]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Ranqueia Reels coletados pelo múltiplo sobre a própria conta.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo TSV, ou -")
    ap.add_argument("--ganchos", "--hooks", dest="ganchos", default=HOOKS, help="caminho do ig-reel/ganchos.json")
    ap.add_argument("--saida", "--out", dest="saida", help="grava também o arquivo de referências em markdown")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = read_rows(args.input)
    if not rows:
        print("nenhuma linha utilizável. Preciso de um arquivo separado por TAB com pelo menos views e gancho.",
              file=sys.stderr)
        sys.exit(2)
    formulas = load_formulas(args.ganchos)
    a = analyse(rows, formulas)
    if not formulas:
        print("aviso: ganchos.json não encontrado, fórmulas sem nome. Use --ganchos.", file=sys.stderr)
    if score_hook is None:
        print("aviso: nota_gancho.py não importável, notas puladas.", file=sys.stderr)

    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    if args.saida:
        path = os.path.expanduser(args.saida)
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        open(path, "w", encoding="utf-8").write(to_markdown(a))
        print(f"gravado em {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
