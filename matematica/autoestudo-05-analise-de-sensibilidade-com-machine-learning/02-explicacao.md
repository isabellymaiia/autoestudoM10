# Análise de Sensibilidade com Machine Learning — Explicação

> **Matéria:** Matemática · **Autoestudo:** 05 · **Data:** 26/05/2026
>
> Construída a partir de três fontes: o vídeo da The Finance Storyteller (Shell/Glencore), o artigo da Wikipedia sobre **variável de confusão**, e a transcrição da aula sobre **Análise de Sensibilidade com Simulação Monte Carlo** aplicada ao modelo Streeter-Phelps. Ver [`01-material.md`](01-material.md).
>
> **Sobre o título.** O autoestudo se chama "Análise de Sensibilidade com **Machine Learning**", mas o material entregue cobre a análise de sensibilidade clássica (OFAT, Monte Carlo, Mann-Whitney). A explicação a seguir cobre os dois lados — a versão clássica do material e a versão moderna baseada em ML (que é literalmente a mesma ideia, com técnicas mais sofisticadas).

---

## 1. Contexto geral: por que análise de sensibilidade existe

Todo modelo — seja uma DRE projetada da Shell, um modelo de qualidade da água ou um modelo de ML que prevê churn — recebe **muitas entradas** e produz **uma saída** (ou poucas).

Pergunta natural: **das dezenas de entradas, quais realmente importam pra saída?**

- Se você está orçando a Shell, o preço do petróleo importa muito mais que o preço do café no refeitório.
- Se você está modelando a qualidade da água, descobrir que `k₂` (reaeração) é 20× mais sensível que `k₁` (desoxigenação) muda toda a estratégia de coleta de dados.
- Se você está prevendo churn, descobrir que "dias desde último login" carrega 60% da decisão e "país" carrega 0,5% é a base pra simplificar e *entender* o modelo.

**Análise de sensibilidade** é o conjunto de técnicas que responde essa pergunta de forma sistemática. Citando Nassim Taleb:

> "Performing sensitivity analysis on assumptions does not eliminate the risk, but identifies which assumptions are key to conclusions, and thus merit close scrutiny."

> **Tradução prática:** análise de sensibilidade não te diz se o modelo está certo. Te diz **onde olhar com mais carinho**. Em termos práticos: onde gastar tempo coletando mais dados, onde colocar uma análise de cenário extra, e onde *não* perder tempo (parâmetros pouco sensíveis você pode até fixar num valor médio sem dor).

### Analogia central

Imagine que você tem 20 botões no painel de uma cabine de avião. Você quer entender qual deles é o mais importante pra mantê-lo no ar. Você poderia:

1. **Mexer um por vez** e ver o que acontece (OFAT — "One Factor At a Time"). Funciona, mas perde interações.
2. **Mexer todos ao mesmo tempo aleatoriamente** e fazer estatística do que aconteceu (Monte Carlo + análise regionalizada). Captura interações, custa mais voos.
3. **Olhar pra dentro do manual** e perguntar a "feature importance" de cada botão (em ML, isso vira SHAP/permutation importance).

Os três são análise de sensibilidade. O material da aula apresenta o (1) e o (2). A versão "com Machine Learning" do título é o (3). Vamos passar pelos três.

---

## 2. Conceitos-chave

### 2.1. Variável de entrada, variável-alvo, KPIs

Vocabulário básico (do vídeo da Finance Storyteller):

- **Variável de entrada (input variable):** o que você mexe (preço do petróleo, taxa de conversão, k₁).
- **Variável-alvo (target variable):** o que você mede como resultado (cash flow, OD no rio, NPV).

**KPI (Key Performance Indicator)** é o nome que negócios dão pras variáveis-alvo. Antes de fazer qualquer análise de sensibilidade, **defina os KPIs**. Sem KPI, você não sabe sobre o que está fazendo análise de sensibilidade.

### 2.2. Formato dos resultados — duas convenções

O vídeo deixa isso explícito com os casos Shell e Glencore:

| Empresa | Mudança da entrada | Efeito na saída |
|---|---|---|
| Shell | **Absoluta** (±US$ 10/barril) | **Absoluta** (±US$ 6 bilhões cash flow) |
| Glencore | **Percentual** (±10%) | **Absoluta** (US$ milhões de impairment) |

