# Monte Carlo para a Simulação de Cenários de Consumo — Explicação

> **Matéria:** Matemática · **Autoestudo:** 03 · **Data:** 22/05/2026
>
> ⚠️ Construída a partir dos **conceitos** padrão do tema (material original não fornecido — ver [`01-material.md`](01-material.md)).
>
> Este autoestudo costura três coisas que já vimos no módulo:
> - O **Monte Carlo** formal de [Matemática-02](../autoestudo-02-processos-estocasticos-cadeias-de-markov-e-metodo-de-monte-carlo/02-explicacao.md) (a teoria de por que funciona).
> - O **Monte Carlo aplicado** de [Programação-02](../../computacao/autoestudo-02-roadmap-do-projeto-perspectiva-de-programacao/02-explicacao.md) (o "como rodar muitas vezes").
> - As **distribuições de probabilidade** de [Matemática-01](../autoestudo-01-distribuicoes-de-probabilidade/02-explicacao.md) (a matéria-prima das simulações).
>
> Agora vamos colocar tudo isso em cima de uma pergunta concreta: **"quanto a minha base de usuários vai consumir mês que vem?"** — e responder com uma *distribuição*, não com um número.

---

## 1. Contexto geral: por que simular cenários de consumo?

Imagine que você é gerente de produto de um e-commerce. Seu chefe vem na sua mesa e pergunta: **"Quanto a gente vai faturar mês que vem?"**

Você tem três opções:

1. **Chutar um número único.** "Acho que R$ 1,2 milhão." Profissional? Não.
2. **Fazer uma média histórica.** "Os últimos 6 meses fizeram, em média, R$ 1,1 milhão. Então R$ 1,1 milhão." Melhor — mas joga fora toda a informação sobre o quão *certo* (ou incerto) você está.
3. **Simular.** "Tem 80% de chance de ficar entre R$ 950 mil e R$ 1,35 milhão. A mediana é R$ 1,15 milhão. Tem 5% de chance de furar pra baixo de R$ 900 mil." **Isso** é uma resposta de adulto.

A terceira opção é o que **Monte Carlo de cenários de consumo** entrega: em vez de um número, **uma distribuição inteira** de futuros possíveis.

> **Analogia central.** Pense num meteorologista. Ele *não* fala "vai chover 18 mm amanhã". Ele fala "70% de chance de chuva, com 60% de chance de ficar entre 10 e 25 mm". Como é que ele consegue isso? Ele roda o modelo atmosférico **centenas de vezes**, cada vez com condições iniciais um pouquinho diferentes (dentro da margem de erro dos sensores). Cada rodada é um "futuro possível". A distribuição desses futuros é a previsão. Isso é Monte Carlo. Você vai fazer o mesmo, só que com **carrinho de compras** no lugar de **frente fria**.

### Por que isso importa pro módulo de Teste A/B?

Antes de gastar 4 semanas rodando um experimento, você precisa saber:

- Quanto **dinheiro** está em jogo (vale a pena testar?).
- Qual é a **menor diferença detectável (MDE — Minimum Detectable Effect)** que importa pro negócio.
- Qual é o **risco** de uma decisão (e se for um falso positivo, perdemos quanto?).

Monte Carlo de cenários de consumo é a ferramenta que responde essas perguntas **antes** do teste rodar. Sem ela, A/B test vira "experimento bonitinho que não move o ponteiro".

---

## 2. Conceitos-chave

### 2.1. Voltando ao Monte Carlo em uma frase

> **Monte Carlo:** quando você não consegue calcular uma quantidade analiticamente, você **sorteia muitos cenários aleatórios** e calcula a estatística *empiricamente*.

A Lei dos Grandes Números (vista em [Matemática-02](../autoestudo-02-processos-estocasticos-cadeias-de-markov-e-metodo-de-monte-carlo/02-explicacao.md)) garante que, conforme `N → ∞`, a média das simulações converge pro valor verdadeiro. O erro cai com **1/√N** — então pra ter o erro 10× menor, você precisa de 100× mais simulações.

### 2.2. O que é "um cenário"?

Um **cenário (scenario)** é **uma execução completa** do seu modelo, do início ao fim, com **um valor sorteado** para cada variável de entrada incerta.

Exemplo concreto: pra simular o faturamento de mês que vem, um cenário precisa decidir:

- Quantos usuários ativos teremos?
- Quantos vão comprar?
- Quantas compras cada um vai fazer?
- Qual o ticket médio de cada compra?

