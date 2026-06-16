# Avaliação de Dados Sintéticos — Material

> **Matéria:** Computação / Programação · **Autoestudo:** 03 · **Data:** 05/05/2026 · **Professor:** Jefferson de Oliveira Silva (Eixo COM)
>
> Fonte única: artigo *"Evaluating Synthetic Data — The Million Dollar Question"*, de Andrew Skabar, PhD (TDS Archive / Towards Data Science, 14/02/2024). Conteúdo limpo de navegação/rodapé e traduzido/estruturado, preservando a fidelidade ao original.

---

## Evaluating Synthetic Data — A pergunta de um milhão de dólares

> **Subtítulo:** *Meus datasets real e sintético são amostras aleatórias da mesma distribuição-mãe (parent distribution)?*

Quando geramos dados sintéticos, tipicamente criamos um **modelo** para os nossos dados reais (ou 'observados') e usamos esse modelo para gerar dados sintéticos. Esses dados observados normalmente são compilados de experiências do mundo real — medições de características físicas de flores de íris, detalhes sobre pessoas que deram calote em crédito, ou que adquiriram alguma condição médica.

Podemos pensar nos dados observados como tendo vindo de uma **'distribuição-mãe' (parent distribution)** — a verdadeira distribuição subjacente da qual os dados observados são uma **amostra aleatória (random sample)**. É claro que nunca conhecemos essa distribuição-mãe — ela precisa ser estimada, e esse é o propósito do nosso modelo.

Mas se o nosso modelo conseguir produzir dados sintéticos que possam ser considerados uma **amostra aleatória da mesma distribuição-mãe**, então acertamos na mosca (hit the jackpot):
- os dados sintéticos terão as mesmas propriedades estatísticas e padrões dos dados observados (**fidelidade / fidelity**);
- serão igualmente úteis em tarefas como regressão ou classificação (**utilidade / utility**);
- e, por serem uma amostra aleatória, não há risco de identificarem os dados observados (**privacidade / privacy**).

Mas como saber se atingimos esse objetivo elusivo?

---

## Parte 1 — Alguns experimentos simples

Considere dois datasets e tente responder:

> Os datasets são amostras aleatórias da mesma distribuição-mãe, ou um foi derivado do outro aplicando pequenas perturbações aleatórias?

Os datasets claramente exibem propriedades estatísticas similares, como distribuições marginais e covariâncias. Eles também teriam desempenho similar numa tarefa de classificação em que um classificador treinado num dataset é testado no outro.

Mas suponha que plotássemos os pontos de cada dataset no mesmo gráfico. Se os datasets são amostras aleatórias da mesma distribuição-mãe, esperaríamos intuitivamente que os pontos de um dataset estivessem **intercalados** com os do outro, de modo que, em média, os pontos de um conjunto estejam tão próximos (tão 'similares') dos seus vizinhos mais próximos no *mesmo* conjunto quanto estão dos seus vizinhos mais próximos no *outro* conjunto. Porém, se um dataset é uma leve perturbação aleatória do outro, então os pontos de um conjunto serão **mais similares** aos seus vizinhos mais próximos no *outro* conjunto do que aos seus vizinhos no *mesmo* conjunto. Isso leva ao teste a seguir.

### O Teste de Similaridade Máxima (Maximum Similarity Test)

Para cada dataset, calcule a similaridade entre cada instância e o seu vizinho mais próximo no **mesmo** dataset. Chame essas de **'similaridades intra-conjunto máximas' (maximum intra-set similarities)**. Se os datasets têm as mesmas características distribucionais, a distribuição das similaridades intra-conjunto deve ser similar para cada dataset.

Agora calcule a similaridade entre cada instância de um dataset e o seu vizinho mais próximo no **outro** dataset, e chame essas de **'similaridades cruzadas máximas' (maximum cross-set similarities)**. Se a distribuição das similaridades cruzadas máximas for igual à distribuição das similaridades intra-conjunto máximas, então os datasets podem ser considerados amostras aleatórias da mesma distribuição-mãe.

> Para o teste ser válido, cada dataset deve conter o **mesmo número de exemplos**.

Como os datasets aqui contêm uma mistura de variáveis numéricas e categóricas, precisamos de uma medida de similaridade que acomode isso. Usamos a **Similaridade de Gower (Gower Similarity)**¹.

