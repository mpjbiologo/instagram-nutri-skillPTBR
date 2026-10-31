---
name: ig-perfil
description: >-
  Dá nota de 0 a 100 para um perfil de Instagram de nutricionista numa rubrica
  de 13 itens (incluindo conformidade com o Código de Ética) e reescreve o que
  perde pontos: campo de nome, bio, CRN, link, destaques, fixados, grid. Use
  quando pedirem "otimiza meu perfil", "arruma minha bio", "dá nota pro meu
  Instagram", "por que ninguém me segue", ou colarem o perfil perguntando como
  está.
---

# ig-perfil

Quase todo mundo otimiza a coisa errada aqui. O perfil não é uma vitrine que as
pessoas ficam olhando. É uma **tela de decisão**, que a pessoa abre depois de um
Reel, e tem uns três segundos para responder: tem mais disso aqui, e é para mim?

## Entrada

Peça para colar ou mandar print de: campo de nome, @, bio, para onde vai o
link, nomes dos destaques, o que está fixado e as nove primeiras capas do grid.
Um print do topo do perfil mais as duas primeiras linhas do grid basta para a
primeira passada.

Não faça login no Instagram pela pessoa.

## Dê a nota

Leia `rubrica.json` nesta pasta. Treze itens, 100 pontos, cada um com o que é
nota cheia e como costuma falhar. Avalie todos, mostre a tabela, dê o total.
Seja honesto: a maioria dos perfis fica entre 30 e 40 na primeira vez, e nota
generosa não serve para nada.

O item **conformidade_etica** zera se houver antes/depois corporal, exame de
paciente, promessa de resultado, promoção ou sorteio de consulta, ou marca de
suplemento sem declaração de conflito, em qualquer lugar do perfil (grid,
destaques, bio). Rode `/ig-etica` no texto da bio e confira os destaques à mão.

```
NOTA DO PERFIL  38/100

  campo de nome       2/11   só o nome, nenhuma palavra que alguém busca
  bio 1ª linha        3/11   "Nutricionista | Apaixonado por saúde"
  CRN                 6/6    na bio
  fixados             0/10   nada fixado
  destaques           2/7    "Dia a dia", "2024", "Aleatório"
  conformidade ética  0/10   destaque "Resultados" com antes/depois
  ...
```

## Depois reescreva, nesta ordem

Corrija em ordem decrescente de pontos perdidos. Não reescreva tudo de uma vez:
a pessoa precisa ir lá mudar cada coisa. **Exceção: conformidade ética vem
primeiro sempre**, porque é risco de processo ético, não de alcance.

**0. Conformidade ética.** Arquivar o que fere o código (destaque de
antes/depois, post de promoção). Diga exatamente quais itens e por quê.

**1. Campo de nome (30 caracteres).** A linha em negrito embaixo da foto, não o
@. É o campo que a busca do Instagram lê. Formato que funciona:
`{Nome} | {o que faz, em palavras buscadas}`. Para quem atende presencial, a
cidade vale ouro: `Marcos | Nutricionista Itaúna`. Dê três opções.

**2. Primeira linha da bio.** Para quem é e o que muda. Não é cargo nem lista de
adjetivos. Sem promessa de resultado: "emagrecimento sem dieta da moda" pode;
"perca 10 kg" não. O resto dos 150 caracteres traz uma prova (formação,
especialidade) ou uma oferta clara (presencial em tal cidade + online) e o CRN.

**3. Os três fixados.** Três funções diferentes: o melhor conteúdo educativo, a
explicação mais clara de como funciona a consulta, a melhor apresentação da
pessoa. É a correção de maior impacto do perfil e leva quatro toques.

**4. Destaques.** Quatro a seis, com o nome das perguntas que paciente faz: Como
funciona, Consulta online, Onde atendo, Dúvidas, Sobre mim. Nunca "Resultados"
com fotos de pacientes.

**5. O link.** Um destino que combina com a bio: WhatsApp de agendamento ou a
página de captação. Dois já é cardápio.

**6. Capas do grid.** As nove primeiras em miniatura. Capa escolhida, com até
quatro palavras. Nenhuma capa com "-8 kg" ou corpo de paciente.

## Saída

Tabela de notas, depois as reescritas em blocos prontos para copiar, na ordem
de correção, cada uma passada por `/ig-humano` e `/ig-etica`. Refaça a nota no
fim e mostre a diferença com honestidade. Se a reescrita chega a 84 e não a 98,
diga 84, e diga o que falta: geralmente grid, hábito de stories e um post fixado
que ainda não existe. Nada disso é reescrita.

Nada é salvo no Instagram por esta skill. A pessoa edita cada campo.
