---
name: ig-reel
description: >-
  Escreve um Reel de nutrição a partir de uma ideia crua: três ganchos de 26
  fórmulas com nota, o roteiro falado, o texto da tela e o mapa de tempos, na
  voz do nutricionista e já checado contra o Código de Ética do CFN. Use quando
  pedirem um Reel, roteiro de vídeo curto, gancho, "faz um reel sobre X", "o que
  eu falo nesse vídeo", ou quando a pessoa vai gravar e não tem a primeira frase.
---

# ig-reel

Transforma uma ideia num Reel que alguém assiste até o fim, sem ferir o Código
de Ética do nutricionista.

Dois scripts moram nesta pasta e os dois rodam de verdade. Use. Não avalie o
gancho no olho e não chute a duração.

```bash
python3 nota_gancho.py ganchos.txt              # ranqueia as opções de gancho
python3 nota_gancho.py --gancho "uma frase"     # avalia um só
python3 tempos.py roteiro.txt --alvo 30         # mapa de tempos antes de gravar
```

## Antes de escrever

1. Leia `~/.claude/instagram/voz.md` se existir. É o perfil de voz: como a
   pessoa fala na câmera, o que nunca diz, com quem fala. Se não existir, peça
   **três Reels ou legendas dela**, deduza a voz e escreva o arquivo a partir de
   `templates/voz.md`. Roteiro na voz errada não serve, porque ela precisa falar
   em voz alta.
2. Leia `ganchos.json` nesta pasta. São 26 fórmulas, cada uma com modelo,
   exemplo de nutrição, versão para a tela, para que serve, como estraga e um
   campo `cfn` com o risco ético quando houver.
3. Se a ideia estiver rala, não encha linguiça. Faça uma pergunta só, agrupada:
   o que aconteceu, com quem (sem identificar paciente), e qual o dado concreto
   (quantidade, preço, tempo, fonte). Um Reel precisa de uma coisa verdadeira e
   específica.
4. Se `~/.claude/instagram/referencias.md` existir, leia. `/ig-viral` grava esse
   arquivo, e ele é a evidência da própria pessoa sobre quais fórmulas estão
   funcionando no nicho dela agora. Vale mais que os padrões daqui.

## O formato

Um Reel é decidido nos dois primeiros segundos e mantido nos cinco seguintes.

```
0:00 - 0:02   GANCHO      a afirmação. Fala e texto de tela escritos separados.
                          Movimento no primeiro quadro, não um rosto parado.
0:02 - 0:07   O PORQUÊ    por que isso importa para quem está vendo. Uma frase.
0:07 - ...    O CORPO     uma ideia por fala, e a imagem muda a cada fala.
ÚLTIMOS 3s    A ENTREGA   entregue o que o gancho prometeu, depois o único pedido.
ÚLTIMA FRASE  O LOOP      repita uma palavra do gancho para o replay emendar.
```

Duração: 15 a 45 segundos é a faixa útil. Abaixo de 7 segundos só o número de
loops infla.

## O ciclo

**1. Três ganchos, não um.** Escolha três fórmulas de `ganchos.json` que caibam
de verdade na ideia e escreva fala + texto de tela de cada. Fórmulas
diferentes, não três versões da mesma.

**2. Dê nota.** Coloque as três falas num arquivo, uma por linha, e rode
`nota_gancho.py`. Mostre o ranking. Se o primeiro está abaixo de 50, o gancho
ainda não existe. Qualquer gancho com "ELIMINATÓRIO: CFN" sai da lista, por
melhor que seja a nota.

**3. Escreva o roteiro** no gancho vencedor. Português falado, do jeito que a
pessoa fala: "pra", "tá", "a gente". Frases curtas. Nenhuma frase que ela
precise ensaiar.

**4. Cronometre.** Rode `tempos.py roteiro.txt --alvo {duração}`. Corrija todo
alerta: gancho passando de 3 segundos, fala acima de 4 segundos, sequência de
falas sem nada concreto, falta de loop. Rode de novo até limpar.

