# Instagram Nutri Skill (PT-BR)

Catorze skills do Claude para o Instagram de **nutricionistas**, em português.
Grátis, licença MIT, sem cadastro, sem chave de API, nada para conectar ao
Instagram.

É uma adaptação do [instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)
de Jake Schincariol (MIT), com três mudanças de fundo:

1. **Tudo em português do Brasil:** instruções, fórmulas de gancho, léxico de
   clichês, mensagens dos scripts, ritmo de fala.
2. **Foco em nutrição:** exemplos, temas, públicos e armadilhas de quem atende
   em consultório e online.
3. **Uma skill nova, `/ig-etica`:** checa o conteúdo contra o Código de Ética e
   Conduta do Nutricionista (Resolução CFN nº 856/2026) antes de qualquer coisa
   ser publicada. Todas as outras skills passam por ela.

**Nada é publicado sem você.** As skills escrevem. Você revisa e posta.

## Instalar

Cole isto no Claude Code:

```
https://github.com/mpjbiologo/instagram-nutri-skillPTBR

Instale estas skills e confirme que /ig-reel funciona.
```

Ou como plugin:

```
/plugin marketplace add mpjbiologo/instagram-nutri-skillPTBR
/plugin install instagram-nutri
```

Ou à mão:

```bash
git clone https://github.com/mpjbiologo/instagram-nutri-skillPTBR.git
cp -r instagram-nutri-skillPTBR/skills/ig-* ~/.claude/skills/
```

Sem Claude Code? Cole qualquer `SKILL.md` no começo de uma conversa no app do
Claude e ele funciona como um modo. Você perde os scripts Python (as notas de
gancho, o mapa de tempos, o humanizador e o checador ético automático), mas as
instruções funcionam.

Depois gaste dez minutos no `templates/voz.md`: copie para
`~/.claude/instagram/voz.md` e preencha, ou mande três Reels seus para o Claude
e diga "escreve meu voz.md a partir destes". Todas as skills leem esse arquivo.

## As catorze

| comando | o que faz |
| --- | --- |
| `/ig-reel` | Uma ideia vira Reel. Três ganchos de [26 fórmulas](skills/ig-reel/ganchos.json), com nota, roteiro, texto da tela e mapa de tempos. |
| `/ig-legenda` | A legenda, revisada. Mostra os 125 caracteres que o feed exibe antes do "mais". |
| `/ig-carrossel` | Carrossel: a capa que faz arrastar, o texto de cada slide e os arquivos 1080x1350. |
| `/ig-stories` | A sequência de stories do dia, qual figurinha para quê, e o funil de DM que começa quando a pessoa responde. |
| `/ig-perfil` | Nota do perfil numa [rubrica de 13 itens](skills/ig-perfil/rubrica.json), de 0 a 100, incluindo conformidade ética. Reescreve na ordem de correção. |
| `/ig-plano` | A semana: o que postar, formato, horário e 10 contas para interagir. |
| `/ig-viral` | Pesquisa o que está funcionando no nicho, ranqueia pelo múltiplo sobre a mediana de cada conta, separa o que fere o código. |
| `/ig-humano` | Tira a cara de IA do texto em português. Dois scripts que rodam de verdade. |
| `/ig-etica` | **Nova.** Checagem do Código de Ética do CFN: antes/depois, promessa de resultado, promoção, marcas, sigilo, IA. |
| `/ig-comentario` | Comentários em posts de outras pessoas. Nove tipos. Nunca "Amei! 🔥". |
| `/ig-resposta` | Os comentários do seu post: separa palavra-chave, possível paciente, conteúdo, pergunta, caso clínico, apoio e ruído. |
| `/ig-dm` | Entrega da palavra-chave, primeira mensagem, proposta de parceria e os dois acompanhamentos. |
| `/ig-reaproveitar` | Um ebook, aula, live ou artigo vira uma semana de Reels e carrosséis. |
| `/ig-auditoria` | Análise do que já foi postado. Ranqueia por múltiplo e envios por alcance, não por views. |

## Os scripts que rodam

Sem dependências, sem internet, nada é enviado. Rodam no seu computador, no seu texto.

```bash
# ganchos e tempo
python3 skills/ig-reel/nota_gancho.py ganchos.txt
python3 skills/ig-reel/tempos.py roteiro.txt --alvo 30

# legenda
python3 skills/ig-legenda/legenda.py legenda.txt --busca "nutricionista em Itaúna"

# humanizador
python3 skills/ig-humano/humanizar.py rascunho.txt -o limpo.txt --relatorio
python3 skills/ig-humano/detectar.py rascunho.txt limpo.txt

# ética
python3 skills/ig-etica/etica.py legenda.txt --ia

# referências
python3 skills/ig-viral/referencias.py coletados.tsv --saida ~/.claude/instagram/referencias.md
```

Exemplo de nota de gancho:

