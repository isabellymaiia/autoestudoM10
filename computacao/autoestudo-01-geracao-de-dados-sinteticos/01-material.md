# Geração de Dados Sintéticos — Material

> **Matéria:** Computação / Programação · **Autoestudo:** 01 · **Data:** 28/04/2026 · **Professor:** Jefferson de Oliveira Silva (Eixo COM)
>
> Compilação de duas fontes. O conteúdo foi limpo de elementos de navegação/rodapé dos sites, preservando o texto substantivo. **Nota:** a segunda fonte (artigo do Medium) chegou **truncada** no envio, cortada no meio da implementação em Python com a Gretel.ai — o trecho final de código está incompleto aqui.

---

## Fonte 1 — Syntheticus: *Synthetic Data 101: What is it, how it works, and what it's used for*

> Guia "Dados Sintéticos 101" da Syntheticus.

Coletar, rotular, treinar e manter datasets para aplicações de machine learning e inteligência artificial pode ser caro e demorado. Apesar do vasto volume de dados produzidos, muito ainda é inacessível para projetos de data science e analytics. Diretrizes estritas de privacidade, segurança e compliance tornam o uso de datasets do mundo real ainda mais desafiador.

Como resultado, organizações estão recorrendo a **dados sintéticos (synthetic data)** — dados gerados artificialmente, criados com algoritmos avançados de machine learning, como alternativa eficaz e acessível a dados reais sensíveis e arriscados. Com os avanços em **IA Generativa (Generative AI)**, gerar dados sintéticos ficou mais fácil e acessível.

### O que é dado sintético?

Resposta curta: dado sintético é, como o nome sugere, **dado artificial gerado para imitar dados reais**. Tipicamente é gerado com técnicas sofisticadas de IA Generativa, criando dados similares em **estrutura, features (características/atributos) e características** aos dados de aplicações do mundo real.

A importância foi reforçada pelo novo **EU AI Act** (proposto em maio de 2023), que menciona explicitamente dados 'sintéticos' nos Artigos 10 e 54. Como o dado sintético não tem correlação um-para-um (one-to-one) com o dado real, ele é usado para **treinar modelos de ML, testar aplicações de software e preencher lacunas em datasets**. É vital para finanças, saúde e seguros, onde privacidade e segurança limitam o acesso a dados reais.

### Como o dado sintético é gerado?

É criado programaticamente, com técnicas em três ramos principais: **modelos baseados em machine learning, modelos baseados em agentes (agent-based), e métodos feitos à mão (hand-engineered)**.

**Modelos baseados em ML:**

- **GAN (Generative Adversarial Network / Rede Generativa Adversária):** sistema de rede neural em duas partes — uma parte gera novos dados sintéticos e a outra avalia e classifica a qualidade desses dados. Muito usado para gerar séries temporais, imagens e texto sintéticos.
- **VAE (Variational Auto Encoders / Autoencoders Variacionais):** usa um sistema adversário com um encoder adicional para gerar dados altamente realistas e similares em estrutura, features e características aos dados reais.
- **Gaussian Copula (baseado em estatística):** usa metodologia estatística para gerar dados realistas com propriedades desejadas (ex.: distribuição normal). Comum para dados com distribuição discreta, como a probabilidade de certos eventos.
- **Modelos baseados em Transformer:** como o GPT (Generative Pre-trained Transformer) da OpenAI, são excelentes em capturar padrões e dependências intrincadas. Treinando em grandes datasets, aprendem a estrutura subjacente e geram dados que se parecem muito com a distribuição original. Muito aplicados em NLP (processamento de linguagem natural), mas também em visão computacional, reconhecimento de fala, síntese de imagem, geração de música e vídeo.

**Modelos baseados em agentes (agent-based):** simulam o comportamento e as interações de agentes (entidades) individuais num sistema. Úteis quando o comportamento de entidades individuais contribui para o padrão geral observado:

- **Simulação de tráfego:** cada veículo é um agente com regras de aceleração, desaceleração e troca de faixa; gera dados sintéticos de fluxo de tráfego.
- **Modelos epidemiológicos:** cada pessoa é um agente; as interações (taxas de contato, probabilidade de infecção) determinam a transmissão da doença. Ajuda a estudar intervenções e prever surtos.
- **Simulação de mercado:** cada trader é um agente com estratégias e preferências de risco diferentes; gera dados de mercado financeiro para testar algoritmos de trading e gestão de risco.

