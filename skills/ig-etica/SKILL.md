---
name: ig-etica
description: >-
  Revisa roteiro, legenda, carrossel, story, bio, comentário ou DM de
  nutricionista contra o Código de Ética e Conduta do CFN (Res. 856/2026):
  antes/depois, promessa de resultado, exames, promoção e sorteio, marcas e
  suplementos, método único, terrorismo alimentar, sigilo do paciente e
  declaração de uso de IA. Use antes de publicar qualquer conteúdo, e quando
  perguntarem "posso postar isso?", "isso fere o código de ética?", "pode antes
  e depois?", "posso divulgar preço?".
---

# ig-etica

A skill que o pacote original não tinha. Toda outra skill deste pacote chama
esta antes de entregar.

```bash
python3 etica.py texto.txt            # checagem
python3 etica.py texto.txt --ia       # o texto foi feito com ajuda de IA
python3 etica.py texto.txt --json
```

As regras ficam em `regras_cfn.json`, editáveis. Cada achado vem com o nível,
o artigo e como corrigir.

| nível | significa |
| --- | --- |
| **VEDADO** | não publique assim. Reescreva. |
| **ATENÇÃO** | pode ser problema dependendo do contexto. Revise. |
| **LEMBRETE** | provavelmente ok, mas confira a condição. |

## Situação da norma (confira sempre)

- O código novo é a **Resolução CFN nº 856, de 25/04/2026**, publicada no DOU em
  28/04/2026. Ele revoga a Resolução CFN nº 599/2018.
- O prazo para ele entrar em vigor **foi prorrogado** e o CFN abriu consulta
  pública. Até a vigência, vale o código de 2018, que **já vedava** antes/depois
  de pacientes e promoções/sorteios como publicidade.
- Na prática, seguir a versão mais restritiva das duas é o caminho seguro. Esta
  skill segue a de 2026.
- Antes de decisões importantes, confira o texto atual no site do CFN
  (sisnormas.cfn.org.br) ou pergunte ao **CRN-9**.

## O que verificar (texto)

1. **Antes e depois corporal.** Vedado mostrar resultado (imagens, composição
   corporal, exames, gráficos), seu ou de terceiros, mesmo com autorização e
   mesmo gerado por IA (Art. 69 §2º). Exceção: contexto técnico-científico (aula,
   evento, artigo), sem identificar a pessoa. Antes/depois de **prato, marmita,
   rotina ou geladeira** pode.
2. **Promessa ou garantia de resultado.** "Perca X kg em Y dias", "resultado
   garantido", "seque a barriga" (Art. 69 §6º).
3. **Linguagem de milagre.** "Detox", "acelera o metabolismo", "queima
   gordura", "cura": exige rigor técnico e não pode induzir a erro (Arts. 69 e 70).
4. **Promoção e sorteio.** Divulgar preço pode, sem termos que induzam a erro.
   Usar honorários, promoções e sorteios como propaganda, não (Art. 68).
   "Black Friday", "consulta grátis", "de R$ 250 por R$ 150", "só hoje".
5. **Marcas, publi, cupom.** Associar a imagem a marca de alimento,
   suplemento, fitoterápico, utensílio, laboratório ou farmácia é vedado, com
   as exceções do Art. 74 e declaração ostensiva de conflito de interesses.
   Embalagem em conteúdo educativo: mostre mais de uma marca (Art. 72).
6. **Método único.** Apresentar uma abordagem como exclusiva ou obrigatória
   fere o pluralismo técnico-científico (Art. 33).
7. **Terrorismo alimentar.** "Veneno", "nunca mais coma": falta contexto e dose
   (Art. 70).
8. **Paciente identificável.** Nome, idade + cidade, print de conversa, foto:
   sigilo profissional e LGPD.
9. **Depoimento.** Zona cinzenta: sem foto, medida, peso ou exame, e sem
   identificar. Na dúvida, CRN.
10. **Uso de IA.** Materiais feitos com IA devem indicar esse uso (Art. 37).
    Rode com `--ia` sempre que o texto saiu deste pacote.

## O que verificar (imagem e vídeo, à mão)

O script só lê texto. Para o visual, pergunte e confira:

- Há foto ou vídeo de corpo de paciente, bioimpedância, exame ou gráfico de
  evolução? **Vedado.**
- Há imagem, vídeo ou voz **gerado por IA** simulando pessoa real ou resultado
  clínico? **Vedado** (Art. 38 e Art. 69 §4º).
- Aparece marca de produto em destaque, ou a pessoa está vestindo marca durante
  atendimento? Revise (Art. 74).
- A capa do Reel ou do carrossel promete resultado ("-10 kg")? **Vedado.**

## Saída

```
CHECAGEM ÉTICA  ·  legenda do Reel de terça

VEDADO    Promessa ou exibição de resultado   [Art. 69, §2º e §6º]
          trecho: "elimine 3 kg"
          -> "o que costuma ajudar a desinchar depois do fim de semana"
LEMBRETE  Uso de IA não declarado   [Art. 37]
          -> rodapé: "Texto feito com apoio de IA e revisado por mim."

VEREDITO  NÃO PUBLICAR  ->  depois das correções: SEM ALERTAS
```

Sempre proponha a reescrita junto com o alerta. Nunca entregue só o "não pode".

## Diga isso com honestidade

Esta é uma checagem automática por palavras, feita por uma ferramenta, não um
parecer. Dá falso positivo e falso negativo. Não substitui a leitura do código
nem a orientação do CRN, e a responsabilidade pelo que é publicado é da
nutricionista ou do nutricionista (Art. 35).
