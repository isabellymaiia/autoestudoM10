# Distribuições de Probabilidade — Explicação

> **Matéria:** Matemática · **Autoestudo:** 01 · **Data:** 06/05/2026 · **Professor:** Diogo Martins Gonçalves de Morais
>
> ⚠️ Construída a partir dos **conceitos** dos vídeos do StatQuest referenciados (o material original não foi fornecido — ver nota no [`01-material.md`](01-material.md)). Quando você tiver as transcrições, posso ajustar exemplos e números para casar 100% com os vídeos.

---

## 1. Contexto geral: por que distribuições importam?

Esse é o **primeiro autoestudo de Matemática** do módulo, e ele é a fundação de quase tudo que vem na parte quantitativa — inclusive do teste A/B (o tema central). Então vamos do zero absoluto.

Imagine que você é dono de uma cafeteria e anota quantos clientes entram por hora, todos os dias, por um mês. Você acaba com uma montanha de números: 12, 8, 15, 11, 9, 14, 13… Olhar essa lista crua não te diz nada. Mas se você perguntar *"qual é o número típico de clientes? E quão imprevisível isso é?"*, você está pedindo para entender a **distribuição** desses dados.

Uma **distribuição** é, em uma frase: **uma descrição de quão frequentes (ou prováveis) são os diferentes valores que algo pode assumir.** Ela transforma um amontoado de números numa forma com significado — te diz **onde os dados se concentram** e **quão espalhados eles estão**.

Por que isso é o coração do módulo? Porque **todo teste A/B é, no fundo, uma comparação de distribuições**. "A versão B converte mais que a A?" é o mesmo que perguntar "a distribuição de conversões da B é diferente da distribuição da A, ou a diferença é só o acaso natural dos dados?". Sem entender distribuições, "significância estatística" e "intervalo de confiança" (que você já viu no Prog-02) são palavras vazias.

---

## 2. Conceitos-chave (do mais básico ao mais avançado)

### 2.1. Do histograma à distribuição

A ponte entre "dados crus" e "distribuição" é o **histograma**.

1. Pegue todas as suas medições (ex.: alturas de 1.000 pessoas).
2. Divida o eixo dos valores em "caixas" (em inglês, **bins**): 1,50–1,55 m; 1,55–1,60 m; etc.
3. Conte quantas medições caem em cada caixa e desenhe uma barra com essa altura.

O resultado é o histograma: barras altas onde há muitos dados, baixas onde há poucos. Agora vem a mágica: **conforme você coleta mais dados e usa caixas cada vez mais finas, o contorno irregular das barras vai virando uma curva suave.** Essa curva idealizada é a **distribuição**.

> **Analogia:** o histograma é uma foto granulada de baixa resolução; a distribuição é a foto em altíssima resolução que você obteria com infinitos dados. O histograma *estima* a distribuição.

### 2.2. Discreto vs. contínuo

Dois tipos de dados, dois tipos de distribuição:

- **Discreto (discrete):** valores **contáveis e separados**, sem meio-termo. Número de clientes (não existe "11,5 clientes"), resultado de um dado (1 a 6), número de cliques. Cada valor tem uma probabilidade própria.
- **Contínuo (continuous):** valores que podem assumir **qualquer ponto num intervalo**. Altura, peso, tempo, temperatura (entre 1,70 m e 1,71 m existem infinitos valores possíveis). Aqui falamos de probabilidade de cair numa **faixa**, não num ponto exato.

> Detalhe que confunde todo mundo: numa distribuição **contínua**, a probabilidade de um valor *exato* é tecnicamente zero (qual a chance de alguém medir *exatamente* 1,73000000… m?). Por isso medimos **áreas sob a curva** (faixas), não pontos.

### 2.3. Área = probabilidade

A regra de ouro de qualquer distribuição (contínua):
- A **área total sob a curva é 1** (= 100%, porque algum valor *vai* acontecer).
- A **área sob um trecho** da curva = a **probabilidade** de um valor cair naquele trecho.

Por isso a curva também se chama **função densidade de probabilidade (probability density function, PDF)**: a altura da curva indica a *densidade* de probabilidade, e a área é a probabilidade de fato.

### 2.4. Os dois números que descrevem uma distribuição

Quase toda distribuição pode ser resumida por duas perguntas:

1. **"Onde está o centro?"** → a **média (mean, μ)** — o valor típico, o "centro de gravidade" dos dados.
2. **"Quão espalhados estão os dados?"** → o **desvio padrão (standard deviation, σ)** — a dispersão em torno da média.

