# Geração de Dados Sintéticos — Explicação

> **Matéria:** Computação / Programação · **Autoestudo:** 01 · **Data:** 28/04/2026 · **Professor:** Jefferson de Oliveira Silva
>
> Explicação detalhada a partir das duas fontes do [`01-material.md`](01-material.md): o guia "Synthetic Data 101" da Syntheticus e o artigo de Moez Ali (Medium), com o workflow da Gretel.ai.

---

## 1. Contexto geral: o problema que os dados sintéticos resolvem

Imagine que você é chef e quer testar uma receita nova, mas o ingrediente principal é **caríssimo, escasso e regulado** — tipo trufas brancas que só aparecem dois meses por ano e exigem licença pra comprar. Você não vai desperdiçar trufa real treinando garçom ou testando o forno. O que você faz? Cria uma **réplica convincente** — uma "trufa de mentira" que tem o mesmo tamanho, peso e textura — pra ensaiar tudo. Quando o processo estiver redondo, aí sim você usa a trufa de verdade no prato que vai pro cliente.

Dados, hoje, são essa trufa. Para treinar modelos de machine learning, testar software e fazer analytics, você precisa de **muito** dado — e dado real é:
- **Caro e demorado** de coletar, rotular e manter;
- **Limitado** (você só tem o que aconteceu, e talvez falte justamente o caso raro que importa);
- **Enviesado e incompleto** (reflete só quem já está na base);
- E, o mais pesado: **regulado e sensível**. Dado de cliente, prontuário médico, transação bancária — tudo isso cai sob leis como o **GDPR** (a lei europeia de proteção de dados), cuja multa chega a **4% do faturamento global** ou **€20 milhões**, o que for maior. Não é brincadeira.

**Dado sintético (synthetic data)** é a "trufa de mentira": **dado artificial, gerado por algoritmos, que imita estatisticamente os padrões e características do dado real** — sem ser o dado real. Você ensaia tudo com ele e protege (ou nem precisa tocar) o dado verdadeiro.

A grande virada recente: **IA Generativa (Generative AI)**. Gerar dado sintético bom era caro e exigia especialista; com os modelos generativos modernos (os mesmos por trás do ChatGPT), ficou acessível. Tanto que o **EU AI Act** já menciona "dado sintético" explicitamente nos seus artigos.

---

## 2. Conceitos-chave (do básico ao avançado)

### 2.1. O que é (e o que NÃO é) dado sintético

A definição-chave, que se repete nas duas fontes: dado sintético **imita estatisticamente** o dado real — mantém a *estrutura*, as *features* (características/atributos, ou seja, as colunas de uma tabela) e as *distribuições* — **mas não tem correlação um-para-um (one-to-one) com nenhum registro real**. Essa última parte é o ouro: como nenhuma linha do dado sintético corresponde a uma pessoa real, a privacidade fica protegida.

> **Feature** (termo de ML): cada atributo/variável que descreve um dado. Numa tabela de clientes, "idade", "cidade" e "valor da última compra" são features. O dado sintético precisa preservar não só cada feature isolada, mas as *relações entre elas* (ex.: que pessoas mais velhas tendem a gastar mais) — senão vira dado inútil.

### 2.2. Dado sintético vs. dado real vs. dado *dummy*

Três coisas que se confundem:

| | Como é feito | Complexidade | Para quê |
|---|---|---|---|
| **Dado real** | Coletado de sistemas reais (exames, transações, logs) | Alta, mas limitado e arriscado | A verdade do mundo |
| **Dado sintético** | Gerado por algoritmos de ML treinados em dado real | Alta — imita distribuições, inclui valores faltantes/raros | Treinar ML, testar, analytics, privacidade |
| **Dado dummy** | Criado **manualmente**, é só placeholder ("João da Silva", "teste123") | Baixa — não imita distribuição nenhuma | Ver se o sistema funciona, sem realismo estatístico |

A diferença que mais cai em prova: **dummy é "fulano de tal" digitado na mão pra ver se a tela não quebra; sintético é gerado por um modelo que aprendeu como os dados reais se comportam.** Sintético é estatisticamente realista; dummy não.

### 2.3. Como o dado sintético é gerado — os três ramos

Esta é a parte mais técnica e mais importante de Programação. As técnicas se dividem em três famílias:

**A) Modelos baseados em Machine Learning** (os mais poderosos e modernos):