```
RANKING DE GANCHOS
==============================================================================
->  83.2 FORTE  Pare de contar caloria da salada. Olhe primeiro o molho.
    62.2 OK     Ninguém te conta que a fome das quatro da tarde começa no s...
        mais fraco: TAMANHO (33)
    35.6 FRACO  Perca 5 kg em 10 dias com esse chá
        eliminatório: CFN: promessa ou exibição de resultado (kg/cm em X dias).
     0.0 FRACO  Oi gente, hoje eu vou falar sobre alimentação saudável
        eliminatório: Saudação. Ninguém abriu o feed para ser cumprimentado.
```

Exemplo de checagem ética:

```
  VEDADO    Antes e depois / evolução corporal   [Art. 69, §2º]
  VEDADO    Promessa ou exibição de resultado    [Art. 69, §2º e §6º]
  VEDADO    Promoção, sorteio ou desconto        [Art. 68, III]
  ATENÇÃO   Paciente possivelmente identificável
  LEMBRETE  Uso de IA não declarado              [Art. 37]
  VEREDITO  NÃO PUBLICAR
```

## Sobre o Código de Ética (leia)

- As regras de `/ig-etica` seguem a **Resolução CFN nº 856/2026**, publicada em
  28/04/2026, que substitui a Resolução 599/2018. O prazo para ela entrar em
  vigor foi prorrogado e o CFN abriu consulta pública. Até lá vale o código de
  2018, que **já vedava** antes/depois de pacientes e promoções/sorteios.
- **Confira a situação atual** no site do CFN ou com seu CRN antes de decisões
  importantes. Normas mudam; quando o código mudar, edite
  `skills/ig-etica/regras_cfn.json`.
- O checador é **heurístico** (busca por palavras). Dá falso positivo e falso
  negativo, não analisa imagem nem vídeo, e **não substitui** o código nem o CRN.
  A responsabilidade pelo que é publicado é do profissional.
- Art. 37: materiais feitos com IA devem indicar esse uso. O humanizador deixa o
  texto com a sua voz; **não** serve para esconder que houve IA. Mantenha a
  linha de declaração no rodapé.

## Honestidade sobre os limites

- **Estas skills não postam no Instagram.** Automatizar postagem, comentário,
  seguir ou DM por automação de navegador ou ferramenta de terceiros viola os
  Termos de Uso do Instagram e bloqueia contas. Toda skill termina num bloco
  pronto para copiar, e você posta. A única exceção é a resposta automática por
  palavra-chave, que o Instagram oferece oficialmente para contas profissionais.
- **A nota de gancho não prevê viral.** No original em inglês, o avaliador
  separou bem gancho real de gancho ruim (AUC 0,83) mas quase não separou acertos
  de erros do mesmo criador (AUC 0,56, cara ou coroa é 0,50). Esta versão em
  português **ainda não foi validada** em ganchos reais em PT-BR. Use para matar
  ganchos fracos antes de gravar, e confie no seu gráfico de retenção.
- **O detector de IA é local.** Não é GPTZero, Originality nem Turnitin, e
  ninguém pode prometer texto "indetectável".
- **Nada é inventado.** Nenhum número, paciente ou resultado vai no seu nome. Se
  um rascunho precisa de um número que você não deu, volta com `{{seu número}}`.
- **Números de plataforma envelhecem.** O limite de hashtags caiu de 30 para 5
  em 18/12/2025. Se algo aqui contradiz o Instagram de hoje, o Instagram está certo.

## Arquivos

```
skills/ig-reel/ganchos.json        26 fórmulas de gancho em PT-BR, com exemplo de nutrição,
                                   alerta do CFN e regex de classificação
skills/ig-reel/nota_gancho.py      painel de cinco propriedades do gancho + eliminatórios CFN
skills/ig-reel/tempos.py           roteiro -> mapa de tempos (150 ppm padrão)
skills/ig-legenda/legenda.py       prévia do corte do feed e revisão da legenda
skills/ig-humano/cliches.json      léxico: ~180 clichês, 18 classes invisíveis, 18 estruturas
skills/ig-humano/humanizar.py      as três passadas de limpeza
skills/ig-humano/detectar.py       o painel de cinco checagens
skills/ig-etica/regras_cfn.json    13 regras do Código de Ética, com artigo e correção
skills/ig-etica/etica.py           o checador ético
skills/ig-viral/referencias.py     ranking por múltiplo e classificação de fórmula
skills/ig-perfil/rubrica.json      a rubrica de 100 pontos para perfil de nutricionista
templates/voz.md                   seu perfil de voz. Preencha primeiro.
templates/voz-exemplo-mpjnutri.md  exemplo parcialmente preenchido
```

## Créditos

Adaptação para português e nutrição: Marcos de Paula Júnior, nutricionista
(CRN-9 35526), [@mpjnutri](https://instagram.com/mpjnutri).

Original em inglês: Jake Schincariol,
[instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) (MIT).

Adaptação feita com apoio de IA (Claude) e revisada pelo autor.

## Licença

MIT. Veja [LICENSE](LICENSE).
