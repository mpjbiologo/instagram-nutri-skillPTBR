---
name: ig-auditoria
description: >-
  Análise do que o nutricionista já postou: quais Reels funcionaram de verdade,
  por quê, e o que parar de fazer. Use quando colarem estatísticas (insights)
  do Instagram ou posts antigos perguntando "o que está funcionando", "por que
  esse flopou", "lê minhas métricas", "audita meu conteúdo", ou quiserem saber
  o que fazer mais.
---

# ig-auditoria

A única fonte honesta do que funciona para uma conta é a própria conta. Toda
regra de todo guia de Instagram, incluindo as deste pacote, é uma suposição
inicial. Os últimos 30 posts da pessoa são a evidência.

## Entrada

Peça o que a pessoa tiver:

- Estatísticas por post: visualizações, alcance, interações, tempo de exibição,
  salvamentos, compartilhamentos, seguidores ganhos e a parcela do alcance que
  veio de não seguidores. Print serve.
- Ou o gráfico de retenção do melhor e do pior Reel recente. Esse print vale
  mais que todo o resto junto.
- Ou só os posts e as views, que basta para uma primeira passada.
- Se houver: quantas pessoas chamaram no WhatsApp ou marcaram consulta depois
  de cada post. Para quem atende, essa é a métrica que paga as contas.

Leia também `~/.claude/instagram/historico.md`, que registra a fórmula de cada post.

## O que medir de verdade

View bruta é o número menos útil da tela, porque depende de quantos já seguem.
Calcule estes e mostre a conta:

| métrica | como | o que diz |
| --- | --- | --- |
| **Múltiplo** | views / mediana de views da conta | se foi acerto real ou um dia normal |
| **Alcance de não seguidores** | % do alcance de quem não segue | se viajou |
| **Retenção aos 3s** | quem ficou aos 3s / quem começou | se o gancho funcionou. É a nota do gancho. |
| **Tempo médio** | direto das estatísticas | se o meio funcionou |
| **Envios por alcance** | compartilhamentos / alcance | o sinal mais forte que existe |
| **Seguidores por alcance** | seguidores / alcance | se o perfil converteu a atenção |
| **Contatos por post** | WhatsApp/DMs de agendamento ligados ao post | se virou paciente |

Ranqueie por múltiplo e envios por alcance, não por views. Um Reel com 4 mil
views e 90 envios ganhou do de 60 mil e 11 envios.

## Ache o padrão

Com os cinco melhores e os cinco piores lado a lado, procure o que separa, e
esteja disposto a concluir algo que a pessoa não vai gostar:

- **Retenção aos 3 segundos.** Se topo e base diferem aqui, é o gancho e mais
  nada.
- **Fórmula de gancho.** Quais números de `ig-reel/ganchos.json` estão no topo?
- **Formato.** Reel, carrossel, foto.
- **Duração.** Menos de 15s, 15 a 30s, 30 a 60s, mais de 60s.
- **Tema.** Emagrecimento, receita, mito, rótulo, bastidor.
- **Se a pessoa respondeu os comentários na primeira hora.**
- **Dia e horário.** Por **último**, e só se o resto não mostrar nada.

Diga a conclusão como afirmação com a evidência junto, e quão confiante ela é.
Com 30 posts dá para ver padrão. Com 6 não, e dizer isso é melhor que inventar.

**Se algum dos posts que mais performaram fere o Código de Ética** (antes/depois,
promessa de kg, promoção), diga com todas as letras: o resultado não justifica,
arquive e não repita. Rode `/ig-etica` nos textos.

## A distinção que economiza meses

**Reel com views e sem seguidores não é Reel ruim, é problema de perfil.** Reel
sem views é problema de gancho. Separe os dois antes de recomendar. Se o alcance
de não seguidores é alto e seguidores por alcance é baixo, pare de mexer no
gancho e vá para `/ig-perfil`. Se ganha seguidor e não ganha contato, o
problema está no caminho até o WhatsApp (bio, link, destaque "Como funciona").

## Saída

```
AUDITORIA  ·  31 posts  ·  01/08 - 30/10  ·  mediana 1.900 views

TOP 5 POR MÚLTIPLO
  18.2x  #16 Pergunta Literal   34.600 views  62% não seguidores  ret@3s 71%  128 envios
   6.4x  #6  O Teste            12.200 views  48% não seguidores  ret@3s 64%   71 envios
  ...

BASE 5
   0.3x  #11 Lista              600 views     9% não seguidores   ret@3s 31%    2 envios
  ...

O QUE OS DADOS DIZEM
1. Retenção aos 3s é a história toda. Topo com média de 66%, base com 33%.
2. Perguntas literais de paciente: média 8,1x contra 0,9x do resto. n=5.
   O sinal mais forte daqui, e não é por pouco.
3. Receitas têm views e nada mais. Alcance alto, nenhum envio, nenhum contato.
4. Dia da semana não mostra nada. Pare de otimizar isso.

PARE: listas genéricas de dicas.
FAÇA MAIS: perguntas de consultório respondidas com um dado e uma fonte.
```

Depois entregue as conclusões para `/ig-plano`, para a próxima semana ser
montada com a evidência da própria pessoa, e para `/ig-viral`, para filtrar as
referências pelas fórmulas que funcionam nesta conta.
