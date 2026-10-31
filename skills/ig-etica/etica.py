#!/usr/bin/env python3
"""
etica.py - revisa um roteiro, legenda, carrossel, story ou DM contra os pontos
do Código de Ética e Conduta da(o) Nutricionista que mais aparecem em redes
sociais (Resolução CFN nº 856/2026).

Três níveis:
  VEDADO    não publique assim. Reescreva.
  ATENÇÃO   pode ser problema dependendo do contexto. Revise.
  LEMBRETE  provavelmente ok, mas confira a condição indicada.

O que é:  uma lista de regex em regras_cfn.json, rodando no seu computador.
O que NÃO é:  parecer jurídico, nem orientação do CRN. Regex dá falso positivo
e falso negativo. Imagens e vídeos não são analisados, só texto. A palavra
final é sua e, na dúvida, do seu CRN.

Uso
  python3 etica.py legenda.txt
  python3 etica.py roteiro.txt --ia          # o texto foi feito com ajuda de IA
  python3 etica.py legenda.txt --json
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RULES = os.path.join(HERE, "regras_cfn.json")
LABEL = {"VEDADO": "VEDADO", "ATENCAO": "ATENÇÃO", "LEMBRETE": "LEMBRETE"}
ORDER = {"VEDADO": 0, "ATENCAO": 1, "LEMBRETE": 2}


def analyse(text, data, used_ai=False):
    findings = []
    for r in data["regras"]:
        hits = [m.group(0).strip() for m in re.finditer(r["regex"], text)]
        if hits:
            findings.append({
                "id": r["id"], "nivel": r["nivel"], "nome": r["nome"], "artigo": r["artigo"],
                "trechos": sorted(set(hits))[:4], "qtd": len(hits), "correcao": r["correcao"],
            })
    ia = data.get("ia")
    if ia and used_ai and not re.search(ia["regex_declaracao"], text):
        findings.append({
            "id": "ia-nao-declarada", "nivel": ia["nivel"], "nome": ia["nome"], "artigo": ia["artigo"],
            "trechos": [], "qtd": 1, "correcao": ia["correcao"],
        })
    findings.sort(key=lambda f: ORDER[f["nivel"]])
    levels = {f["nivel"] for f in findings}
    verdict = ("NÃO PUBLICAR" if "VEDADO" in levels else
               "REVISAR" if "ATENCAO" in levels else
               "OK, CONFIRA OS LEMBRETES" if findings else "SEM ALERTAS")
    return {"achados": findings, "veredito": verdict}


def render(a, data, used_ai, out=sys.stdout):
    head = "CHECAGEM ÉTICA CFN  ·  " + data.get("fonte", "")
    print("\n" + head, file=out)
    print("=" * max(len(head), 62), file=out)
    if not a["achados"]:
        print("  Nenhum alerta no texto.", file=out)
    for f in a["achados"]:
        print(f"\n  {LABEL[f['nivel']]:<9} {f['nome']}   [{f['artigo']}]", file=out)
        if f["trechos"]:
            print("            trecho: " + " | ".join(f"\"{t}\"" for t in f["trechos"]), file=out)
        print(f"            {f['correcao']}", file=out)
    print("\n" + "-" * 62, file=out)
    print(f"  VEREDITO  {a['veredito']}", file=out)
    if data.get("ia", {}).get("imagem"):
        print(f"\n  Lembrete fixo: {data['ia']['imagem']}", file=out)
    print("  Esta é uma checagem automática por palavras. Não substitui o código nem o CRN.\n", file=out)


def main():
    ap = argparse.ArgumentParser(description="Checagem ética CFN para conteúdo de nutrição.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo, ou -")
    ap.add_argument("--ia", action="store_true", help="o texto foi produzido com ajuda de IA")
    ap.add_argument("--regras", default=RULES, help="caminho do regras_cfn.json")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    data = json.load(open(args.regras, encoding="utf-8"))
    text = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = analyse(text, data, used_ai=args.ia)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a, data, args.ia)
    sys.exit(2 if a["veredito"] == "NÃO PUBLICAR" else (1 if a["veredito"] == "REVISAR" else 0))


if __name__ == "__main__":
    main()