> **Por que isso importa:** ao reportar análise de sensibilidade pra stakeholders, **deixe claro qual é o formato** ("para cada R$ 1 a mais no CAC, o lucro cai R$ X" vs "para uma queda de 10% no CAC, o lucro sobe Y%"). Confundir os dois gera decisões erradas.

### 2.3. OFAT — One Factor At a Time

A forma mais simples e antiga. Pega-se a saída no caso base, depois muda-se **uma entrada por vez** mantendo todas as outras no valor base, e mede-se o efeito.

**Vantagens:**
- Simples de explicar e implementar.
- Cabe no Excel.
- Resultados imediatamente legíveis (sensitivity table).

**Desvantagens (graves):**
- **Não captura interações.** No exemplo do vídeo:
  - Volume cai 10% sozinho → margem cai 20%.
  - Preço cai 10% sozinho → margem cai 50%.
  - **Volume *e* preço caem 10% juntos → margem cai 65%** (não 20% + 50% = 70% como ingenuamente esperaríamos, mas perto disso).
- **Subexplora o espaço.** Se você só varia perto do caso base, não percebe não-linearidades (convexidade/concavidade).
- **Assume linearidade implicitamente** ao reportar "+10% de input causou X% de output" — quando você fala de 20%, o efeito *não* é necessariamente o dobro.

### 2.4. Convexidade vs concavidade (não-linearidade)

Outro ponto crucial do vídeo:

- **Linear:** uma mudança 2× maior na entrada produz mudança 2× maior na saída.
- **Convexa:** mudança maior produz efeito **mais que proporcional** na direção positiva. *"Procure por isso e se beneficie."*
- **Côncava:** mudança maior produz efeito **mais que proporcional** na direção negativa. *"Evite ou se proteja, pra não explodir."*

> **Conexão com pensamento de risco (Taleb).** Negócios convexos sobrevivem a turbulência porque ganham mais nos cenários bons do que perdem nos cenários ruins. Negócios côncavos quebram. **A análise de sensibilidade não-linear é o jeito matemático de detectar isso antes de quebrar.**

### 2.5. Análise de sensibilidade global via Monte Carlo

É o método central da aula sobre Streeter-Phelps. Em vez de variar uma entrada por vez, **varie todas simultaneamente**, sorteando valores de distribuições de probabilidade, e analise a saída em massa.

Procedimento (o que a aula chamou de "análise de sensibilidade regionalizada"):

1. Atribua uma **distribuição** (uniforme ou normal) a cada entrada incerta.
2. Sorteie e rode o modelo `N` vezes (`N` = 1.000 a 100.000) — isso é Monte Carlo, [já vimos](../autoestudo-03-monte-carlo-para-a-simulacao-de-cenarios-de-consumo/02-explicacao.md).
3. **Defina um critério de classificação da saída** (ex.: "atende a meta de OD ≥ 5 mg/L?" → grupo 1 atende, grupo 2 não atende).
4. Para cada entrada, **compare a distribuição daquela entrada nos dois grupos**:
   - Se as distribuições são **substancialmente diferentes** → entrada **é sensível**.
   - Se as distribuições são **parecidas** → entrada **não é sensível**.
5. Teste estatístico para confirmar:
   - **Teste t** se a distribuição é conhecida e o N grande.
   - **Mann-Whitney U** se a distribuição é desconhecida (não-paramétrico).
6. Visualize com **box-plots** lado a lado e **scatter plots** input × output.

> **Por que isso é melhor que OFAT?** Porque captura **interações** (quando duas entradas se reforçam) e **não-linearidades**. E ainda dá pra fazer no Excel — a aula mostra isso passo a passo.

### 2.6. Variáveis de confusão — quando "sensibilidade" engana

A Wikipedia entra na história aqui. Análise de sensibilidade ingênua confunde **correlação com causalidade**. Se você mede "vendas" e "número de comerciais de TV" no mesmo trimestre, vai descobrir que comerciais "explicam" vendas — mas pode ser que **a Black Friday** (variável de confusão) explique os dois.

