# Monte Carlo para a Simulação de Cenários de Consumo — Material

> **Matéria:** Matemática · **Autoestudo:** 03 · **Data:** 22/05/2026 · **Horário:** 10:00h
>
> ⚠️ **Material original não fornecido.** O autoestudo veio apenas com o título e a data, com a instrução de "colocar o que sei e criar o conteúdo". O que segue é uma **reconstrução temática** do conteúdo padrão deste tópico, ancorada no que já foi visto no módulo (especialmente [Matemática-02](../autoestudo-02-processos-estocasticos-cadeias-de-markov-e-metodo-de-monte-carlo/02-explicacao.md), [Programação-02](../../computacao/autoestudo-02-roadmap-do-projeto-perspectiva-de-programacao/02-explicacao.md) e [Programação-05](../../computacao/autoestudo-05-cadeias-de-markov-e-o-comportamento-do-usuario/02-explicacao.md)). Substituir por versão fiel quando o material estiver disponível.

## Tópicos esperados

1. **Recapitulação:** o que é o Método de Monte Carlo e por que ele funciona (Lei dos Grandes Números).
2. **Simulação de cenários (scenario simulation):** uso do Monte Carlo para construir distribuições de resultados futuros a partir de variáveis de entrada incertas.
3. **Modelagem de consumo:** como representar matematicamente o comportamento de consumo de uma população (quantidade, frequência, ticket médio).
4. **Distribuições típicas** usadas para modelar consumo:
   - **Poisson** — para *contagem* de eventos (quantos pedidos por usuário num mês).
   - **Lognormal / Gamma** — para *valores monetários* (ticket por compra), pela cauda à direita.
   - **Bernoulli / Binomial** — para *eventos binários* (converteu / não converteu).
   - **Exponencial / Weibull** — para *tempo entre eventos* (tempo até churn, tempo entre pedidos).
5. **Cenários:** base case, optimistic, pessimistic, e a distribuição *completa* gerada pela simulação.
6. **Aplicações práticas:**
   - Previsão de receita (revenue forecasting) com incerteza.
   - Simulação de impacto financeiro de um teste A/B antes do lançamento.
   - Análise de dimensionamento de estoque, capacity planning, churn projection.

## Conexão esperada com o módulo

- **Programação-05 (Cadeias de Markov e o Comportamento do Usuário)** — combinar Markov para *trajetórias* + Monte Carlo para *amostragem em massa*.
- **Negócios-01 (Experimentação em Produtos Digitais)** — a simulação alimenta o business case que justifica rodar (ou não) um teste A/B.
- **Negócios-02 (Plano de Negócios)** — projeções financeiras com distribuição de cenários.

## Status

> Conteúdo desenvolvido na explicação ([`02-explicacao.md`](02-explicacao.md)).