**Métodos feitos à mão (hand-engineered):** projetar regras e algoritmos. Usados quando a distribuição dos dados é bem compreendida:

- **Geração baseada em regras (rule-based):** dados criados a partir de regras e condições predefinidas. Ex.: "crie novas transações para cada cliente com valores e datas de compra aleatórios, garantindo que as datas estejam num intervalo razoável dos dados originais."
- **Modelos paramétricos:** representações matemáticas da distribuição; os dados são gerados amostrando do modelo.
- **Amostragem aleatória (random sampling):** gera dados selecionando aleatoriamente dos dados existentes (ex.: idades).
- **Interpolação linear:** gera pontos sintéticos entre pontos existentes de uma série temporal, suavizando-a.

Cada método tem benefícios, e alguns podem ser combinados. A melhor abordagem depende das necessidades da organização.

### Tipos de dado sintético

Tipos amplos por **formato**:
- **Texto sintético:** usado em NLP e tarefas de texto quando o dado real é indisponível ou sensível.
- **Mídia sintética:** vídeo, imagem, som — para detecção e reconhecimento de objetos.
- **Dado tabular sintético:** estruturado em linhas e colunas (tabelas de banco de dados relacional); preenche lacunas/valores faltantes.

E também por **quantidade de dado sintético no dataset**:
- **Totalmente sintético (fully synthetic):** inteiramente artificial, sem equivalente no mundo real. Gerado do zero por um algoritmo que identifica as propriedades estatísticas e padrões e cria um dataset novo que os imita. Sem link identificável com dados reais.
- **Parcialmente sintético (partially synthetic):** contém info real que foi manipulada para ficar inutilizável num cenário real. Substitui dados sensíveis (ex.: nomes de clientes) por identificadores genéricos não rastreáveis. Mantém algumas propriedades estatísticas enquanto protege a privacidade. Técnicas: imputação múltipla (multiple imputation) e técnicas baseadas em modelo.
- **Híbrido (hybrid):** combina dado real e totalmente sintético. Pareia registros reais aleatórios com registros sintéticos, tornando quase impossível rastrear até o indivíduo original. Permite escalar datasets e criar analytics avançado protegendo contra ameaças.

### Como determinar a qualidade do dado sintético?

Um dos principais desafios. Fatores: tamanho do dataset, número de variáveis, e quão bem imita o dado real. Considerações-chave: aleatoriedade da amostra, quão bem captura a distribuição estatística do dado real, e se inclui valores faltantes ou errôneos.

Modelos generativos como GANs ou VAEs podem ser avaliados com métricas como **Inception Score** ou **FID score**, que comparam a qualidade do dado sintético contra o real. Esses aspectos geralmente consideram **similaridade com o dado de treino** e **diversidade dentro de si**.

Outro ponto: quão bem protege privacidade e segurança. Diferentes técnicas têm diferentes níveis de risco de revelar informação sensível. Avaliar: se está bem anonimizado e de-identificado, se poderia ser revertido (reverse-engineered) para revelar identidades, probabilidade de vazamentos e robustez contra ataques.

O dado sintético é medido contra **três dimensões-chave: fidelidade (fidelity), utilidade (utility) e privacidade (privacy)**. No fim, a qualidade depende do caso de uso específico — não há um único padrão ou métrica para todas as aplicações (a qualidade de imagens sintéticas, por exemplo, é muito subjetiva).

### Dado sintético vs. dado real

Dado real é coletado por sistemas reais (exames médicos, transações bancárias, logs de servidor). Dado sintético é gerado por algoritmos de ML. Diferenças-chave:
- Dado real é tipicamente limitado em tamanho, difícil de acessar e pode não refletir toda a gama de valores/comportamentos possíveis.
- Dado sintético é mais flexível, fácil de acessar, gerado em grande quantidade com maior precisão para requisitos específicos.
- Dado sintético é **compatível com privacidade** (privacy compliant): não contém PII (informação pessoalmente identificável) e não pode ser facilmente revertido para extrair info sensível.

### Dado sintético vs. dado dummy