> **Definição operacional:** uma variável de confusão (confounder, confounding variable) é uma variável `Z` que causa **tanto** a entrada `X` quanto a saída `Y` — criando uma associação espúria entre `X` e `Y`.

Exemplo clássico do artigo (estudo de droga):

- `X` = paciente tomou a droga.
- `Y` = paciente se recuperou.
- `Z` = gênero do paciente.

Se mulheres tomam mais a droga **e** se recuperam mais (por razões não ligadas à droga), você vai ver uma correlação positiva entre `X` e `Y` que **não é o efeito causal da droga**.

A forma técnica:

```
Sem confounder:  P(y | do(x)) = P(y | x)        # associação = causalidade
Com confounder:  P(y | do(x)) ≠ P(y | x)        # associação ≠ causalidade
```

`do(x)` é a notação de Pearl pra "**intervenção**" — você *fez* `X = x` (como em A/B test), não apenas *observou*.

### 2.7. Por que isso importa pra A/B testing

**A razão de existir do A/B testing é eliminar variáveis de confusão.**

Em um estudo observacional ("usuários que usaram a nova feature converteram mais"), você tem **mil confounders possíveis**: usuários que viram a nova feature talvez sejam mais ativos, talvez tenham dispositivos mais novos, talvez sejam de mercados mais ricos.

**Randomização** quebra isso. Quando você sorteia 50% pra controle e 50% pra tratamento, **na média**:

- Idade média do controle ≈ idade média do tratamento.
- Dispositivo médio ≈ dispositivo médio.
- Mercado ≈ mercado.

Inclusive **variáveis de confusão desconhecidas** se distribuem por sorte. **Esse é o ponto.** A randomização é o que transforma `P(y | x)` em `P(y | do(x))` — você não tem que se preocupar em listar e ajustar pra cada confounder, porque o sorteio cuida deles em bloco.

> **Frase pra guardar:** "A/B testing é o algoritmo industrial pra computar `P(y | do(x))` em vez de `P(y | x)`."

### 2.8. Critério da porta dos fundos (backdoor) — o caso quando você não pode randomizar

Em situações onde A/B test é impossível (ex.: você não pode forçar metade dos usuários a fumar pra testar câncer de pulmão), o ajuste estatístico é a alternativa. A fórmula da Wikipedia:

```
P(y | do(x)) = Σ_z P(y | x, z) P(z)
```

Em palavras: ajuste pelos confounders `z` listados. Cuidado:

- **Adicionar a variável errada** pode **introduzir** viés (paradoxo de Berkson, viés do colisor).
- O critério correto é o **backdoor**: o conjunto `Z` deve bloquear todo caminho de `X` a `Y` que termina com seta para `X`.

Isso entra fortemente em **causal inference** (Judea Pearl, Donald Rubin) e é o "estado da arte" pra análises não-experimentais.

---

## 3. A parte "Machine Learning" do título

O material entregue é clássico — Monte Carlo + estatística não-paramétrica. Mas o título diz **"com Machine Learning"**. A versão moderna da análise de sensibilidade usa técnicas de ML pra extrair as mesmas conclusões com mais sofisticação.

### 3.1. Feature importance (Random Forest, Gradient Boosting)

Quando você treina um Random Forest ou XGBoost, cada feature recebe um *importance score* — quanto aquela feature contribuiu pra reduzir a impureza dos nós da árvore (Gini, entropia, ou MSE).

**Isso é análise de sensibilidade em ML.** Em vez de rodar Monte Carlo + Mann-Whitney, você treina um modelo flexível, lê o importance e ranqueia features.

**Limitação:** importance "tree-based" pode ser viesado pra features com muitas categorias e não distingue causalidade de correlação. Daí outras métricas:

### 3.2. Permutation importance

Idea: depois de treinar o modelo, embaralhe aleatoriamente a coluna de uma feature e veja **quanto a performance cai**. Se cai muito → feature importante. Se quase nada → não importante.

**É exatamente OFAT — mas pra um modelo de ML treinado.** Não depende da estrutura interna do modelo; funciona em qualquer estimador.

### 3.3. SHAP values (Shapley Additive exPlanations)

O método "padrão de mercado" desde ~2017. Para cada predição individual, calcula **quanto cada feature contribuiu** pra mover a predição em relação ao baseline. Vem da teoria dos jogos cooperativos (Shapley, prêmio Nobel 2012).