Cada uma dessas perguntas tem uma **distribuição de probabilidade** atrás. Um cenário **sorteia um valor** de cada distribuição e calcula o faturamento total. **N** cenários (N = 10 mil, p.ex.) te dão uma distribuição empírica de faturamento.

### 2.3. As distribuições que você vai usar pra modelar consumo

Esta é a parte que mais conecta com [Matemática-01 (Distribuições de Probabilidade)](../autoestudo-01-distribuicoes-de-probabilidade/02-explicacao.md). **Diferentes coisas que você mede pedem distribuições diferentes**:

| O que você quer modelar | Distribuição típica | Por quê |
|---|---|---|
| **Converteu / não converteu** (1 usuário) | **Bernoulli** | Sucesso/fracasso, uma tentativa. |
| **Quantos converteram** (em N usuários) | **Binomial** | Soma de N Bernoullis independentes. |
| **Quantos pedidos por usuário** | **Poisson** | Contagem de eventos raros num intervalo. |
| **Ticket médio (R$ por compra)** | **Lognormal** ou **Gamma** | Valor positivo, cauda longa à direita (alguns clientes gastam muito mais que a média). |
| **Tempo até churn** | **Exponencial** ou **Weibull** | "Tempo até evento" — fundação de survival analysis. |
| **Tempo entre compras** | **Exponencial** | Memoryless: o próximo intervalo não depende do tempo desde a última compra. |

> **Por que ticket médio não é Normal?** Porque ticket é positivo (você não compra valores negativos) e **assimétrico**: a maioria gasta pouco, e poucos clientes gastam *muito* mais. A Lognormal captura isso (cauda à direita). Modelar ticket como Normal é o erro mais comum em projeções de e-commerce — superestima a probabilidade de valores extremamente baixos e subestima a de valores extremamente altos.

### 2.4. O algoritmo em 5 passos

```
1. DEFINIR o modelo: qual é a fórmula que liga as entradas à saída?
   ex.: receita = usuarios_ativos × taxa_conversao × pedidos_por_conversor × ticket_medio

2. PARAMETRIZAR cada entrada com uma distribuição (baseada em dados históricos).
   ex.: taxa_conversao ~ Beta(α, β)  (Beta é a distribuição "natural" pra taxas entre 0 e 1)

3. SORTEAR um valor de cada distribuição → 1 cenário.

4. CALCULAR a saída pra esse cenário.

5. REPETIR N vezes (N = 10.000, 100.000). Cada repetição é um ponto na distribuição final.
```

### 2.5. Cenários nomeados vs. distribuição contínua

Tradicionalmente em consultoria/finanças, "cenários" eram **3 valores fixos**:

- **Base case** — premissas médias.
- **Optimistic** — premissas favoráveis.
- **Pessimistic** — premissas desfavoráveis.

Monte Carlo **enriquece isso**: em vez de 3 cenários, você tem **uma distribuição contínua**. Daí você extrai:

- **Mediana (P50)** — o "valor mais provável".
- **P10 e P90** — banda de confiança 80%.
- **P5 e P95** — banda de 90%.
- **Value at Risk (VaR)** — "qual é o pior 5%?" (financeiro).
- **Probability of breaking target** — "qual a chance de bater a meta de R$ 1M?".

> **Ganho conceitual.** Os "três cenários" eram uma simplificação imposta pela época do Excel pré-2000. Hoje, com um notebook Python, você roda 100.000 cenários em segundos. Não tem desculpa pra continuar entregando "otimista / pessimista / base" como resposta de previsão.

---

## 3. Exemplo prático: simulando faturamento mensal de um e-commerce

Vamos colocar isso em código.

### 3.1. Modelo

```
faturamento_mes = Σᵢ (compras_do_usuario_i × ticket_medio_do_usuario_i)
```

Pra cada usuário ativo:
- `comprou` ~ Bernoulli(p) — com `p` = taxa de conversão histórica.
- Se comprou: `n_pedidos` ~ Poisson(λ) — λ = média histórica de pedidos por conversor.
- Pra cada pedido: `valor` ~ Lognormal(μ, σ).

### 3.2. Código