Dado **dummy** é dado falso/mock que age como placeholder de dados reais em desenvolvimento e testes. Serve para o desenvolvedor entender a funcionalidade, a lógica e o fluxo de um sistema antes de o dado real estar disponível. Diferenças: o sintético é gerado por algoritmos de ML baseados em datasets reais, enquanto o dummy é tipicamente criado manualmente. O sintético é muito mais complexo e costuma gerar datasets realistas com valores faltantes ou corrompidos.

### Benefícios de usar dado sintético

Permite usar dados complexos sem o risco e as preocupações de privacidade do dado real. É gerado mais rápido e com mais precisão. Outros benefícios:
- Maior controle sobre qualidade e formato do dataset.
- Custos menores de gestão e análise de dados.
- Melhor desempenho em algoritmos de ML (datasets de maior qualidade).
- Tempo de entrega mais rápido para fluxos de desenvolvimento.
- Maior privacidade e segurança para fontes sensíveis (saúde, financeiro).

### Casos de uso do dado sintético

Gira em torno de: desenvolvimento/teste de produto, machine learning, análise de dados, e privacidade/segurança.

- **Analytics avançado:** provedores de nuvem (CSPs) oferecem ferramentas de analytics (ex.: Google Analytics), mas as organizações precisam cumprir regulações que limitam o acesso. Dado sintético com privacidade preservada permite extrair valor sem quebrar o isolamento entre os dados e o CSP.
- **ML / IA:** data scientists sofrem com datasets limitados ou de baixa qualidade; o dado sintético preenche lacunas e melhora a precisão de modelagem preditiva, forecasting e gestão de risco financeiro.
- **Desenvolvimento e teste de software:** ajuda a entender funcionalidade, lógica e fluxo antes do dado real existir — testar/debugar features, otimizar performance, melhorar UX, criar test cases realistas.
- **Cibersegurança:** treina algoritmos cumprindo regulações; ajuda times de segurança a detectar, prevenir e responder a fraudes, ransomware e outras ameaças, retendo as propriedades estatísticas do dado real sem características identificáveis.

### Casos de uso por indústria

**Seguros (insurance):**
- **Reinventando a avaliação de risco (risk assessment):** dado sintético é moldado para incluir vários fatores de risco e variáveis demográficas; permite prever risco com mais precisão e simular **eventos raros/extremos** que ocorrem pouco mas têm grande impacto.
- **Reformulando o processamento de sinistros (claims processing):** cria datasets realistas e diversos representando vários tipos de sinistro; acelera o timeline.
- **Detectando fraude:** cria cenários de fraude realistas e diversos (fraudadores evoluem suas táticas); protege a privacidade do cliente (não contém info do cliente).
- **Combate ao viés (bias):** gerado com precisão para incluir demografias diversas, garantindo representação justa e evitando práticas discriminatórias.
- **Teste de software (TDM):** usar dado de produção para teste vira risco com regulações como GDPR, CPRA, ISO 27001 (versão 2022). Dado sintético oferece nova abordagem de Test Data Management.

**Bancos e finanças:** superam limitações de uso, privacidade e segurança. Casos:
- **Anti-money laundering (AML / antilavagem de dinheiro):** gera grandes conjuntos de transações sintéticas para treinar e testar modelos AML.
- **Detecção de fraude e gestão de risco:** imita padrões de fraude reais, melhora detecção e reduz falsos positivos.
- **Redução de viés de dados:** datasets mais representativos de toda a população, incluindo grupos sub-representados.
- **Credit scoring e originação de empréstimo:** gera "gêmeos digitais" (digital twins) de clientes e simula scores de crédito.
- **Otimização de portfólio:** gera dados sobre vários cenários de investimento.
- **Stress testing e análise de cenários:** cria cenários hipotéticos difíceis/impossíveis de obter no mundo real para testar a robustez dos modelos.

**Saúde e farma (healthcare & pharma):** criam datasets realistas para treinar/avaliar modelos sem comprometer a confidencialidade do paciente. Tipos: dados de imagem (exames médicos) e dados tabulares (prontuário eletrônico, resultados de laboratório).

### Dicas para trabalhar com dado sintético

- **Comece com dados iniciais limpos:** dados limpos e bem estruturados são a base de datasets sintéticos precisos. Limpe/reconcilie primeiro.
- **Otimize para cenários realistas:** garanta que o dataset sintético contenha cenários/casos de uso realistas.
- **Teste seus resultados a fundo:** compare manualmente contra dado real ou use ferramentas estatísticas para destacar discrepâncias.
- **Considere requisitos regulatórios, leis de privacidade e cibersegurança:** GDPR, CCPA, e a Privacy Enhancing Technology Research Act (H.R.4755). Integrar PETs (Privacy Enhancing Technologies) como dado sintético reforça a proteção.