**Resultado do experimento:** em média, as instâncias de um dataset eram mais similares aos seus vizinhos mais próximos no *outro* dataset do que aos seus vizinhos no *mesmo* dataset. Isso indica que os datasets são mais provavelmente **perturbações** um do outro do que amostras aleatórias da mesma distribuição-mãe. E de fato eram perturbações: o Dataset 1 foi gerado de um modelo de mistura de gaussianas (Gaussian mixture model); o Dataset 2 foi gerado selecionando (sem reposição) uma instância do Dataset 1 e aplicando uma pequena perturbação aleatória.

> O maior perigo de pontos sintéticos estarem perto demais dos observados é a **privacidade** — ou seja, conseguir identificar pontos do conjunto observado a partir do conjunto sintético. Isso aconteceu mesmo num caso em que a similaridade cruzada máxima média era apenas **0,3% maior** que a similaridade intra-conjunto máxima média!

### Modelando e sintetizando

Ao criar um modelo para o Dataset 1 (estimado como uma mistura de gaussianas) e gerar um dataset sintético (Dataset 3), os resultados foram: as três médias idênticas até três algarismos significativos, e os três histogramas muito similares. Portanto, segundo o Teste de Similaridade Máxima, ambos podem ser razoavelmente considerados amostras aleatórias da mesma distribuição-mãe. O exercício de geração foi um sucesso, alcançando a **trinca (trifecta): fidelidade, utilidade e privacidade.**