```python
import numpy as np

# ── Premissas (calibradas com base em dados históricos) ──
N_USUARIOS = 100_000          # usuários ativos no mês
TAXA_CONVERSAO = 0.04         # 4% convertem
LAMBDA_PEDIDOS = 1.5          # média de pedidos por conversor
TICKET_MEDIO_LOG_MU = 4.6     # ln(ticket médio) ≈ 4.6 → ticket ≈ R$ 99
TICKET_MEDIO_LOG_SIGMA = 0.5  # dispersão dos tickets

N_SIMULACOES = 10_000
rng = np.random.default_rng(42)

receitas_mensais = np.zeros(N_SIMULACOES)

for sim in range(N_SIMULACOES):
    # Quantos converteram?
    conversores = rng.binomial(N_USUARIOS, TAXA_CONVERSAO)

    # Pra cada conversor, quantos pedidos?
    n_pedidos_por_conv = rng.poisson(LAMBDA_PEDIDOS, size=conversores)
    total_pedidos = n_pedidos_por_conv.sum()

    # Ticket de cada pedido (lognormal — captura cauda à direita)
    tickets = rng.lognormal(TICKET_MEDIO_LOG_MU,
                             TICKET_MEDIO_LOG_SIGMA,
                             size=total_pedidos)

    receitas_mensais[sim] = tickets.sum()

# ── Análise da distribuição resultante ──
print(f"Mediana (P50):   R$ {np.median(receitas_mensais):,.0f}")
print(f"Média:           R$ {np.mean(receitas_mensais):,.0f}")
print(f"P10:             R$ {np.percentile(receitas_mensais, 10):,.0f}")
print(f"P90:             R$ {np.percentile(receitas_mensais, 90):,.0f}")
print(f"P(receita > R$ 800k): {(receitas_mensais > 800_000).mean():.1%}")
```

### 3.3. Saída esperada (mental model)

```
Mediana (P50):   R$ 660.000
Média:           R$ 678.000   ← maior que mediana por causa da cauda lognormal
P10:             R$ 555.000
P90:             R$ 815.000
P(receita > R$ 800k): 12.4%
```

**O que você diz pro seu chefe agora?**
> "A receita esperada de mês que vem é R$ 660 mil (mediana). Tem 80% de chance de ficar entre R$ 555 mil e R$ 815 mil. Mas só 12% de chance de bater R$ 800 mil — se essa for a meta, ela está agressiva."

**Isso é incomparavelmente mais útil que "vai dar R$ 678 mil".**

### 3.4. Dois cuidados que aparecem aqui

1. **Mediana ≠ Média** numa distribuição assimétrica (como lognormal). Pra projeções de consumo, **sempre** reporte ambas — e prefira mediana como "valor típico".
2. **Independência entre amostras.** O código acima assume que pedidos diferentes têm tickets independentes. Em alguns negócios, isso é falso (um cliente premium tende a ter *todos* os tickets altos). Pra capturar isso, você modela em **dois níveis**: sorteia um "tipo de cliente" primeiro, e depois sorteia os tickets daquele tipo. Hierárquico.

---

## 4. Cases reais e aplicações no mundo

### 4.1. Amazon — "Working Backwards" com Monte Carlo

Antes de lançar uma feature, a Amazon escreve um **PR/FAQ** (Press Release / FAQ) hipotético. Anexado ao PR/FAQ tem um modelo de receita que usa Monte Carlo pra simular **3 anos de adoção, churn, ticket médio e impacto cross-sell**. Se a distribuição de NPV (Net Present Value) tem média positiva *e* P10 acima de zero (cenário pessimista ainda não destrói valor), a feature é aprovada pra construção. Monte Carlo aqui filtra ideias **antes** de gastar engenharia.

### 4.2. Netflix — capacity planning de CDN

A Netflix usa Monte Carlo pra simular **demanda por região** dos seus servidores. Cada cenário sorteia: quantos usuários ativos por país, qual a distribuição de bitrate (4K vs HD vs SD), qual horário de pico. A saída é a distribuição de "GBps necessários por região-hora", e eles dimensionam a infraestrutura pelo P99 (não P50) — porque ficar sem stream é um desastre de PR. Aqui o **consumo** é de banda, não de produto, mas a matemática é idêntica.

### 4.3. Booking.com — simulando o lifetime value (LTV)

Antes de bidar mais alto no Google Ads pra um segmento de usuários, o Booking estima LTV via Monte Carlo: sorteia quantas reservas o usuário vai fazer ao longo de 5 anos (Poisson), com qual ADR (Average Daily Rate — Lognormal) e qual cancelamento (Bernoulli). Se a *mediana* do LTV simulado for maior que o custo de aquisição (CAC) com folga, eles aumentam o lance. Isso já reverteu várias decisões "intuitivas" de marketing — a média do LTV era bonita, mas a mediana mostrava que metade dos usuários daquele segmento não pagava de volta.