- **GAN — Generative Adversarial Network (Rede Generativa Adversária).** A ideia é genial e vale entender a fundo, porque é a base de quase tudo. São **duas redes neurais competindo** como num jogo de gato e rato:
  - O **Gerador (Generator)** é um *falsificador*: tenta criar dados falsos convincentes.
  - O **Discriminador (Discriminator)** é o *perito da polícia*: recebe dados reais e falsos misturados e tenta dizer qual é qual.
  - Eles treinam um contra o outro: o falsificador melhora pra enganar o perito, o perito melhora pra pegar o falsificador. No fim, o falsificador fica tão bom que produz dado quase indistinguível do real. Usado para séries temporais, imagens e texto.
- **VAE — Variational Auto Encoder (Autoencoder Variacional).** Usa um *encoder* que comprime o dado real numa representação compacta (um "resumo matemático" chamado espaço latente) e depois um *decoder* que reconstrói dados a partir desse resumo — gerando variações novas e realistas.
- **Gaussian Copula (baseado em estatística).** Não usa rede neural; usa matemática estatística pura pra capturar como as variáveis se distribuem e se correlacionam, e amostra dados novos com as propriedades desejadas (ex.: distribuição normal). Bom para dados com distribuição discreta. *(Note a ponte com a Matemática do módulo — distribuições de probabilidade!)*
- **Modelos baseados em Transformer** (ex.: GPT). São os mesmos modelos por trás dos LLMs. Treinados em grandes volumes, capturam padrões e dependências intrincadas e geram dado que se parece com a distribuição original. Fortes em NLP, mas também em imagem, áudio e vídeo.

**B) Modelos baseados em agentes (agent-based).** Em vez de aprender de um dataset, você **simula entidades individuais** seguindo regras, e o dado "emerge" da interação delas:
- **Tráfego:** cada carro é um agente com regras de aceleração/frenagem → gera dados de fluxo de trânsito.
- **Epidemiologia:** cada pessoa é um agente, com probabilidade de contágio → simula a propagação de uma doença.
- **Mercado financeiro:** cada trader é um agente com sua estratégia → gera dados de mercado.

> Guarde "agent-based" e "simulação" — eles são *primos diretos* do **Método de Monte Carlo** e das **Cadeias de Markov**, que aparecem em vários autoestudos do módulo.

**C) Métodos feitos à mão (hand-engineered).** Quando você já entende bem a distribuição dos dados, escreve as regras você mesmo:
- **Rule-based:** regras explícitas ("gere transações com valores e datas aleatórios dentro de um intervalo razoável").
- **Modelos paramétricos:** define a fórmula matemática da distribuição e amostra dela.
- **Random sampling:** sorteia valores do dataset existente.
- **Interpolação linear:** "preenche os buracos" entre pontos de uma série temporal.

### 2.4. Tipos de dado sintético

Por **formato**: texto sintético (NLP), mídia sintética (imagem/vídeo/som) e **tabular sintético** (linhas e colunas — o mais comum em negócios e o foco da maioria dos casos de teste A/B).

Por **quanto do dado é artificial**:
- **Totalmente sintético (fully synthetic):** 100% gerado do zero, sem link com dado real. Máxima privacidade.
- **Parcialmente sintético (partially synthetic):** dado real com as partes sensíveis (nomes, etc.) trocadas por valores sintéticos. Mantém parte das estatísticas reais.
- **Híbrido (hybrid):** mistura registros reais com sintéticos, pareados de forma que não dá pra rastrear o indivíduo.

### 2.5. Como medir a qualidade: fidelidade, utilidade, privacidade

Aqui mora o maior desafio: **como saber se o dado sintético presta?** Não há uma métrica única; avalia-se em **três dimensões** (decore essa tríade, é central):

1. **Fidelidade (fidelity):** quão fiel o sintético é ao real, estatisticamente. Captura bem as distribuições e correlações?
2. **Utilidade (utility):** o dado sintético *serve para a tarefa*? Um modelo treinado nele performa tão bem quanto um treinado no real?
3. **Privacidade (privacy):** ele realmente protege? Dá pra fazer engenharia reversa (reverse-engineering) e re-identificar alguém? Resiste a ataques?

Há uma **tensão** entre essas dimensões: quanto mais fiel ao real, maior o risco de vazar informação real (menos privacidade). O bom dado sintético equilibra os três.