Sobre o desvio padrão, que costuma assustar:
- A **variância (variance, σ²)** é a média dos quadrados das distâncias de cada ponto à média. (Eleva-se ao quadrado para que distâncias negativas e positivas não se cancelem.)
- O **desvio padrão (σ)** é simplesmente a **raiz quadrada da variância** — o que o traz de volta à unidade original (metros, reais, clientes), ficando interpretável.

> **Intuição:** σ pequeno = dados "grudados" perto da média (previsível). σ grande = dados muito espalhados (imprevisível). Duas cafeterias podem ter a mesma média de 12 clientes/hora, mas uma com σ=1 (sempre por volta de 12) e outra com σ=6 (umas horas vazias, outras lotadas) — experiências de negócio completamente diferentes, mesmo com a mesma média.

### 2.5. A estrela do show: a distribuição normal

A **distribuição normal** — também **gaussiana (Gaussian)** ou **curva de sino (bell curve)** — é a distribuição mais importante de toda a estatística. Características:

- **Formato de sino simétrico:** o pico no centro (na média), decaindo igualmente para os dois lados. Média, mediana e moda coincidem no centro.
- **Definida por apenas dois parâmetros:** a **média (μ)**, que diz *onde* o sino está, e o **desvio padrão (σ)**, que diz *quão largo* ele é. Sabendo μ e σ, você sabe *tudo* sobre aquela normal.
- **Caudas infinitas:** a curva nunca toca o eixo, mas as pontas ficam finíssimas (valores extremos são raros, não impossíveis).

#### A regra empírica 68–95–99,7 (a "regra de ouro" da normal)

Numa distribuição normal, a distância em desvios padrão a partir da média te diz a probabilidade:

| Faixa | % dos dados |
|---|---|
| μ ± 1σ | ~**68%** |
| μ ± 2σ | ~**95%** |
| μ ± 3σ | ~**99,7%** |

> **Exemplo concreto:** notas de um vestibular com média μ=500 e desvio padrão σ=100. Então ~68% dos candidatos tiraram entre 400 e 600; ~95% entre 300 e 700; e ~99,7% entre 200 e 800. Quem tirou 750 está além de 2σ — no top ~2,5%. Esse raciocínio é a base do **Z-score**, que você vai ver em Matemática-03.

### 2.6. Por que a normal aparece em todo lugar?

Não é coincidência que altura, peso, erro de medição, ruído e tantas coisas sejam aproximadamente normais. A razão tem nome: o **Teorema Central do Limite (Central Limit Theorem, CLT)**. Numa frase intuitiva:

> Quando você **soma ou faz a média de muitos fatores aleatórios independentes**, o resultado tende a uma distribuição normal — *não importa* a distribuição de cada fator individual.

A altura de uma pessoa é a soma de centenas de pequenos efeitos (genes, nutrição, etc.); por isso a soma vira um sino. **E aqui está a ponte direta com teste A/B:** quando você calcula a *taxa de conversão média* de milhares de visitantes, essa média — pela CLT — se comporta como uma normal. É **por isso** que conseguimos usar a curva de sino para calcular significância estatística e intervalos de confiança num teste A/B, mesmo que cada visitante individual seja só um "converteu / não converteu" (que não tem nada de sino).

### 2.7. Outras distribuições que valem conhecer

A normal é a estrela, mas há um elenco de apoio (você já cruzou com algumas no Prog-02, no Monte Carlo):

- **Uniforme (uniform):** todos os valores igualmente prováveis (uma linha reta). Ex.: o resultado de um dado honesto, um sorteio.
- **Binomial (binomial):** conta **quantos sucessos** em N tentativas de "sim/não" (ex.: quantos dos 1.000 visitantes converteram). É *a* distribuição natural de um teste A/B, e para N grande ela se aproxima de uma normal.
- **Triangular (triangular):** definida por mínimo, máximo e valor mais provável — usada em estimativas de negócio (você viu no Monte Carlo).
- **Poisson:** conta eventos raros num intervalo (ex.: número de reclamações por dia).

---

## 3. Exemplo prático

Suponha um teste A/B onde a versão A teve **taxa de conversão de 10%** com **5.000 visitantes**.

```python
import numpy as np

# Cada visitante: 1 = converteu, 0 = não (distribuição de Bernoulli, p=0.10)
n, p = 5000, 0.10

# A taxa de conversão observada é uma MÉDIA de muitos 0s e 1s.
# Pela CLT, essa média se distribui ~ normalmente:
media   = p                      # 0.10  -> centro da normal
desvio  = np.sqrt(p*(1-p)/n)     # erro padrão da proporção
print(f"Conversão esperada: {media:.3f}")
print(f"Desvio padrão (erro padrão): {desvio:.4f}")
# ~0.0042  -> ou seja, ~95% das vezes a conversão medida cai em 0.10 ± 2*0.0042 = [9.16%, 10.84%]
```