### Onde obter dado sintético?

- **Plataformas comerciais** (ex.: Syntheticus): plugam na infraestrutura existente e geram datasets realistas rapidamente; oferecem suporte, consultoria, garantias de privacidade/compliance e às vezes trials gratuitos.
- **Ferramentas open-source:** código e algoritmos para construir datasets customizados; gratuitas, com suporte da comunidade — ideais para pesquisadores/devs com orçamento limitado, mas nem sempre tão fáceis de usar ou customizáveis quanto soluções comerciais.

---

## Fonte 2 — Moez Ali (Medium): *Synthetic data is the future of Artificial Intelligence*

> Autor: Moez Ali · ~11 min de leitura · 18/01/2023 · Subtítulo: *Overcoming the Limitations of Real-World Data*
>
> ⚠️ **Material truncado no envio** — o artigo foi cortado no meio da seção de implementação em Python. O conteúdo abaixo reflete o que foi recebido.

### Introdução

Dado sintético é dado gerado artificialmente, projetado para imitar dado do mundo real. É criado usando algoritmos e modelos estatísticos que replicam os padrões, características e relações encontradas no dado real. Pode ser usado para treinar e testar modelos de ML, melhorar privacidade e segurança, e reduzir viés em datasets.

Um dos grandes casos de uso: pode **economizar milhões de dólares** ao cobrir riscos associados à privacidade e proteção de dados, conforme os padrões de compliance do **GDPR (General Data Protection Regulation)**. O GDPR é um conjunto de regras da União Europeia sobre como empresas devem tratar e proteger dados pessoais de indivíduos que vivem na UE. Foi oficialmente lançado em 25 de maio de 2018, substituindo a Diretiva de Proteção de Dados de 1995 da UE.

A penalidade por não-conformidade pode ser significativa: organizações em violação podem ser multadas em até **4% da receita global anual** ou **€20 milhões** (o que for maior).

### O que é dado sintético? (Moez Ali)

O termo refere-se a dado anotado artificialmente, produzido por algoritmos de computador ou simulações. É frequentemente utilizado como **fonte alternativa** ao dado real. Embora artificial, ele **imita estatisticamente** os padrões e características do dado real — essa é uma característica-chave.

É particularmente útil em IA e ML: permite que pesquisadores contornem problemas do dado real, como **viés, incompletude e falta de variedade**. Uma das principais vantagens é poder ser gerado em grande quantidade e com características diferentes, criando datasets diversos para treinar modelos — útil quando o dado real é escasso ou difícil de obter. Também protege a privacidade: gera-se dado removendo PII (informação pessoalmente identificável) ou gerando dado que não a contém.

### Casos de uso do dado sintético (Moez Ali)

1. **Treinar modelos de ML:** obter grandes volumes de dado real é difícil e demorado, especialmente se for sensível/regulado (GDPR). O dado real também pode ser enviesado, incompleto ou conter erros. O sintético suplementa ou substitui o real, permitindo treinar em um conjunto maior e mais diverso, melhorando desempenho e generalização do modelo.
2. **Reduzir viés (bias):** dado real costuma ser enviesado ou desbalanceado. Um dataset é enviesado se não dá uma imagem verdadeira da população — ex.: se a maioria das informações vem de um único grupo (raça, gênero), pode não representar bem os outros. O sintético permite **controlar a distribuição** de gênero, raça e outras características demográficas, tornando o dataset mais representativo.
3. **Reforçar privacidade protegendo PII:** dado real costuma conter informação privada que não pode ser compartilhada. O sintético representa esse dado de forma que preserva a privacidade. **PII** = qualquer informação que possa identificar um indivíduo (nome, endereço, telefone, email, CPF/SSN), além de info financeira, registros médicos e biométricos. Sob GDPR, organizações devem proteger isso e obter consentimento claro.

### GDPR, pseudonimização e anonimização

Dois conceitos subjacentes importantes:

- **Pseudonimização (pseudonymization):** substituir informação sensível (nomes, endereços) por um **pseudônimo ou identificador artificial**. O dado ainda pode ser **relinkado** ao dataset original, mas só com informação adicional (uma chave ou token).
- **Anonimização (anonymization):** tornar o dado **completamente anônimo**, impossível de identificar indivíduos. Remove/obscurece toda informação identificável. O dado anonimizado **não é linkável** a nenhum outro dataset e é impossível re-identificar indivíduos.

O dado sintético, quando gerado com proteções de privacidade apropriadas, oferece proteção contra ataques adversariais que técnicas tradicionais de anonimização (mascaramento, tokenização) não conseguem garantir.

**Recital 26 do GDPR:** afirma que "os princípios da proteção de dados não devem se aplicar a informação anônima, ou seja, informação que não se relaciona a uma pessoa natural identificada ou identificável, ou a dado pessoal tornado anônimo de modo que o titular não seja mais identificável". Dado pseudônimo ainda pode ser considerado dado pessoal se o controlador puder ligar o pseudônimo a uma pessoa via informação adicional. **Implicação:** se o dado sintético for gerado corretamente com os filtros apropriados, ele fica **fora do escopo do GDPR**, eliminando os riscos de trabalhar com dado real contendo PII.

### Ferramentas e stack

O ecossistema de startups que trabalham com dado sintético é diverso, focado em melhorar o desempenho de IA/ML, reforçar privacidade e segurança, reduzir viés, aumentar justiça (fairness) e melhorar a eficiência de processos data-driven.

**Gretel.ai** — empresa que fornece uma plataforma para criar dado sintético usando técnicas de ML de ponta, permitindo treinar modelos sem comprometer privacidade/segurança. Cobre dado tabular, NLP e séries temporais. Tem workflows e algoritmos para conformidade com GDPR (removendo PII).

### Implementação em Python (Gretel.ai)

O workflow de anonimização da Gretel.AI tem três passos (algoritmos):

1. **Classify (Classificar):** define uma política para encontrar e rotular dado sensível (PII, credenciais, regex customizado) em texto, logs e dados estruturados. Usa **named entity recognition (NER / reconhecimento de entidades nomeadas)** por baixo.
2. **Transform (Transformar):** define uma política para rotular e transformar o dataset — com opções avançadas como busca por regex customizado, deslocamento de datas (date shifting) e substituição por entidades falsas (fake entity replacements).
3. **Synthetics (Sintetizar):** gera dado sintético que **não pode ser relinkado** ao dado original. Modelos suportados:
   - **Gretel LSTM** — modelo de deep learning para dado tabular, séries temporais e texto (NLP).
   - **Gretel ACTGAN** — modelo adversário para dado tabular, dados numéricos estruturados e alto número de colunas.
   - **Gretel Amplify** — modelo estatístico para geração de altos volumes de dado tabular.
   - **Gretel DGAN** — modelo adversário para séries temporais.
   - **Gretel GPT** — transformer generativo pré-treinado para geração de texto natural.

```python
# Instalar dependências
%%capture
!git clone https://github.com/gretelai/gdpr-helpers.git
!cd gdpr-helpers; pip install -Uqq .

import os
if not os.getcwd().endswith('gdpr-helpers'):
    os.chdir('gdpr-helpers')
```

Usando o dataset de exemplo "bike buying" fornecido pela biblioteca da Gretel.ai:

```python
import glob
from gdpr_helpers import Anonymizer

search_pattern = "data/adventure-works-bike-buying.csv"

am = Anonymizer(
    project_name="gdpr-workflow",
    run_mode="cloud",
    transforms_config="src/config/transforms_config.yaml",
    synthetics_config="src/config/synthetics_config.yaml",
    endpoint="https://api.gretel.cloud"
    )

for dataset_path in glob.glob(search_pattern):
    am.anonymize(dataset_path=dataset_path)
```

Ao rodar, é pedida a API key (login na conta Gretel.ai → copiar a chave em settings; há cadastro gratuito com créditos). A classe `Anonymizer` requer dois arquivos de config (`transforms_config` e `synthetics_config`, em YAML). É possível acompanhar um dashboard ao vivo conforme o modelo treina. O processo roda por alguns minutos e gera três arquivos: (1) relatório, (2) CSV de dado transformado, (3) CSV de dado sintético.

> ⚠️ **O material recebido foi truncado a partir daqui** (limite de caracteres da mensagem). O artigo original continua com a análise do output gerado / relatório de anonimização.