**5. Humanize.** Passe o roteiro por `/ig-humano`. Frase com cara de texto
escrito fica óbvia assim que alguém fala em voz alta.

**6. Cheque a ética.** Rode `/ig-etica` no roteiro e no texto da tela (com
`--ia`, porque foi feito com IA). Nada com VEDADO sai daqui.

**7. Entregue o bloco.** Roteiro num bloco de código, texto de tela numa lista
separada com minutagem, e depois:

```
REEL PRONTO
gancho:     #3 Ninguém Te Conta, nota 82 FORTE
duração:    28,4s em 9 falas a 150 ppm
tela:       6 cartelas
humano:     4 marcas removidas, nota humana 78 PASSOU
ética:      sem alertas (lembrete: declarar uso de IA)
legenda:    rode /ig-legenda em seguida

Responda "sim" para registrar, ou diga o que mudar.
```

**8. Nunca publique.** Esta skill entrega um roteiro. A pessoa grava e posta.
No "sim", acrescente em `~/.claude/instagram/historico.md` a data, a fórmula
usada e a primeira frase, para `/ig-auditoria` ter histórico depois.

## O texto da tela é um roteiro à parte

Escreva separado, sempre. Ele é lido antes de ser ouvido.

- **Seis palavras ou menos por cartela.** É lido com o celular a um palmo, por
  alguém que ainda não está ouvindo.
- **A cartela do gancho aparece no quadro 1**, não depois de um silêncio.
- **Respeite a área segura.** Num quadro 1080x1920, nada acima de y=230 nem
  abaixo de y=1440, e deixe livres os 230 pixels da direita. A interface cobre
  tudo fora disso: legenda, botões, faixa de áudio.
- **Legenda queimada no corpo.** A maioria assiste sem som primeiro.

## Regras que fazem diferença

- **Uma ideia por Reel.** Se o roteiro tem duas, são dois Reels. Diga isso.
- **Número no lugar de adjetivo.** "9 colheres de chá de açúcar" ganha de
  "muito açúcar". Se a pessoa não deu o número, pergunte em vez de contornar.
- **Corte a introdução.** Sem "oi, gente", sem "neste vídeo", sem nome, sem
  vinheta. O vídeo começa na frase que normalmente viria no segundo seis.
- **Mude a imagem a cada fala.** Plano parado por 8 segundos é onde a pessoa
  sai, e `tempos.py` aponta.
- **Um pedido no final.** Comentar uma palavra, salvar ou seguir. Um.
- **Nunca invente.** Nada de número, paciente ou resultado inventado em nome da
  pessoa, nem como exemplo. Se precisa de um número desconhecido, deixe
  `{{seu número}}` e avise.
- **Prometa informação, nunca resultado.** "O que trava seu emagrecimento" é
  informação. "Perca 5 kg" é promessa e é vedado.
- **Estatística com fonte.** Vigitel, IBGE, POF, Guia Alimentar, artigo. Diga a
  fonte no vídeo ou na legenda.
- **Sem antes/depois de corpo.** Antes/depois de prato, marmita, geladeira ou
  carrinho de mercado, sim. De corpo, composição corporal ou exame, não, nem seu.

## Exemplo

```
/ig-reel a fome da tarde vem do café da manhã fraco em proteína
```

```
GANCHOS  (com nota)
  82  FORTE  #3  Ninguém Te Conta  "Ninguém te conta que a fome das 16h começa no café."
                                   tela: A FOME DAS 16H COMEÇA CEDO
  71  FORTE  #2  Comando Negativo  "Pare de culpar a força de vontade às quatro da tarde."
                                   tela: NÃO É FORÇA DE VONTADE
  54  OK     #16 Pergunta Literal  "Por que eu ataco a geladeira de tarde?"
                                   tela: PERGUNTA DE TODA SEMANA

Gravando o #3: é concreto (16h), lê num relance e é a sua observação de consultório.
```