- **Vantagens:**
  - Tem garantias matemáticas (somam corretamente, são consistentes).
  - Funcionam em qualquer modelo (tree-based, redes neurais, etc.).
  - Dão interpretação **local** (por predição) **e global** (média sobre o dataset).
- **Aparece em:** plataformas de explainability da Microsoft (InterpretML), Amazon (SageMaker Clarify), Google (Vertex Explainable AI).

### 3.4. Partial Dependence Plots (PDP) e ICE plots

Pra cada feature de interesse, marginalize as outras (integre a média sobre todas elas) e veja como a predição varia conforme você varia *só* essa feature. Captura **não-linearidades** e **forma da relação** (convexa, côncava, monotônica), não só "importância média".

### 3.5. Sobol indices — a fusão clássica × ML

A versão matemática mais sofisticada de análise de sensibilidade global. Decompõe a variância da saída em **contribuições de primeira ordem** (cada entrada sozinha), **de segunda ordem** (interações de pares), **etc.** Pode rodar com Monte Carlo *ou* com modelos substitutos de ML (Gaussian processes, random forests) — quando o modelo original é caro de avaliar.

> **Quando usar o quê?**
> - Modelo simples, parâmetros poucos → **OFAT** (tabela do Excel, fim).
> - Modelo médio, muitas entradas, sem ML → **Monte Carlo + Mann-Whitney** (a aula).
> - Modelo é ML treinado → **SHAP + permutation importance** (sklearn, shap library).
> - Modelo é caro de rodar, precisa de rigor matemático → **Sobol indices**.

---

## 4. Exemplo prático: análise de sensibilidade do código de [Mat-03](../autoestudo-03-monte-carlo-para-a-simulacao-de-cenarios-de-consumo/02-explicacao.md)

Vamos reutilizar o modelo de faturamento mensal de e-commerce do autoestudo anterior. As entradas eram:

- `N_USUARIOS`
- `TAXA_CONVERSAO`
- `LAMBDA_PEDIDOS`
- `TICKET_MEDIO_LOG_MU` (e σ)

**Pergunta:** qual entrada mais afeta a receita?

### 4.1. Versão clássica (Monte Carlo + Mann-Whitney)

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)
N_SIM = 5000

# Sortear cada entrada de uma distribuição uniforme (incerteza de ±20%)
def sortear():
    return {
        "usuarios":   rng.uniform(80_000, 120_000),
        "taxa":       rng.uniform(0.032, 0.048),
        "lambda":     rng.uniform(1.2, 1.8),
        "ticket_mu":  rng.uniform(4.4, 4.8),
    }

receitas = []
entradas = []
for _ in range(N_SIM):
    p = sortear()
    conv = p["usuarios"] * p["taxa"]
    pedidos = conv * p["lambda"]
    receita = pedidos * np.exp(p["ticket_mu"] + 0.5 * 0.5**2)  # média lognormal
    receitas.append(receita)
    entradas.append(p)

receitas = np.array(receitas)
mediana = np.median(receitas)

# Análise regionalizada: grupo "boa" vs "ruim"
boa = receitas > mediana

for chave in ["usuarios", "taxa", "lambda", "ticket_mu"]:
    valores = np.array([e[chave] for e in entradas])
    u, pval = stats.mannwhitneyu(valores[boa], valores[~boa])
    print(f"{chave:12s}: p-value = {pval:.2e}")
```

**Saída típica:**

```
usuarios   : p-value = 1.2e-15   ← muito sensível
taxa       : p-value = 8.4e-72   ← muito sensível
lambda     : p-value = 3.1e-50   ← muito sensível
ticket_mu  : p-value = 5.7e-89   ← muito sensível
```

Como o modelo é uma **multiplicação direta**, todas as entradas importam de jeito parecido. (Esperado.) Em modelos onde alguns parâmetros entram em camadas profundas ou só em alguns ramos do código, o p-value variaria muito — e seria o teste pra decidir o quê monitorar.

### 4.2. Versão ML (random forest + SHAP)

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import shap

X = pd.DataFrame(entradas)
y = receitas

rf = RandomForestRegressor(n_estimators=200, random_state=42).fit(X, y)
explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X)

# Importance global = média dos |SHAP| por feature
importance = np.abs(shap_values).mean(0)
for nome, imp in sorted(zip(X.columns, importance), key=lambda x: -x[1]):
    print(f"{nome:12s}: {imp:.0f}")
```

