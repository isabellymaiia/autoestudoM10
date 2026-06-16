# Processos Estocásticos (Cadeias de Markov & Método de Monte Carlo) — Material

> **Matéria:** Matemática · **Autoestudo:** 02 · **Data:** 11/05/2026 · **Professor:** Diogo Martins Gonçalves de Morais (Eixo MTF)
>
> ⚠️ **Material original não fornecido.** Os autoestudos referenciados são dois vídeos ("Processos Estocásticos 1" e "Processos Estocásticos 2"). Como as transcrições não foram disponibilizadas, o que segue é uma **reconstrução temática** do conteúdo padrão desses tópicos — **não é transcrição literal**. Substituir por versão fiel quando o material estiver disponível.

## Fontes referenciadas

1. **Vídeo: Processos Estocásticos 1** (sem transcrição)
2. **Vídeo: Processos Estocásticos 2** (sem transcrição)

---

## Resumo reconstruído — Vídeo 1: Processos Estocásticos (fundamentos)

> Reconstrução temática (não literal).

- Um **processo estocástico (stochastic process)** é uma **coleção de variáveis aleatórias indexadas por um parâmetro**, geralmente o tempo — notação `{X_t}`. Em palavras: é um fenômeno aleatório que **evolui ao longo do tempo**.
- Contraste com o **determinístico**: num processo determinístico, conhecido o estado inicial, todo o futuro está fixado (ex.: a trajetória de um projétil sem vento). Num processo estocástico, o futuro envolve **aleatoriedade** — só podemos falar de probabilidades.
- Dois ingredientes definem um processo:
  - **Espaço de estados (state space):** os valores possíveis que o processo pode assumir (podem ser **discretos** — ex.: número de clientes na fila — ou **contínuos** — ex.: o preço de uma ação).
  - **Conjunto de índices / tempo (index set):** quando observamos o processo (pode ser **tempo discreto** — passos 1, 2, 3… — ou **tempo contínuo** — qualquer instante).
- Combinando, há **quatro tipos** de processo (estado discreto/contínuo × tempo discreto/contínuo).
- Exemplos clássicos: **passeio aleatório (random walk)**, **processo de Poisson** (contagem de eventos no tempo), **movimento browniano (Brownian motion)** (estado e tempo contínuos).

---

## Resumo reconstruído — Vídeo 2: Cadeias de Markov & Método de Monte Carlo

> Reconstrução temática (não literal).

### Cadeias de Markov (como processo estocástico)

- Uma **Cadeia de Markov** é um **processo estocástico de tempo discreto e espaço de estados discreto** que satisfaz a **propriedade de Markov**: o estado futuro depende **apenas do estado presente**, não de toda a trajetória passada.
- Formalmente: `P(X_{n+1} = j | X_n = i, X_{n-1}, …, X_0) = P(X_{n+1} = j | X_n = i)`.
- Descrita pela **matriz de transição** (probabilidades de ir de cada estado a cada outro; linhas somam 1) e pelo **vetor de estado inicial**.
- Conceitos de longo prazo: **distribuição estacionária** (equilíbrio independente do início) e **ergodicidade**.

### Método de Monte Carlo

- O **Método de Monte Carlo** é uma técnica numérica que usa **amostragem aleatória repetida** para estimar quantidades difíceis de calcular analiticamente (integrais, áreas, probabilidades, valores esperados).
- Fundamento teórico: a **Lei dos Grandes Números (Law of Large Numbers)** — a média de muitas amostras aleatórias converge para o valor esperado verdadeiro.
- Procedimento geral: (1) gerar muitas amostras aleatórias de uma distribuição; (2) calcular a quantidade de interesse em cada amostra; (3) tirar a média/estatística sobre todas.
- **Precisão** melhora com o número de simulações `N`, mas a taxa de convergência do erro é da ordem de **1/√N** (para reduzir o erro pela metade, precisa de ~4× mais simulações).
- Exemplo didático típico: **estimar π** lançando pontos aleatórios num quadrado com um círculo inscrito e contando a fração que cai dentro do círculo.
- Inventado por **von Neumann e Ulam** (anos 1940), nomeado em referência ao cassino de Monte Carlo.

### A ponte: Markov Chain Monte Carlo (MCMC)

- A combinação dos dois temas dá origem ao **MCMC (Markov Chain Monte Carlo)** — uma família de algoritmos que usa cadeias de Markov projetadas para que sua distribuição estacionária seja a distribuição que queremos amostrar. Base de muita estatística bayesiana moderna.
