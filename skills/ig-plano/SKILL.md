---
name: ig-plano
description: >-
  Monta a semana no Instagram de um nutricionista: o que postar, em que
  formato, quando, e com quem interagir. Use quando pedirem "planeja minha
  semana", "o que eu posto", "calendário de conteúdo", "não tenho assunto",
  ou quiserem cronograma de posts e lista de interação.
---

# ig-plano

A sala de controle. O resto do pacote executa; esta decide o que executar. Rode
uma vez por semana, no mesmo dia.

## Entrada

Se `~/.claude/instagram/voz.md`, `referencias.md` e `historico.md` existirem,
leia. O arquivo de referências é a evidência da própria pessoa (de `/ig-viral`)
e vale mais que qualquer padrão daqui. O histórico evita repetir tema das
últimas duas semanas.

Se não existirem, pergunte quatro coisas e anote:

1. O que a pessoa oferece e para quem (ex.: consulta presencial e online,
   programa de emagrecimento, convênios e parcerias).
2. Os três ou quatro temas pelos quais quer ser conhecida.
3. O que aconteceu de verdade esta semana: uma dúvida que vários pacientes
   trouxeram, um rótulo que chamou atenção no mercado, um mito que apareceu na
   TV, uma receita que deu certo, um erro. É daí que vêm os posts. (Nada que
   identifique paciente.)
4. Dez contas para quem vale a pena ser visto.

## O que postar

Quatro a cinco posts por semana, pelo menos três Reels. Reel é o único formato
que chega com regularidade em quem não segue. Carrossel aprofunda com quem já
segue. Stories são diários e planejados à parte (`/ig-stories`).

Misture ao longo da semana, nunca dois do mesmo tipo seguidos:

| tipo | frequência | função |
| --- | --- | --- |
| **Prova** | 1 por semana | competência demonstrada: um teste de rótulos, uma comparação de preços, um estudo explicado. Nunca resultado de paciente. Reel. |
| **Ensino** | 1 a 2 por semana | uma coisa que a pessoa pode fazer hoje. Reel ou carrossel. |
| **Opinião** | 1 por semana | uma posição que pode custar seguidor (com base científica). Reel. |
| **História** | 1 a cada 15 dias | uma cena de consultório anonimizada, ou da sua rotina. Reel. |
| **Oferta** | 1 a cada 15 dias | como funciona a consulta, dito com clareza, sem desconto nem sorteio. Carrossel ou stories. |

Para cada post: tema, o ângulo específico do que aconteceu na semana, formato e
número da fórmula de `ig-reel/ganchos.json`. Não um assunto, um ângulo.
"Proteína" não é plano. "Os 12 iogurtes 'proteicos' do mercado que eu li o
rótulo" é um Reel.

Datas que rendem no Brasil: começo de ano, Carnaval, Páscoa (chocolate), festa
junina, férias, Black Friday (como tema educativo, nunca como promoção de
consulta), festas de fim de ano.

## Quando postar

Quando o público está acordado e fora do trabalho. Para público geral,
geralmente começo da noite. Mas diga com clareza: **o horário importa muito
menos que os dois primeiros segundos.** Se a pessoa está otimizando horário
antes dos ganchos funcionarem, está polindo a coisa errada.

## A rodada de interação, que não é opcional

20 minutos por dia, antes de postar. Lista de 10:

- **5 de alcance:** contas com o público que a pessoa quer, onde um bom
  comentário é visto. Comente cedo.
- **3 colegas:** mesmo tamanho, mesma área. O grupo que retribui.
- **2 locais:** academias, estúdios de pilates, clínicas e comércios da cidade
  (parcerias existentes ou possíveis). Nunca ofereça desconto em comentário.

Entregue a lista para `/ig-comentario`.

## Saída

```
SEMANA DE 03/11

SEG  só interação  (20 min, lista abaixo)
TER  19h30  REEL       PROVA     #6  O Teste         - 12 iogurtes "proteicos", só 2 passam
QUA  só stories + interação
QUI  19h    CARROSSEL  ENSINO    legenda tipo B      - montando o prato em 4 passos
SEX  19h30  REEL       OPINIÃO   #20 Permissão       - você não precisa cortar o pão
SÁB  -
DOM  18h    REEL       HISTÓRIA  #21 Meio da Frase   - "...e ela pulava o almoço fazia 8 anos"

STORIES  todo dia, 3 a 5 telas, caixinha de pergunta na quinta.

INTERAÇÃO  (5 alcance / 3 colegas / 2 locais)
  ...

Diga "escreve terça" e eu faço.
```

Grave o plano em `~/.claude/instagram/plano.md` para as outras skills lerem.
Nada é agendado nem postado. É um plano e a pessoa executa.