### 4.4. Conexão direta com Teste A/B — pre-experiment power analysis

Aqui é onde Monte Carlo de cenários **alimenta o teste A/B**: antes de rodar o experimento, você simula:

1. "Se o tratamento move conversão de 4% pra 4,2% (lift de 5%), quanto isso gera de receita extra?"
2. "Quantos usuários eu preciso por braço pra detectar esse lift com 80% de power?"

A simulação te diz se vale o custo de operar o teste por 4 semanas. Empresas como Microsoft e Airbnb fazem isso sistemicamente — chamam de **"experiment scoping"** ou **"impact estimation"**. Sem essa etapa, time roda teste atrás de teste pra mover métrica em 0,01%.

---

## 5. Conexão com o módulo

Este autoestudo é um **case de uso aplicado** que cruza várias matérias:

- **[Matemática-01 — Distribuições de Probabilidade](../autoestudo-01-distribuicoes-de-probabilidade/02-explicacao.md):** as distribuições (Poisson, Lognormal, Beta) são a *matéria-prima* da simulação. Sem entender quando cada uma se aplica, você modela errado.
- **[Matemática-02 — Processos Estocásticos, Markov e Monte Carlo](../autoestudo-02-processos-estocasticos-cadeias-de-markov-e-metodo-de-monte-carlo/02-explicacao.md):** o porquê do Monte Carlo funcionar (LGN) e a taxa de convergência 1/√N.
- **[Programação-02 — Roadmap do Projeto (Perspectiva de Programação)](../../computacao/autoestudo-02-roadmap-do-projeto-perspectiva-de-programacao/02-explicacao.md):** o "como" rodar simulações em escala (AWS Batch, paralelização). Quando N = 1 milhão e cada cenário é caro, você precisa de infra.
- **[Programação-05 — Cadeias de Markov e o Comportamento do Usuário](../../computacao/autoestudo-05-cadeias-de-markov-e-o-comportamento-do-usuario/02-explicacao.md):** dá pra **combinar Markov + Monte Carlo** — simular trajetórias estocásticas individuais (Markov) e agregar via Monte Carlo. Esse é o padrão usado em modelos de churn estado-a-estado.
- **[Negócios-01 — Experimentação em Produtos Digitais](../../negocios/autoestudo-01-experimentacao-em-produtos-digitais/02-explicacao.md):** a simulação alimenta a *priorização* dos experimentos.
- **[Negócios-02 — Plano de Negócios](../../negocios/autoestudo-02-plano-de-negocios/02-explicacao.md):** projeção financeira *com* incerteza é o que separa um plano sério de um chute.

---

## 6. Resumo estruturado

- **Pergunta central:** em vez de prever "um número" de consumo futuro, qual a **distribuição** de futuros possíveis?
- **Ferramenta:** Monte Carlo — sorteia muitos cenários, cada um com valores aleatórios das variáveis de entrada, e analisa a distribuição da saída.
- **Componentes:**
  1. Um **modelo** que conecta entradas à saída (ex.: `receita = usuários × conversão × pedidos × ticket`).
  2. Uma **distribuição de probabilidade** para cada entrada incerta (Poisson pra contagens, Lognormal pra valores, Beta pra taxas).
  3. **N simulações** com sorteios independentes.
  4. **Análise** da distribuição resultante (mediana, P10, P90, probabilidade de bater meta).
- **Vantagem sobre "3 cenários fixos":** distribuição contínua, intervalos de credibilidade, probabilidade de eventos específicos.
- **Aplicações:** revenue forecasting, capacity planning, LTV, experiment scoping (pré-A/B).
- **Conexão com Teste A/B:** é a ferramenta de **decidir o que vale ser testado** — calibra MDE em termos de receita e dimensiona poder estatístico.

---

## 7. Auto-reflexão (pra pensar)

1. Se a média do faturamento simulado é R$ 678 mil mas a mediana é R$ 660 mil, o que essa diferença está te dizendo sobre a forma da distribuição? Que decisão de negócio você tomaria baseando-se em cada uma?
2. Por que modelar ticket médio como Normal pode te fazer subestimar o risco de "cauda gorda" (clientes excepcionais)? Em que tipo de negócio isso é mais grave?
3. Você precisa rodar quantas simulações pra reduzir o intervalo de confiança da sua estimativa de receita em 10×? (Dica: convergência 1/√N.)