Esse `0.10 ± 0.84%` é, na essência, um **intervalo de confiança de 95%** — e ele só existe porque a média de conversões segue uma **normal** (CLT). Se a versão B medir 12% de conversão, ela está *bem fora* dessa faixa → forte indício de que a diferença é real, não acaso. **Isso é exatamente o que um teste A/B calcula por baixo dos panos.**

---

## 4. Cases reais no mundo

- **Controle de qualidade industrial (Six Sigma):** o nome "Six Sigma" (Seis Sigma) vem *literalmente* de querer que defeitos fiquem além de **6 desvios padrão** da média — ou seja, pouquíssimos. Toyota, GE e Motorola construíram metodologias inteiras sobre a curva normal.
- **Mercado financeiro:** modelos de risco (como o VaR que você viu no Prog-02) assumem distribuições para retornos de ações. A crise de 2008 foi, em parte, uma lição de que retornos financeiros têm **caudas mais gordas** que a normal prevê (eventos extremos são mais comuns do que o sino diz) — um alerta clássico sobre escolher a distribuição certa.
- **Teste A/B na prática:** plataformas como Optimizely, VWO e o próprio RD Station (que você viu no Prog-02) calculam significância estatística assumindo a aproximação normal da distribuição binomial das conversões. Quando elas dizem "95% de confiança", estão usando a regra dos ~2σ.

---

## 5. Conexão com o módulo

Este autoestudo é a **espinha dorsal matemática** de várias coisas:

- **Prog-02 (Roadmap / Monte Carlo):** lá as distribuições (normal, uniforme, triangular) eram os "tijolos" de entrada da simulação de Monte Carlo. Agora você entende *o que elas são* de verdade.
- **Prog-03 (Avaliação de Dados Sintéticos):** o conceito de **"distribuição-mãe (parent distribution)"** daquele autoestudo é precisamente uma distribuição de probabilidade — e o objetivo de gerar dados sintéticos é replicá-la. A "mistura de gaussianas" usada lá são normais combinadas.
- **Matemática-03 (Formulação de Hipóteses Estatísticas — Z-score e Teste t):** o próximo grande passo. O **Z-score** mede "quantos desvios padrão um valor está da média" — só faz sentido depois de entender μ, σ e a normal. É a ferramenta que transforma "a B parece melhor" em "a B é melhor com 99% de confiança".
- **Teste A/B (tema do módulo):** intervalo de confiança, significância, p-value — tudo repousa sobre a distribuição normal e a CLT. Este autoestudo é o que torna esses termos compreensíveis.
- **UX-01 (Métodos Mistos):** o teste A/B é o método **quantitativo** por excelência; a matemática daqui é o que dá rigor a esse "quanti".

---

## 6. Resumo estruturado

- **Distribuição** = descrição de **quão prováveis/frequentes** são os valores que algo pode assumir (onde os dados se concentram + quão espalhados estão).
- **Histograma → distribuição:** com muitos dados e caixas finas, o histograma vira uma curva suave (a distribuição).
- **Discreto** (valores contáveis) vs. **contínuo** (qualquer valor num intervalo; probabilidade = **área** sob a curva, que soma 1).
- **Dois resumos essenciais:** **média (μ)** = centro; **desvio padrão (σ)** = espalhamento (raiz da **variância σ²**).
- **Distribuição normal (gaussiana / curva de sino):** simétrica, definida só por **μ** e **σ**. Regra **68–95–99,7** (±1σ, ±2σ, ±3σ).
- **Teorema Central do Limite (CLT):** médias/somas de muitos fatores aleatórios tendem à normal → é por isso que a normal está em todo lugar **e** por que conseguimos analisar testes A/B com ela.
- **Outras distribuições:** uniforme, binomial (a do A/B!), triangular, Poisson.

---

## 7. Auto-reflexão (pra pensar sozinha)

1. Duas turmas tiveram a **mesma média** na prova (7,0), mas a turma A teve σ=0,5 e a turma B teve σ=2,5. Sem ver as notas, o que você já sabe sobre como cada turma se saiu? Em qual turma é mais "arriscado" ser aluno?
2. Por que conseguimos usar a **curva de sino** para analisar um teste A/B, se cada visitante individual só faz uma de duas coisas (converte ou não — que não tem nada de "sino")? (Dica: pense na CLT e no que estamos *de fato* medindo.)
3. Uma loja diz que o tempo de entrega tem média de 5 dias e desvio padrão de 1 dia (distribuição aproximadamente normal). Usando a regra 68–95–99,7, qual a chance de uma entrega demorar **mais de 7 dias**?
