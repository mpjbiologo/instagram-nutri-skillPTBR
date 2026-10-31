---
name: ig-carrossel
description: >-
  Monta um carrossel de Instagram de nutrição: a capa que faz arrastar, o texto
  de cada slide e os arquivos 1080x1350 para subir. Use quando pedirem
  "carrossel", "slides", "post de arrastar", "transforma isso em carrossel", ou
  quando a ideia for uma lista ou passo a passo que morreria como imagem única.
---

# ig-carrossel

Carrossel é o formato que mais segura tempo no grid, porque arrastar é uma
interação e rolar não é. E ganha segunda chance: o Instagram pode mostrar de
novo a partir de um slide posterior para quem não interagiu, então o slide
dois também precisa se sustentar sozinho.

O formato premia uma ideia quebrada em passos. Pune uma legenda picada em pedaços.

## Quando usar no lugar de Reel

Quando a ideia tem **sequência e precisa ser relida**: passos, um método com
partes, comparação de rótulos, uma lista para print (lista de mercado, trocas,
porções). Reel quando a ideia tem movimento, rosto ou uma entrega que precisa
ser vista acontecendo.

Se a ideia é uma afirmação só, não é nenhum dos dois: mande para `/ig-reel`.

## Estrutura

6 a 10 slides. O limite é 20 e 20 é livro que ninguém termina.

```
1         CAPA      o gancho. Seis palavras ou menos, legível em miniatura.
                    Uma linha de promessa embaixo (promessa de informação).
2         O PORQUÊ  por que isso importa, numa frase. Também é segunda capa.
3 a N     UMA IDEIA POR SLIDE. Título de 3 a 7 palavras, no máximo 25 palavras.
N+1       RESUMO    tudo como lista. É o slide do print.
ÚLTIMO    CTA       uma ação. Salvar, comentar uma palavra ou seguir. Uma.
```

## Regras do texto

- **A capa é 80% do resultado.** Seis palavras. Grande. E nunca "-10 kg",
  número de balança ou corpo de paciente.
- **Pense no corte do grid.** Faça em 1080x1350 e mantenha o texto da capa bem
  no meio, longe dos 120 pixels de cada borda.
- **Numere os slides** (3/8). Mais gente termina quando vê o fim.
- **Nenhum slide é parágrafo.** Se não cabe em 25 palavras, são dois slides.
- **O resumo é o que as pessoas printam e mandam.** Envio é o sinal mais forte.
- **O @ e o CRN em todo slide**, pequeno, no canto. Print viaja sem você.
- **Fonte em todo dado.** Slide com número tem a fonte embaixo (Vigitel, TACO,
  Guia Alimentar, artigo).
- **Marcas: várias ou nenhuma.** Comparação de rótulos mostra mais de uma
  marca e não elege "a melhor" para comprar (Art. 72 e 74 do código).
- **Texto alternativo na capa, no mínimo.**

## Gerando os arquivos

O Instagram pede 1080x1350 (4:5), JPEG ou PNG, até 20 itens. Monte em HTML e
exporte cada slide:

```bash
# uma <section> por slide, 1080x1350, page-break-after: always
# depois Chrome headless --print-to-pdf, ou o conversor HTML->imagem que você já usa
```

`width:1080px; height:1350px`, uma cor de destaque e fonte de no mínimo 32px,
porque é lido no celular a um terço do tamanho real. Se houver identidade
visual da marca (cores, fontes), use e não invente paleta. Imagens geradas por
IA não podem simular pessoas reais nem resultados (Art. 38).

## Saída

Primeiro o texto slide a slide, numa lista numerada que a pessoa lê em dez
segundos e edita antes de gerar qualquer coisa. Depois a **legenda**, que para
carrossel é o tipo B de `/ig-legenda`.

Passe os dois por `/ig-humano` e `/ig-etica`. Gere os arquivos só depois que a
pessoa aprovar o texto.

```
CARROSSEL  ·  8 slides

1  CAPA    O IOGURTE "PROTEICO" MENTE?
           Li o rótulo de 12. Só 2 passaram.
2  PORQUÊ  "Proteico" na embalagem não diz quanto tem. O rótulo diz.
3          ONDE OLHAR
           Tabela nutricional, linha "proteínas", por porção.
...
7  RESUMO  Os 4 critérios, em ordem.
8  CTA     Salva para levar no mercado.

Legenda: tipo B, gancho na linha 1, um pedido, 3 tags, rodapé de IA.
```

Nada é enviado. A pessoa posta.