Para modelos generativos como GANs/VAEs, métricas técnicas comuns são o **Inception Score** e o **FID (Fréchet Inception Distance)**, que medem **similaridade com o dado de treino** e **diversidade** do que foi gerado.

### 2.6. Privacidade: PII, GDPR, pseudonimização vs. anonimização

Esse é o "porquê jurídico" de tudo:

- **PII — Personally Identifiable Information (Informação Pessoalmente Identificável):** qualquer dado que identifica alguém — nome, endereço, telefone, email, CPF, dado bancário, médico, biométrico.
- **GDPR:** a lei da UE que obriga proteger PII e exige consentimento. Multa de até 4% do faturamento global / €20 milhões.

Duas técnicas tradicionais de proteção, que **não** são a mesma coisa:
- **Pseudonimização (pseudonymization):** troca o dado sensível por um pseudônimo/token. **Reversível** — com a "chave" você volta ao original. Por isso, sob o GDPR, **dado pseudonimizado ainda conta como dado pessoal**.
- **Anonimização (anonymization):** torna impossível identificar a pessoa, de forma irreversível. Dado anonimizado de verdade sai do escopo do GDPR (Recital 26).

O argumento central do artigo de Moez Ali: **dado sintético bem gerado fica fora do escopo do GDPR** (como dado anonimizado), porque não corresponde a indivíduo nenhum — e ainda resiste melhor a ataques adversariais do que mascaramento/tokenização tradicionais.

---

## 3. Exemplo prático: o workflow da Gretel.ai

O artigo demonstra a anonimização via API da **Gretel.ai** em três passos — uma boa ilustração concreta de como isso vira código:

1. **Classify (Classificar):** uma política varre o dataset e **rotula o que é sensível** (PII, credenciais, padrões via regex). Por baixo usa **NER — Named Entity Recognition (Reconhecimento de Entidades Nomeadas)**, a mesma técnica de NLP que identifica "isto é um nome", "isto é um CPF".
2. **Transform (Transformar):** aplica transformações ao dado rotulado — *date shifting* (deslocar datas), substituição por entidades falsas, etc.
3. **Synthetics (Sintetizar):** gera o dado sintético final, **não relinkável** ao original, escolhendo um modelo conforme o tipo de dado (LSTM para tabular/séries/texto, ACTGAN para tabular complexo, Amplify para volume, DGAN para séries temporais, GPT para texto).

```python
import glob
from gdpr_helpers import Anonymizer

am = Anonymizer(
    project_name="gdpr-workflow",
    run_mode="cloud",
    transforms_config="src/config/transforms_config.yaml",
    synthetics_config="src/config/synthetics_config.yaml",
    endpoint="https://api.gretel.cloud"
)

for dataset_path in glob.glob("data/adventure-works-bike-buying.csv"):
    am.anonymize(dataset_path=dataset_path)
```

A saída são três arquivos: um **relatório** (de qualidade/privacidade), o **CSV transformado** e o **CSV sintético**. Repare como o "Classify → Transform → Synthesize" espelha as três dimensões de qualidade: você identifica o risco, mitiga, e gera algo útil e privado.

> *(Lembrete: o material original foi truncado a partir da análise do relatório de saída — veja a nota no `01-material.md`.)*

---

## 4. Cases reais no mundo (e a ponte com teste A/B)

- **Waymo / carros autônomos:** treinar um carro a reconhecer um pedestre atravessando no escuro com chuva exige milhões de exemplos desse cenário raro e perigoso. Coletar isso no mundo real é inviável (e antiético). A Waymo e a NVIDIA geram **dados sintéticos de cenários extremos** (edge cases) para treinar a IA com segurança — exatamente o ponto da fonte sobre "simular eventos raros".
- **J.P. Morgan e American Express (finanças):** usam dado sintético para treinar modelos de **detecção de fraude** e **anti-lavagem de dinheiro (AML)** sem expor transações reais de clientes — e para gerar mais exemplos de fraude (que são raros) e reduzir falsos positivos.
- **Saúde:** datasets sintéticos de prontuários permitem pesquisa e treino de modelos sem violar a confidencialidade do paciente (e sem o pesadelo regulatório).

**A conexão direta com teste A/B** (o tema do módulo) — e por que isso é um autoestudo de *Programação*:

1. **Simular experimentos antes de rodar.** Antes de gastar tráfego real num teste A/B, você pode gerar **usuários sintéticos** com comportamento realista e simular o experimento — para validar seu pipeline de experimentação, estimar quanto tempo o teste vai durar e fazer **power analysis** (cálculo de tamanho de amostra) sem queimar usuários de verdade.
2. **Testar o pipeline de análise.** O código que calcula significância, *lift* e p-value de um teste A/B precisa ser testado — e dado sintético dá o cenário controlado ideal (você *sabe* a "verdade", porque você a definiu ao gerar os dados, e checa se sua análise a recupera).
3. **Cenários raros e contrafactuais.** Quer saber como seu teste se comportaria com uma queda de conversão de um grupo específico? Gere esse cenário sinteticamente.

Em resumo: **dado sintético é o "laboratório seguro" onde você ensaia a experimentação A/B** antes de ela tocar usuários reais e dados sensíveis.

---

## 5. Conexão com o módulo

Olhando o [README](../../README.md) e o cronograma, este autoestudo é uma **base técnica** que se conecta a vários outros:

- **Computação — [Autoestudo 06: Fundamentos de Programação de Testes A/B](../../computacao/autoestudo-06-fundamentos-de-programacao-de-testes-ab/02-explicacao.md).** É o par natural: dado sintético é o ambiente seguro pra testar e validar pipelines de experimentação A/B.
- **UX — [Autoestudo 01: Métodos Mistos](../../ux/autoestudo-01-metodos-mistos-de-exploracao-e-pesquisa/02-explicacao.md).** Lá vimos que dado **quantitativo** (analytics, A/B) precisa de qualidade e representatividade. Dado sintético ataca justamente o **viés** e a **incompletude** que comprometem a parte quantitativa da pesquisa.
- **À frente no cronograma:** este é o primeiro de uma trilha de Programação que inclui **Avaliação de Dados Sintéticos** (Prog-03, o "como medir qualidade" aprofundado) e os autoestudos de **Monte Carlo** e **Cadeias de Markov** (Prog-04, 05, 07, 08) — os modelos *agent-based* e de simulação que vimos aqui são exatamente essa família. Na Matemática, **Distribuições de Probabilidade** é o alicerce do Gaussian Copula e da geração estatística.

---

## 6. Resumo estruturado

- **Dado sintético** = dado artificial gerado por algoritmos que **imita estatisticamente** o real, **sem corresponder a registros reais** (logo, protege privacidade).
- **Resolve:** custo, escassez, viés, incompletude e — principalmente — **risco regulatório** (GDPR e suas multas).
- **≠ dado dummy:** dummy é placeholder manual sem realismo estatístico; sintético é gerado por modelo treinado no real.
- **3 ramos de geração:** (A) **ML** — GAN (gerador vs. discriminador), VAE, Gaussian Copula, Transformers; (B) **agent-based** — simular entidades (tráfego, epidemia, mercado); (C) **hand-engineered** — regras, paramétrico, sampling, interpolação.
- **3 tipos por composição:** totalmente / parcialmente / híbrido sintético.
- **3 dimensões de qualidade:** **fidelidade** (parece real?), **utilidade** (serve à tarefa?), **privacidade** (protege?). Há tensão entre elas.
- **Privacidade:** PII, GDPR; **pseudonimização** (reversível, ainda é dado pessoal) ≠ **anonimização** (irreversível, sai do GDPR). Sintético bem-feito ≈ anonimizado.
- **Workflow Gretel.ai:** Classify (NER) → Transform → Synthetics.
- **Ponte com A/B:** simular experimentos, testar pipelines de análise e modelar cenários raros **antes** de tocar usuários e dados reais.

---

## 7. Auto-reflexão (pra pensar sozinha)

1. Uma startup quer treinar um modelo de detecção de fraude, mas só tem 50 exemplos reais de fraude (porque fraude é rara). Qual ramo de geração de dado sintético você usaria pra criar mais exemplos, e qual das 3 dimensões de qualidade seria a mais crítica de garantir aqui?
2. Sua empresa quer compartilhar um dataset de clientes com uma consultoria externa. Por que **pseudonimizar** não seria suficiente sob o GDPR, e como o dado **totalmente sintético** resolveria o problema?
3. Antes de rodar um teste A/B caro com tráfego real, como você usaria dado sintético pra ter mais confiança de que seu pipeline de cálculo de significância (p-value, lift) está correto?
