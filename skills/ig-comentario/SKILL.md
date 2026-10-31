---
name: ig-comentario
description: >-
  Escreve comentários em posts e Reels de outras pessoas que soam como um
  nutricionista com opinião, não como robô. Use quando colarem um post ou Reel
  pedindo comentário, "comenta isso", "interage com esse post", "o que eu falo
  aqui", ou quiserem um lote para a rodada diária de interação.
---

# ig-comentario

Comentar é o melhor investimento de vinte minutos no Instagram, e o mais fácil
de fazer mal. Um comentário no topo de um Reel com 40 mil views é visto por mais
gente que a maioria dos posts da própria conta, e é o único lugar onde um
estranho vai direto para o seu perfil com um toque.

Comentário genérico é pior que nenhum. Marca a conta como "grupo de
engajamento" justamente para a pessoa cuja opinião importava: o criador.

## Entrada

A pessoa cola o texto do post ou Reel, ou um print, com o @. Se mandar um link
que você não consegue abrir, peça para colar. Não use navegador para varrer o
feed e não poste nada.

## Os nove tipos de comentário

Escolha pelo que o post realmente é. Nunca vá no tipo 1 por padrão.

| # | tipo | quando | formato |
| --- | --- | --- | --- |
| 1 | **Acrescentar um dado** | o post faz uma afirmação que você sustenta com número e fonte | "O Vigitel mostra..." |
| 2 | **O caso que faltou** | o post está certo mas incompleto | "Vale até {condição}." |
| 3 | **Discordar com respeito** | você acha que está errado | concorde primeiro no que der, depois a divergência |
| 4 | **Ampliar uma frase** | uma frase do post é a boa | cite e construa em cima |
| 5 | **A pergunta de verdade** | o post pulou a parte difícil | uma pergunta, específica |
| 6 | **A experiência** | você vê isso no consultório | o que você observa, duas frases, sem paciente identificável |
| 7 | **A correção** | há um erro técnico | esteja certo, seja breve, gentil e seguro, cite fonte |
| 8 | **Outra leitura** | fatos certos, enquadramento errado | "Outro jeito de ver:" |
| 9 | **A frase curta** | o post não precisa de nada, você quer presença | menos de 10 palavras, engraçada ou verdadeira |

## Regras

- **Uma a três frases.** Parágrafo é recolhido atrás do "mais".
- **Nunca abra com** "Amei!", "Perfeito!", "Que conteúdo!", "Isso 👏", "Precisava
  ver isso hoje" ou o nome do criador com exclamação. São invisíveis.
- **Nada de comentário só de emoji**, nem emoji como primeiro caractere.
- **Não repita o Reel.** Todo mundo acabou de ver.
- **Uma ideia.** Dois pontos parecem sequestro do post.
- **Diga a coisa específica.** Se o comentário serve em qualquer post do tema,
  é ruído.
- **Nunca venda.** Nem consulta, nem link, nem "vem ver meu perfil".
- **Respeito com colegas.** Discordar de conteúdo, nunca desqualificar o
  profissional. Comentário depreciativo sobre colega é infração ética.
- **Correção de leigo ou influenciador:** sem tom de superioridade. A correção
  que educa ganha seguidores; a que humilha ganha bloqueio.
- **Cedo importa.** Comentário na primeira hora de um Reel que viraliza vai junto.

## Saída

Dê **duas opções de tipos diferentes**, rotuladas, e uma linha sobre qual você
postaria e por quê. Passe as duas por `/ig-humano` (comentário é curto, então
travessão e clichê aparecem mais) e `/ig-etica`.

```
OPÇÕES DE COMENTÁRIO  (no Reel do @conta sobre jejum)

[6 · Experiência]
No consultório o que mais vejo é gente que faz o jejum e compensa tudo no
jantar. A janela fecha, mas o total do dia não muda.

[2 · O caso que faltou]
Vale lembrar que para quem tem diabetes e usa medicação, jejum sem
acompanhamento pode dar hipoglicemia.

Poste o segundo. Acrescenta segurança e ninguém mais disse.
```

## Modo lote

Para a rodada de interação, peça os 5 a 10 posts colados numa mensagem só,
devolva um comentário para cada num bloco, e mantenha uma nota em
`~/.claude/instagram/historico.md` de quem já recebeu comentário na semana.
Comentar nas mesmas três contas todo dia fica visível.

## Nunca

Não poste sozinho, não automatize comentários e não use navegador para
publicar pela pessoa. Interação automatizada viola os Termos de Uso do
Instagram e bloqueia contas. Esta skill escreve o comentário. A pessoa posta.
