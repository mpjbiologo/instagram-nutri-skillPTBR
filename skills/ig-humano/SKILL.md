---
name: ig-humano
description: >-
  Tira a cara de IA de qualquer rascunho em português: travessões, clichês de
  texto gerado, caracteres invisíveis, e dá nota num painel de cinco checagens
  antes de publicar. Use sempre que um texto precisar soar humano, quando
  pedirem "humaniza", "isso parece IA?", "tira os travessões", "tá com cara de
  ChatGPT", ou antes de mostrar qualquer legenda, roteiro, comentário, resposta
  ou DM.
---

# ig-humano

Dois scripts moram nesta pasta e os dois rodam. Use. Não faça isso no olho.

```bash
python3 humanizar.py rascunho.txt --relatorio       # limpa e mostra o que mudou
python3 detectar.py rascunho.txt                     # nota, cinco checagens
python3 detectar.py antes.txt depois.txt             # prova a diferença
```

Os dois leem `cliches.json`: cerca de 180 palavras e expressões de texto gerado
com troca por português simples, 18 tipos de caractere invisível, 11 trocas
tipográficas e 18 estruturas típicas. Os dois últimos blocos são de Instagram e
de marketing de nutrição ("sua melhor versão", "hábitos saudáveis", "emagrecer
com saúde"). O arquivo é para ser editado: se a pessoa usa de propósito uma
palavra que está ali, tire do arquivo.

## Por que isso importa mais no Instagram

Legenda é curta e roteiro é falado. Uma frase com cara de texto escrito pesa
mais numa legenda de 600 caracteres do que num artigo, e uma narração que
ninguém falaria assim fica óbvia no primeiro take. O problema não é um
detector marcar o post; é a pessoa rolando passar direto porque soou como
propaganda.

## O que é corrigido automaticamente

**1. Caracteres invisíveis.** Espaço de largura zero, word joiner, hífen oculto,
BOM, tags Unicode, espaço rígido. Teclado não produz isso, sobrevive ao copiar
e colar, e é o sinal mais mecânico de texto gerado.

**2. Tipografia.** Travessão vira vírgula, meia-risca vira hífen, aspas curvas
viram retas, reticências de um caractere viram três pontos. O travessão é o que
mais importa, e o script limpa a pontuação duplicada que sobra.

**3. Clichês.** "Mergulhar em", "no mundo acelerado de hoje", "é importante
ressaltar", "potencializar", "jornada", "holístico", "em suma", mais o bloco do
Instagram ("para de rolar", "neste vídeo", "segue pra mais dicas", "marca
alguém que precisa ver isso") e o de nutrição.

**Depois de rodar, releia a concordância.** Em português a troca de uma palavra
pode desencontrar artigo e adjetivo. O script evita as trocas mais perigosas,
mas a revisão final é sua.

## O que NÃO é corrigido automaticamente

Estruturas são **apontadas, não reescritas**, porque mudar o formato de uma
frase exige julgamento:

- "Não é só X, é Y" e "não apenas X, mas também Y"
- "Não é sobre X. É sobre Y."
- Trios de três palavras
- Linha de pergunta retórica: "O resultado?"
- Introdução de vídeo: "neste vídeo eu vou te mostrar"
- Lista com emoji no lugar de marcador
- Três palavras gritadas seguidas
- Muro de hashtags
- Isca genérica: "segue pra mais", "marca aquela amiga"
- Clichê motivacional: "sua melhor versão", "corpo dos sonhos"
- Gerundismo: "vou estar enviando"

Essa lista é trabalho seu. Reescreva cada linha apontada à mão, mantendo o
sentido, e rode `detectar.py` de novo. É isso que leva de REVISAR para PASSOU.

## As cinco checagens

| checagem | o que mede | cara de máquina |
| --- | --- | --- |
| VARIAÇÃO | variação no tamanho das frases | todas do mesmo tamanho |
| CONCRETUDE | números, nomes, marcadores concretos a cada 100 palavras | substantivos abstratos, nenhum número |
| CLICHÊS | ocorrências do léxico a cada 100 palavras | vocabulário pronto |
| DIGITAIS | invisíveis, travessões, aspas curvas a cada mil caracteres | tipografia perfeita demais |
| VOZ | marcas de fala informal ("pra", "tá", "a gente"), pessoa, estruturas | sem informalidade, revelações encenadas |

O veredito pesa a média em 60% e a **pior checagem** em 40%, porque basta um
sinal. PASSOU exige nota geral 70+ e nenhuma checagem abaixo de 55.

## Diga isso com honestidade

São cinco heurísticas locais. Rodam no computador da pessoa e nada é enviado.
**Não** são GPTZero, Originality, Copyleaks, Winston ou Turnitin, e não prometem
o veredito deles. Nunca diga que um texto é "indetectável".

E mais importante para nutricionista: **humanizar não é esconder o uso de IA.**
O Código de Ética (Res. CFN 856/2026, Art. 37) pede que materiais feitos com IA
indiquem esse uso. O objetivo aqui é o texto ficar bom de ler e com a voz da
pessoa, não fingir que não houve IA. Mantenha a linha de declaração no rodapé.

## Ordem de operação

1. `humanizar.py rascunho.txt -o limpo.txt --relatorio`
2. Leia as estruturas apontadas. Reescreva essas linhas você mesmo.
3. `detectar.py rascunho.txt limpo.txt` para mostrar o antes e depois.
4. Se não PASSOU, corrija a checagem mais fraca e repita. Duas rodadas é
   normal. Cinco quer dizer que o rascunho foi escrito por fórmula, e a solução
   é outro rascunho, não mais rodadas.
5. Mostre o texto limpo e a nota. Nunca só a nota.