> [O código Python usado na Parte 1 está disponível em https://github.com/a-skabar/TDS-EvalSynthData]

---

## Parte 2 — Datasets reais, geradores reais

O dataset da Parte 1 é simples e modelável com uma mistura de gaussianas. A maioria dos datasets do mundo real é muito mais complexa. Aqui, vários geradores de dados sintéticos são aplicados a datasets reais populares, comparando as distribuições de similaridades máximas dentro e entre os conjuntos observado e sintético.

**Os seis datasets** vêm do **repositório UCI**² e são clássicos da literatura de machine learning. Todos são de **tipo misto** (categóricas + numéricas), escolhidos por variarem no equilíbrio entre features categóricas e numéricas.

**Os seis geradores** representam as principais abordagens:
- **CopulaGAN**³, **GaussianCopula**, **CTGAN**³ e **TVAE**³ — das bibliotecas do **Synthetic Data Vault (SDV)**⁴;
- **synthpop**⁵ — pacote open-source em R;
- **UNCRi** — ferramenta proprietária do framework *Unified Numeric/Categorical Representation and Inference*⁶.

Todos usados com configurações padrão.

### Métricas e o teste TSTR

A tabela de resultados mostra as similaridades intra- e cruzadas máximas médias de cada gerador em cada dataset:
- Entradas em **vermelho:** privacidade comprometida (similaridade cruzada máxima média **excede** a similaridade intra-conjunto máxima média nos dados observados).
- Entradas em **verde:** a maior similaridade cruzada máxima média (excluindo as vermelhas).
- Última coluna: o resultado do teste **TSTR — Train on Synthetic, Test on Real (Treinar no Sintético, Testar no Real)**: um classificador ou regressor é treinado nos exemplos sintéticos e testado nos exemplos reais (observados). Para o Boston Housing (regressão), reporta-se o **MAE (mean absolute error)**; para os demais (classificação), reporta-se a **AUC (area under ROC curve)**.

**Achados principais:**
- Para os geradores que **não** violaram privacidade, a similaridade cruzada máxima média ficou muito próxima da intra-conjunto máxima média nos dados observados — e as distribuições (histogramas) eram claramente similares (de forma marcante no Census Income).
- O gerador com a maior similaridade cruzada máxima média em cada dataset (excluindo os vermelhos) também teve o **melhor desempenho no TSTR**. Ou seja: embora nunca se possa afirmar ter descoberto a 'verdadeira' distribuição subjacente, o gerador mais eficaz para cada dataset capturou as features cruciais dessa distribuição.

### Privacidade

Apenas dois dos geradores tiveram problemas de privacidade: **synthpop** e **TVAE**, cada um violando em 3 dos 6 datasets. Em dois casos (TVAE no Cleveland Heart Disease e TVAE no Credit Approval), a violação foi particularmente severa: os exemplos sintéticos ficaram **similares demais entre si** e dos seus vizinhos nos dados observados — uma representação ruim da distribuição-mãe. A causa provável: o Credit Approval contém várias features numéricas extremamente assimétricas (highly skewed).

### Outras observações

- Os dois geradores **baseados em GAN** — CopulaGAN e CTGAN — estiveram consistentemente entre os **piores**, o que surpreende dada a popularidade das GANs.
- O **GaussianCopula** teve desempenho medíocre em quase todos, exceto no Wisconsin Breast Cancer. Seu desempenho fraco no Iris (dataset simples, modelável por mistura de gaussianas) foi especialmente surpreendente.
- Os geradores **mais consistentes** foram **synthpop** e **UNCRi**, ambos operando por **imputação sequencial (sequential imputation)**: só precisam estimar e amostrar de uma **distribuição condicional univariada** (ex.: P(x₇ | x₁, x₂, …)), o que é tipicamente muito mais fácil do que modelar e amostrar de uma distribuição multivariada (ex.: P(x₁, x₂, x₃, …)) — que é, implicitamente, o que GANs e VAEs fazem. O synthpop estima distribuições com árvores de decisão (fonte do overfitting a que é propenso); o UNCRi usa uma abordagem baseada em vizinhos mais próximos, com hiperparâmetros otimizados por validação cruzada que previne overfitting.

---

## Conclusão

A geração de dados sintéticos é um campo novo e em evolução, e ainda não há técnicas de avaliação padrão — mas há consenso de que os testes devem cobrir **fidelidade, utilidade e privacidade**. Porém, embora todas sejam importantes, **elas não estão em pé de igualdade**.

Por exemplo, um dataset sintético pode ir bem em fidelidade e utilidade mas falhar em privacidade. Isso **não** lhe dá um "dois de três": se os exemplos sintéticos estão perto demais dos observados (falhando no teste de privacidade), o modelo sofreu **overfitting (sobreajuste)**, tornando os testes de fidelidade e utilidade **sem sentido**. Há uma tendência de alguns fornecedores proporem medidas de pontuação única que combinam múltiplos testes — algo baseado na mesma lógica equivocada do "dois de três".

Se um dataset sintético pode ser considerado uma **amostra aleatória da mesma distribuição-mãe** que os dados observados, então não há como fazer melhor — atingimos o máximo de fidelidade, utilidade e privacidade. O **Teste de Similaridade Máxima** mede o quanto dois datasets podem ser considerados amostras aleatórias da mesma distribuição-mãe, baseado na noção simples e intuitiva: se observado e sintético são amostras da mesma distribuição-mãe, uma instância sintética deve ser, em média, tão similar ao seu vizinho observado mais próximo quanto uma instância observada é similar ao seu vizinho observado mais próximo.

### Medida de pontuação única proposta

> **Razão = (similaridade cruzada máxima média) / (similaridade intra-conjunto máxima média nos dados observados)**
>
> Quanto mais perto de **1 — sem exceder 1 —** melhor a qualidade do dado sintético. (Exceder 1 indica violação de privacidade / overfitting.) Deve, é claro, ser acompanhada por uma checagem de sanidade dos histogramas.

---

## Referências

1. Gower, J. C. (1971). *A general coefficient of similarity and some of its properties.* Biometrics, 27(4), 857–871.
2. Dua, D. & Graff, C. (2017). *UCI Machine Learning Repository.* http://archive.ics.uci.edu/ml
3. Xu, L., Skoularidou, M., Cuesta-Infante, A. and Veeramachaneni, K. *Modeling Tabular data using Conditional GAN.* NeurIPS, 2019.
4. Patki, N., Wedge, R., & Veeramachaneni, K. (2016). *The synthetic data vault.* IEEE DSAA (pp. 399–410).
5. Nowok, B., Raab G.M., Dibben, C. (2016). *synthpop: Bespoke Creation of Synthetic Data in R.* Journal of Statistical Software, 74(11).
6. UNCRi framework — http://skanalytix.com/uncri-framework
7. Harrison, D., & Rubinfeld, D.L. (1978). *Boston Housing Dataset.*
8. Kohavi, R. (1996). *Census Income.* UCI ML Repository.
9. Janosi, A. et al. (1988). *Heart Disease.* UCI ML Repository.
10. Quinlan, J.R. (1987). *Credit Approval.* UCI ML Repository.
11. Fisher, R.A. (1988). *Iris.* UCI ML Repository.
12. Wolberg, W. et al. (1995). *Breast Cancer Wisconsin (Diagnostic).* UCI ML Repository.
