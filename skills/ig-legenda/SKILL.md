---
name: ig-legenda
description: >-
  Escreve a legenda de Instagram de um post de nutrição: a linha que sobrevive
  ao corte do "... mais", o corpo, o único pedido, os termos de busca e até
  cinco hashtags, e revisa antes de publicar. Use quando pedirem "escreve a
  legenda", "legenda para esse post", "o que coloco na descrição", quando houver
  um Reel ou carrossel pronto precisando de texto, ou perguntas sobre hashtags.
---

# ig-legenda

Um script mora nesta pasta e roda:

```bash
python3 legenda.py legenda.txt
python3 legenda.py legenda.txt --busca "nutricionista em Itaúna,emagrecimento"
```

Ele mostra a legenda como o feed mostra: os primeiros 125 caracteres numa
caixa, o resto atrás do toque. Leia essa caixa antes de qualquer outra coisa.

## Primeiro, decida qual é o trabalho da legenda

**Tipo A: o vídeo já prendeu.** Um Reel carrega o gancho nos dois primeiros
segundos. A legenda não é um segundo gancho, e competir com o vídeo faz perder
os dois. O trabalho dela é o pedido, o contexto que dá sentido ao pedido e as
palavras que as pessoas buscam.

**Tipo B: a legenda é o conteúdo.** Foto, imagem única, capa de carrossel. Aqui
a primeira linha é o gancho e funciona como gancho de Reel: concreta, curta, e
cortada num suspense, não no meio de uma oração.

Diga qual está escrevendo. Se for Reel com gancho forte, escreva A e explique.

## O formato

```
Linha 1     125 caracteres visíveis. Tipo A: o pedido, direto. Tipo B: o gancho.
            Nunca saudação, nunca hashtag, nunca emoji como primeiro caractere.
Corpo       parágrafos curtos, uma linha em branco entre eles. Dois a seis.
            É aqui que moram os termos de busca.
O pedido    um. Comentar uma palavra, salvar, ou chamar no WhatsApp/DM. Um.
Hashtags    até cinco, numa linha própria no fim, ou nenhuma.
Rodapé      quando o texto foi feito com ajuda de IA, uma linha dizendo isso
            (ex.: "Texto feito com apoio de IA e revisado por mim"). Art. 37.
```

O limite é 2.200 caracteres e quase nada precisa disso.

## Hashtags, com honestidade

Hashtag não é mais alavanca de alcance. **O Instagram limitou a cinco hashtags
por post em 18/12/2025**, antes eram trinta. Use até cinco, específicas, como
rótulo de assunto. Aquele bloco de vinte salvo nas notas do celular virou peso
morto e o script vai reprovar.

`#viral`, `#fyp`, `#explore`, `#saude`, `#dieta`, `#foco` não descrevem nada.

## Termo de busca vale mais que hashtag

A busca do Instagram lê o texto da legenda. Então a frase pela qual a pessoa
quer ser encontrada vai na legenda como alguém digitaria, numa frase normal:
"nutricionista em Itaúna" no terceiro parágrafo, não "#nutricionistaitauna"
num bloco no fim. Para nutricionista com consultório, cidade + especialidade é
o termo mais valioso que existe.

Peça dois ou três termos e passe para o script com `--busca`.

## Regras

- **Sem link na legenda.** Legenda não é clicável. Link vai na bio ou na DM.
- **Um pedido.** Dois é o mesmo que nenhum. O script conta.
- **Palavra-chave que dá para digitar.** Uma palavra, sem espaço, sem emoji, e
  falada no vídeo também. "Comenta CAFÉ" funciona. "Comenta 'quero o guia do
  café'" não.
- **Emoji é pontuação, não enfeite.** O script aponta mais de 4 a cada 100
  caracteres.
- **Texto alternativo vale 20 segundos.** Em carrossel e foto, escreva.
- **Preço pode, chamariz não.** Se citar valor de consulta, sem "só hoje",
  "desconto", "de R$ X por R$ Y" ou sorteio (Art. 68).

## O ciclo

1. Decida Tipo A ou B e diga qual.
2. Escreva.
3. Rode `/ig-humano`. Legenda é curta, então clichê aparece mais aqui que em
   qualquer lugar.
4. Rode `legenda.py` com os termos de busca. Corrija toda FALHA. Decida em voz
   alta cada ATENÇÃO.
5. Rode `/ig-etica` (com `--ia`). Nada VEDADO passa.
6. Entregue o bloco pronto para copiar, e depois:

```
LEGENDA PRONTA
tipo:       A - o Reel carrega o gancho
visível:    118 de 125 caracteres antes do corte
pedido:     um, comentar CAFÉ
hashtags:   3
busca:      "nutricionista em Itaúna" no parágrafo 3
revisão:    PRONTA
ética:      sem alertas, rodapé de IA incluído
```

Nada é publicado. A pessoa cola.