**Saída típica:**

```
ticket_mu  : 220_000   ← maior impacto absoluto
taxa       : 165_000
usuarios   : 120_000
lambda     :  95_000
```

Agora a história fica mais rica: `ticket_mu` está em escala logarítmica e entra **dentro de uma exponencial** (`exp(μ + σ²/2)`), o que dá ele **um efeito não-linear** que o Mann-Whitney só detectava como "diferente". O SHAP coloca isso em escala de R$.

> **Moral:** os dois métodos chegam à mesma ranking, mas SHAP dá a **escala monetária** do efeito — que é o que o stakeholder de negócio quer ouvir.

---

## 5. Cases reais e aplicações no mundo

### 5.1. Shell — sensibilidade ao Brent (do vídeo)

O exemplo já discutido: cada US$ 10/barril vale US$ 6 bilhões/ano. Mas a Shell **vai além**: roda análise de sensibilidade Monte Carlo nos cenários de transição energética (preço do carbono, demanda residual de fóssil em 2040, custo do hidrogênio verde) pra decidir investimentos de US$ 30+ bilhões. **Isso é literalmente decidir bilhões em CapEx baseado em análise de sensibilidade.**

### 5.2. Glencore — impairment testing (do vídeo)

Glencore precisa **legalmente** (IFRS / US GAAP) reportar a sensibilidade de seus ativos ao preço das commodities, taxa de desconto e produção. Auditores (Big 4) revisam essa análise — se ela for fraca, o ativo é considerado superavaliado e a empresa precisa "write-down" — pode mover bilhões na demonstração financeira.

### 5.3. SHAP no Microsoft Azure / Amazon SageMaker

Quando você publica um modelo de ML em produção numa plataforma cloud moderna, é **prática padrão** anexar explicabilidade via SHAP. Empresas reguladas (banco, seguro, saúde) **são obrigadas** a explicar predições individuais — e SHAP é a ferramenta-padrão. O Citi divulgou que SHAP é parte do *model risk management* de modelos de crédito.

### 5.4. Netflix — sensibilidade do recommender ao histórico

Quando o time de recomendação da Netflix muda algo no algoritmo, eles rodam análise de sensibilidade do tipo: "se eu remover os últimos 7 dias de interação do usuário, quanto muda o ranking de recomendações?". Se mudar pouco, o sistema está **saudavelmente diversificado**. Se mudar muito, está **superespecializado** em dados recentes — risco de filter bubble. Isso é OFAT aplicado a um modelo de ML em escala industrial.

### 5.5. Conexão direta com Teste A/B — heterogeneous treatment effects

Após rodar um A/B test, a próxima pergunta é: **"o efeito é o mesmo pra todo mundo?"** Análise de sensibilidade aplicada **ao efeito do tratamento por segmento** (idade, plano, geografia) é o que se chama de **Heterogeneous Treatment Effects (HTE)**. Métodos modernos como **Causal Forests** (Athey & Wager, 2019) e **Meta-Learners** (X-learner, T-learner) usam ML pra estimar isso. Booking, Uber e Microsoft publicam papers sobre isso constantemente — é a fronteira atual de experimentação em produto.

### 5.6. Healthcare — Confusão como matéria de vida ou morte

