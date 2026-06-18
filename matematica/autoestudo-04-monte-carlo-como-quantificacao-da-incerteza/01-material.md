# Monte Carlo como Quantificação da Incerteza — Material

> **Matéria:** Matemática · **Autoestudo:** 04 · **Data:** 25/05/2026 · **Horário:** 10:00h
>
> ⚠️ **Material original não fornecido.** O autoestudo veio apenas com o título e a data, com a instrução de "colocar o que sei e criar o conteúdo". O que segue é uma **reconstrução temática** do conteúdo padrão deste tópico (Uncertainty Quantification — UQ), ancorada nos autoestudos anteriores do módulo. Substituir por versão fiel quando o material estiver disponível.

## Tópicos esperados

1. **O que é Quantificação da Incerteza (Uncertainty Quantification — UQ)** — o "ramo" da matemática aplicada que trata explicitamente da incerteza em modelos.
2. **Tipos de incerteza:**
   - **Aleatória (aleatory)** — variabilidade intrínseca, *irredutível* (ex.: lance de dado).
   - **Epistêmica (epistemic)** — falta de conhecimento, *redutível* coletando mais dados (ex.: você não sabe o parâmetro do modelo, mas poderia saber).
3. **Monte Carlo como ferramenta de UQ:** propagação de incerteza das entradas pra saída.
4. **Intervalos de confiança e credibilidade via Monte Carlo:**
   - Bootstrap (frequentista).
   - Posterior sampling (bayesiano).
5. **Conexão com Teste A/B:** intervalo de confiança do lift, p-value via simulação, robustez à premissa de normalidade.
6. **Casos típicos:** previsão de chuva (ensemble), Value at Risk (VaR), confiabilidade estrutural, planejamento experimental.

## Conexão esperada com o módulo

- **[Matemática-02](../autoestudo-02-processos-estocasticos-cadeias-de-markov-e-metodo-de-monte-carlo/02-explicacao.md):** fundamentação teórica do Monte Carlo (LGN, convergência 1/√N).
- **[Matemática-03](../autoestudo-03-monte-carlo-para-a-simulacao-de-cenarios-de-consumo/02-explicacao.md):** Monte Carlo aplicado a cenários — agora formalizamos a "incerteza" da saída.
- **[Programação-03 (Avaliação de Dados Sintéticos)](../../computacao/autoestudo-03-avaliacao-de-dados-sinteticos/02-explicacao.md):** sintéticos servem pra "rodar o experimento que ainda não rodou" — UQ via Monte Carlo é a teoria por trás.
- **[Programação-06 (Fundamentos de Programação de Testes A/B)](../../computacao/autoestudo-06-fundamentos-de-programacao-de-testes-ab/02-explicacao.md):** intervalos de confiança em A/B test são feitos via bootstrap em produção (Booking, Netflix).

## Status

> Conteúdo desenvolvido na explicação ([`02-explicacao.md`](02-explicacao.md)).
