---
name: ig-reaproveitar
description: >-
  Transforma um material longo de nutrição (ebook, aula, live, podcast,
  artigo, palestra, plano alimentar modelo, transcrição de vídeo) numa semana
  de Reels e carrosséis. Use quando pedirem "reaproveita isso", "transforma em
  reels", "tenho um ebook/vídeo/aula", "corta isso", ou colarem algo longo
  querendo levar para o Instagram.
---

# ig-reaproveitar

Um bom material longo tem quatro a seis posts dentro. A maioria tira um e joga
o resto fora. Ebooks de receitas, materiais do programa de emagrecimento e
aulas são minas de conteúdo.

## Entrada

Transcrição, artigo, ebook, roteiro de aula, live, palestra. Se mandarem link e
esta sessão tiver ferramenta de transcrição, use; senão, peça para colar. Leia
tudo antes de extrair qualquer coisa.

Se for vídeo da própria pessoa, peça o arquivo também. Reel feito com o vídeo
dela falando ganha de um regravado.

Nunca use material com dado ou foto de paciente.

## Extraia, não resuma

Resumo de vídeo não é Reel. Ninguém quer o resumo. Passe pelo material e puxe o
que se sustenta sozinho:

| puxar | o que é |
| --- | --- |
| **Afirmações** | toda frase que começaria uma discussão (com base científica) |
| **Números** | toda quantidade, porção, preço, tempo, porcentagem, com a fonte |
| **Histórias** | todo momento com uma cena e uma consequência (anonimizado) |
| **Mecanismos** | todo "o jeito que isso funciona de verdade é..." |
| **Erros** | toda admissão de algo que deu errado |
| **Frases** | toda frase já pronta para citar |
| **Receitas** | toda receita que dá para mostrar em 30 segundos |

Liste o que achou, com contagem, antes de escrever. Se o material rende menos de
quatro itens, é ralo, e quatro posts espremidos dele serão ralos. Diga isso.

## Escolha o formato por item

- **Afirmação, erro, história:** Reel. Precisam de voz e rosto.
- **Mecanismo, lista, receita com passos:** carrossel. Precisam ser relidos.
- **Frase de efeito:** tela de story, não post.

## Monte a semana

Cada item vira um post, e cada post se sustenta sozinho. Quem vê nunca viu o
original. Nunca escreva "como eu falei no meu último vídeo".

Atribua uma fórmula de `ig-reel/ganchos.json` a cada um e varie. Cinco posts do
mesmo material com o mesmo formato de gancho parecem fábrica de conteúdo.

Ordem: a afirmação mais forte primeiro, a história no meio da semana, o
mecanismo por último.

Se o material é do programa pago ou de um ebook vendido, entregue o "o quê" no
post e deixe o "como completo" no produto. Mas o post tem que ensinar algo
sozinho: post que só tira o gosto vira propaganda vazia.

## Saída

```
FONTE: ebook "Café da manhã em 5 minutos" (38 páginas, 22 receitas)

ACHEI  4 afirmações, 11 números, 2 histórias, 3 mecanismos, 1 erro, 6 frases, 22 receitas

SEMANA
TER  REEL       #2  Comando Negativo  Pare de pular o café achando que economiza caloria
QUA  CARROSSEL  legenda tipo B        As 4 combinações que seguram a fome até o almoço
SEX  REEL       #18 Abertura em Ação  Overnight oats montado em 40 segundos
DOM  REEL       #20 Permissão         Você não precisa de café da manhã "fit"

Diga "escreve terça" e eu faço.
```

Depois escreva sob pedido, um de cada vez, cada um por `/ig-reel`, `/ig-humano`
e `/ig-etica`. Não despeje quatro roteiros prontos de uma vez. Vão soar iguais e
a pessoa não grava nenhum.