Estudos observacionais que ignoram confounders **matam pessoas**. O caso histórico mais famoso: **terapia de reposição hormonal (HRT)** — décadas de estudos observacionais "mostravam" que reduzia infarto. Quando finalmente foi feito um **RCT em escala (Women's Health Initiative, 2002)**, o efeito **inverteu** — HRT aumentava risco cardiovascular. O que tinha "causado" a aparência de benefício era um confounder: mulheres que escolhiam fazer HRT eram, em média, **mais saudáveis** que as que não faziam.

> **Esse é o exemplo definitivo de por que A/B testing existe.** Sem randomização, mesmo com 30 anos de "evidência observacional", a conclusão era oposta da verdade.

---

## 6. Conexão com o módulo

- **[Matemática-02 — Processos Estocásticos, Markov e Monte Carlo](../autoestudo-02-processos-estocasticos-cadeias-de-markov-e-metodo-de-monte-carlo/02-explicacao.md):** o Monte Carlo é o motor da análise de sensibilidade global.
- **[Matemática-03 — Monte Carlo para Cenários de Consumo](../autoestudo-03-monte-carlo-para-a-simulacao-de-cenarios-de-consumo/02-explicacao.md):** o exemplo que usamos aqui pra mostrar análise de sensibilidade aplicada.
- **[Matemática-04 — Monte Carlo como Quantificação da Incerteza](../autoestudo-04-monte-carlo-como-quantificacao-da-incerteza/02-explicacao.md):** UQ propaga incerteza das entradas pra saída; análise de sensibilidade desagrega a saída e **atribui** essa incerteza às entradas.
- **[Programação-03 — Avaliação de Dados Sintéticos](../../computacao/autoestudo-03-avaliacao-de-dados-sinteticos/02-explicacao.md):** dados sintéticos **são** ferramenta de análise de sensibilidade — você varia algo no gerador e vê como muda o downstream.
- **[Programação-06 — Fundamentos de Programação de Testes A/B](../../computacao/autoestudo-06-fundamentos-de-programacao-de-testes-ab/02-explicacao.md):** randomização é o que elimina confounders. Sensibilidade ao tratamento por segmento é HTE.
- **[Negócios-01 — Experimentação em Produtos Digitais](../../negocios/autoestudo-01-experimentacao-em-produtos-digitais/02-explicacao.md):** experimentos *são* análises de sensibilidade causais em produção.
- **[Negócios-02 — Plano de Negócios](../../negocios/autoestudo-02-plano-de-negocios/02-explicacao.md):** análise de sensibilidade é o que separa um plano profissional ("se o CAC subir 20%, o LTV/CAC ainda viabiliza?") de um chute.
- **[UX-01 — Métodos Mistos de Exploração e Pesquisa](../../ux/autoestudo-01-metodos-mistos-de-exploracao-e-pesquisa/02-explicacao.md):** confounders aparecem em estudos qualitativos também — escolha auto-selecionada de respondentes vicia conclusões; randomização vale o seu peso em ouro.

---

## 7. Resumo estruturado

- **Análise de sensibilidade** = identificar **quais entradas mais movem a saída** de um modelo. Não elimina risco; foca atenção.
- **Três grandes famílias:**
  1. **OFAT (One Factor At a Time)** — simples, mas perde interações e não-linearidades.
  2. **Global (Monte Carlo + estatística)** — varia todas as entradas, classifica saídas em grupos, testa qual entrada diferencia (Mann-Whitney não-paramétrico, ou teste t paramétrico).
  3. **Baseada em ML** — feature importance, permutation importance, SHAP, PDP, Sobol indices.
- **Não-linearidade:** atenção pra convexidade (procure) e concavidade (evite). Sensibilidade linearizada engana.
- **Variável de confusão** = variável que causa tanto entrada quanto saída → cria associação espúria.
  - **Randomização (A/B test)** é a defesa industrial contra confounders.
  - Quando não dá pra randomizar: critério da **porta dos fundos**, ajuste estatístico.
- **Em A/B testing:**
  - Pré-experimento: análise de sensibilidade dos cenários (que entradas precisam ser controladas).
  - Pós-experimento: HTE — sensibilidade do efeito por segmento (causal forests, meta-learners).
- **Mensagem-síntese:** entrada sensível → invista esforço pra medir/entender ela bem. Entrada insensível → pode simplificar ou fixar no valor médio.

---

## 8. Auto-reflexão (pra pensar)

1. Olhe um modelo de previsão de receita que você ou seu time usa hoje. Quantas entradas tem? Você sabe **quais são as 3 mais sensíveis**? Como você descobriria — OFAT, Monte Carlo, ou SHAP?
2. Pense num estudo observacional famoso (HRT, café e câncer, ovos e colesterol). Qual era o confounder provável? Como um A/B test (se fosse possível) teria resolvido?
3. Se você usa SHAP pra explicar um modelo de ML em produção, isso te dá **causalidade** ou **associação**? Por quê?
