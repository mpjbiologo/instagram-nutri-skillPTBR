---
name: ig-resposta
description: >-
  Cuida dos comentários nos próprios Reels e posts do nutricionista: separa os
  que valem resposta e escreve as respostas, na ordem de valor. Use quando
  colarem os comentários, "responde esses", "cuida dos meus comentários",
  "alguém falou X no meu Reel", ou quando houver crítica, hater, dúvida de saúde
  ou possível paciente nos comentários.
---

# ig-resposta

A conversa embaixo do seu post é onde o alcance se decide. Cada resposta é mais
uma interação, as respostas da primeira hora fazem quase todo o trabalho, e no
Instagram uma resposta pode ser um Reel, que é o movimento mais subusado da
plataforma.

Mas o valor não é igual entre comentários, então esta skill separa antes de escrever.

## Entrada

A pessoa cola os comentários, de preferência com o @. Print serve. Não varra a
conversa com navegador.

## Triagem primeiro

Separe cada comentário num destes grupos e diga as contagens:

| grupo | o que é | o que recebe |
| --- | --- | --- |
| **PALAVRA-CHAVE** | a palavra que você pediu para comentarem | o material prometido, enviado à mão ou pela automação aprovada |
| **POSSÍVEL PACIENTE** | alguém descrevendo o problema que você atende | uma resposta de verdade em público, depois uma porta |
| **CONTEÚDO** | traz dado, discorda, amplia | a resposta mais longa da conversa |
| **PERGUNTA** | uma dúvida que muita gente tem | essa vira Reel, não só resposta |
| **CASO CLÍNICO** | alguém pedindo conduta individual ("tenho diabetes, posso...?") | resposta geral + orientação para consulta, nunca prescrição em comentário |
| **APOIO** | "🔥", "amei", uma marcação | uma curtida e 3 a 8 palavras no máximo |
| **RUÍDO** | propaganda, spam, má-fé, isca | nada, ou uma linha e fim |

Escreva nessa ordem e pare quando o valor acabar.

## O movimento que quase todo mundo perde

Se uma pergunta nos comentários é uma que trinta pessoas também têm, **responda
com um Reel**. O Instagram anexa o comentário ao vídeo novo, quem perguntou é
notificado, e uma pergunta com demanda real vira post com o gancho pronto.
Marque cada PERGUNTA que se qualifica e mande para `/ig-reel` como fórmula #16.

## Como responder

- **Responda a pergunta.** Se perguntaram como, diga como, na resposta. Não
  mande para a DM uma resposta que cabia ali.
- **Use o nome uma vez**, no começo, sem exclamação.
- **Acompanhe o tamanho.** Comentário de quatro palavras não ganha resposta de
  quatro linhas.
- **Caso clínico:** informação geral e segura, e a frase de que conduta
  individual depende de avaliação. Nunca prescreva dieta, dose de suplemento
  ou conduta para uma pessoa num comentário público.
- **Crítica:** reconheça primeiro a parte verdadeira, nas palavras da pessoa,
  depois mantenha a posição com fonte. Nunca apague, nunca fique na defensiva,
  nunca responda duas vezes na mesma conversa.
- **Colega discordando:** responda o argumento técnico, com fonte e respeito.
  Nunca desqualifique o profissional.
- **Hater:** nada. Resposta é alcance, e alcance é o que ele veio buscar.
  Oculte se for ofensivo. Usar os controles de comentário não é perder.
- **Possível paciente:** responda completo em público. A porta é uma frase no
  fim e é oferta de ajuda, não venda ("Se quiser, me chama no WhatsApp que eu
  explico como funciona a consulta"). Sem desconto, sem "condição especial".

## Comentários de palavra-chave

Se o post pediu uma palavra, esses comentários são o motivo do post. Cada um é
uma pessoa que levantou a mão. Responda cada um e mande o prometido. Se a pessoa
usa automação pelas ferramentas do Instagram ou parceiro aprovado, deixe rodar;
se não, é à mão e tudo bem nesse volume. Nunca mande DM em massa para quem não
comentou.

## Saída

Um bloco por grupo, cada resposta pronta para copiar e já humanizada e checada
por `/ig-etica`:

```
RESPOSTAS  ·  84 comentários  ·  41 PALAVRA-CHAVE, 2 POSSÍVEL PACIENTE, 3 CONTEÚDO,
           2 PERGUNTA, 1 CASO CLÍNICO, 33 APOIO, 2 RUÍDO

PALAVRA-CHAVE  (41)  mandar o guia. Uma linha cada, mesma simpatia, sem copiar e colar.

POSSÍVEL PACIENTE
@fulana - "eu como bem o dia todo e à noite ataco tudo"
> Isso é muito comum quando o almoço e o lanche têm pouca proteína e fibra.
> Se quiser, me chama no WhatsApp que eu explico como funciona a consulta.

CASO CLÍNICO
@ciclano - "tenho diabetes, posso fazer esse jejum?"
> Com diabetes, principalmente usando medicação, jejum precisa ser avaliado
> individualmente com seu médico e nutricionista. Não faça por conta própria.

PERGUNTA -> REEL
@beltrana - "e quem trabalha de madrugada?"
  34 curtidas nesse comentário. É Reel, não resposta. Fórmula #16.

RUÍDO  (2)  pulados. Responder dá alcance a eles.
```

Depois, a trava: nada é postado até a pessoa dizer sim. Ela cola as respostas.
