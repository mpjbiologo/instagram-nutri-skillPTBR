---
name: ig-viral
description: >-
  Encontra os Reels que estão funcionando agora no nicho de nutrição, ranqueia
  pelo quanto cada um superou a própria conta, dá nome à fórmula de gancho e
  transforma isso num arquivo de referências para gravar, filtrando o que fere
  o Código de Ética. Use quando pedirem "acha vídeos virais", "o que está
  funcionando agora", "o que outros nutricionistas estão postando", "analisa
  esse perfil", "monta minhas referências", ou quando perguntarem o que gravar
  e não houver evidência para responder.
---

# ig-viral

A skill de pesquisa. As outras escrevem; esta vai olhar. Rode uma vez por mês,
não todo dia. Fórmula dura uma estação.

```bash
python3 referencias.py coletados.tsv --saida ~/.claude/instagram/referencias.md
```

## A ideia que faz isso valer a pena

**View bruta não é evidência.** Conta de dois milhões fazendo 400 mil views teve
uma terça fraca. Conta de quatro mil fazendo 400 mil achou alguma coisa, e essa
coisa é copiável.

Então tudo aqui ranqueia pelo **múltiplo**: views divididas pela mediana recente
da própria conta. Acima de 3x é sinal. Abaixo de 1,5x é o dia normal da conta e
não ensina nada, por maior que o número pareça.

Colete contas **até umas 10 vezes o tamanho da pessoa**. Uma fórmula que funciona
com 2 milhões de seguidores muitas vezes funciona porque são 2 milhões.

## Passo 1: escolher as contas

Peça 6 a 12 contas, ou proponha e peça aprovação:

- **4 diretas:** nutricionistas do mesmo nicho (emagrecimento, saúde
  metabólica), um pouco à frente.
- **4 vizinhas:** outro nicho, mesmo público. Educadores físicos, médicos,
  receitas saudáveis, finanças pessoais para o mesmo público. É de onde os
  formatos vêm antes de chegar no nicho.
- **2 a 4 grandes:** contas muito maiores, só para formato, nunca para
  frequência ou tom.

Peça também para a pessoa abrir a **coleção de Salvos** dela. É o acervo mais
rápido e relevante que existe, já filtrado pelo gosto dela.

## Passo 2: ir olhar

Use a ferramenta de navegação que esta sessão tiver (navegador do app, extensão
no Chrome da pessoa, uso do computador) ou peça para a pessoa colar os dados.
Não há API para isso e nem precisa: o volume é pequeno o bastante para ler.

**Regras inegociáveis:**

- **Nunca faça login no Instagram pela pessoa e nunca peça senha.** Se a página
  exigir login, quem está logada é ela. Conduza o navegador com ela presente,
  ou peça para colar.
- **Isso é leitura, não raspagem.** Dez contas, uma dúzia de Reels cada, em
  ritmo humano. Coleta automatizada em volume viola os Termos de Uso do
  Instagram e bloqueia contas. Não construa crawler, não use serviço de
  raspagem, não deixe rodando em segundo plano.
- **Copie a fórmula, nunca o vídeo.** O formato do gancho, a estrutura, a
  duração, o ritmo dos cortes. Não o roteiro, a voz ou a edição de ninguém.
  Atribua cada linha à conta de onde veio.
- **Viralizar não torna ético.** Muito conteúdo de nutrição que viraliza usa
  antes/depois, promessa de kg ou suplemento com cupom. O script marca esses
  ganchos com [CFN!]. Eles entram na análise, mas nunca viram sugestão.

**O que anotar por Reel**, nas palavras do criador:

| campo | observação |
| --- | --- |
| conta | @ |
| seguidores | do perfil |
| mediana | olhe os últimos 12 Reels e pegue o número do meio |
| views | deste Reel |
| gancho | a primeira frase, falada ou na tela, literal, com o português que veio |
| tela | a primeira cartela, se diferente |
| duração | segundos |
| cta | o que pediram no final |

A mediana é a coluna importante. Sem ela, você volta a ranquear por número de
seguidores, que é justamente o que esta skill existe para evitar.

## Passo 3: ranquear

Preencha um arquivo separado por TAB com cabeçalho e rode o script:

```
conta	seguidores	mediana	views	gancho
@alguem	48000	11000	412000	ninguém te conta que a fome da tarde começa no café
```

```bash
python3 referencias.py coletados.tsv --saida ~/.claude/instagram/referencias.md
```

Ele calcula o múltiplo, dá nome à fórmula usando as mesmas 26 de `/ig-reel`,
dá nota a cada gancho com `nota_gancho.py` e mostra o que separa o terço de
cima do terço de baixo.

## Passo 4: dizer o que significa, com cuidado

Relate três coisas e só:

1. **Quais fórmulas aparecem demais** no terço de cima, com contagem. Duas
   fórmulas aparecendo quatro vezes cada em seis contas é achado. Uma
   aparecendo duas vezes não é.
2. **O que o topo tem em comum na estrutura** que a base não tem: tamanho do
   gancho, se a entrega é visual, se o primeiro quadro se mexe, onde fica o pedido.
3. **Os sem classificação.** Todo gancho que o classificador não reconheceu é
   ruído ou uma fórmula que ainda não está em `ganchos.json`. Leia à mão. É a
   coluna mais valiosa.

Depois diga o tamanho da amostra e a confiança em palavras simples. Quarenta
Reels em seis contas sustentam uma afirmação. Doze não, e dizer isso é a
diferença entre pesquisa e horóscopo.

## Passo 5: transformar em algo para gravar

Para as três melhores fórmulas, escreva **a versão da pessoa**: a observação de
consultório dela, o dado dela, no formato que está funcionando, já dentro das
regras do CFN. Entregue cada uma para `/ig-reel` com a fórmula escolhida.

Nunca devolva "faz um Reel igual a esse". Devolva uma frase de gancho que ela
pode falar amanhã.

## Saída

```
REFERÊNCIAS  ·  38 reels  ·  7 contas  ·  base: mediana da conta

ACIMA DE 3x
  38.4x  nota 82  #3  Ninguém Te Conta    @conta_a   412.000  (mediana 10.700)
  11.2x  nota 79  #16 Pergunta Literal    @conta_c   180.000  (mediana 16.100)
  ...

O QUE APARECE DEMAIS
  #16 Pergunta Literal   x5 no topo, 0 na base
  #20 Permissão          x4
  tamanho mediano        8 palavras no topo, 17 na base

FORA DO JOGO (CFN)
  3 do topo usam antes/depois ou kg. Não sugeridos.

SUA VERSÃO
  #16  "Posso comer fruta à noite? Eu ouço isso toda semana no consultório."
  ...
```

Grave o arquivo em `~/.claude/instagram/referencias.md`. `/ig-reel` e
`/ig-plano` leem esse arquivo, e esse é o ponto: depois de rodar uma vez, o
resto do pacote trabalha com a evidência da própria pessoa.

Nada é postado, seguido, curtido ou enviado por esta skill. Ela lê.
