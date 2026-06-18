# Análise de Sensibilidade com Machine Learning — Material

> **Matéria:** Matemática · **Autoestudo:** 05 · **Data:** 26/05/2026 · **Horário:** 10:00h

O autoestudo foi composto por **três fontes** que se complementam:

1. **Vídeo:** *Sensitivity analysis* — The Finance Storyteller (exemplos Shell e Glencore).
2. **Artigo Wikipedia:** *Variável de confusão* (confounding variable).
3. **Vídeo (aula):** *Análise de Sensibilidade com Simulação Monte Carlo* — modelo de qualidade da água (Streeter-Phelps).

---

## Fonte 1 — Transcrição: *Sensitivity analysis* (The Finance Storyteller)

> Transcrição do vídeo: *Sensitivity analysis*. Canal: The Finance Storyteller.

### Exemplo do mundo real: Shell e o preço do petróleo

O exemplo mais claro de análise de sensibilidade que já vi é o da empresa de óleo e gás **Shell** sobre o impacto de mudanças no preço do petróleo.

A sensibilidade ao preço no nível do grupo Shell é de **US$ 6 bilhões de cash flow from operations** por ano, **por movimento de US$ 10/barril** no preço do petróleo Brent.

- Se o preço sobe US$ 10/barril → esperam **+US$ 6 bilhões** de cash flow incremental.
- Se o preço cai US$ 10/barril → esperam **−US$ 6 bilhões**.

Essa declaração de sensibilidade vem com um disclaimer: ela é apropriada para mudanças pequenas de preço e é melhor usada para números de ano fechado.

> **Formato dessa análise:** efeito de uma mudança em **termos absolutos** de uma variável de entrada (preço do petróleo) sobre o **valor absoluto** de uma variável-alvo (cash flow from operations).

### Análise de sensibilidade em impairment testing (Glencore)

A empresa de mineração e trading **Glencore** apresenta no relatório anual uma análise de sensibilidade para cada cash generating unit com pouco *headroom* em relação ao valor recuperável.

- **Coal South Africa:** queda de **10%** no preço do carvão levaria a uma possível impairment de **US$ 703 milhões**.
- **Mopani:** queda de 10% no preço do cobre → impairment de US$ 181 milhões. Queda de 10% na produção anual estimada ao longo da vida da mina → impairment de US$ 116 milhões.

Análises similares são feitas para níquel, óleo e zinco.

> **Formato dessa análise:** efeito de uma mudança **em termos percentuais** de uma variável de entrada (10%) sobre o **valor absoluto** de uma variável-alvo (milhões de US$ de impairment).

### Definição de análise de sensibilidade

Esses exemplos levam à definição: **análise de sensibilidade é o processo de estimar como variáveis-alvo mudam em relação a mudanças em variáveis de entrada**.

- Efeito de uma mudança na variável `x` sobre `f(x)`?
- Efeito de uma mudança no preço do petróleo sobre o cash flow das operações?
- Efeito de uma mudança na receita sobre a lucratividade?
- Efeito de uma mudança nos benefícios estimados de um projeto sobre o NPV?

A chave é **identificar as premissas mais significativas** que afetam um output — quais variáveis de entrada têm o impacto mais forte sobre as variáveis-alvo.

### Defina KPIs antes da análise de sensibilidade

Antes de começar uma análise de sensibilidade, você precisa decidir quais são os **key performance indicators (KPIs)** — as variáveis-alvo.

### Sensibilidade de demonstrativos financeiros

Caso base, à esquerda. DRE projetada:

- Receita: US$ 1.000K
- Custos variáveis: US$ 600K
- Margem de contribuição: US$ 400K
- Custos fixos: US$ 200K
- **Margem operacional: US$ 200K**

A empresa espera vender **100 mil unidades a US$ 10 cada**.

Pergunta: efeito de uma queda de 10% na receita sobre a margem operacional?

> **Pergunta errada.** Nem toda mudança em receita tem o mesmo efeito sobre a margem operacional.

Há duas formas de cair 10% em receita:

| Cenário | Volume | Preço | Receita | Custo variável | Margem contrib. | Custo fixo | **Margem operacional** |
|---|---|---|---|---|---|---|---|
| Base | 100K | $10 | $1.000K | $600K | $400K | $200K | **$200K** |
| 10% volume ↓ | 90K | $10 | $900K | $540K | $360K | $200K | **$160K** (−20%) |
| 10% preço ↓ | 100K | $9 | $900K | $600K | $300K | $200K | **$100K** (−50%) |
| 10% ambos ↓ | 90K | $9 | $810K | $540K | $270K | $200K | **$70K** (−65%) |

**Lições:**

- Queda de 10% no **volume** → queda de **20%** na margem operacional.
- Queda de 10% no **preço** → queda de **50%** na margem operacional.
- **Tema muito mais a queda de preço do que a queda de volume.**

### Análise de um fator vs múltiplos fatores

O que foi feito acima é **"one assumption at a time" (OAT/OFAT)** — variar uma entrada por vez, mantendo as outras fixas. Na vida real, muitas premissas estão **ligadas** e se movem ao mesmo tempo, na mesma direção ou em direções opostas.

Se volume **e** preço caem 10% simultaneamente: receita = US$ 810K, custos variáveis = US$ 540K, margem operacional = US$ 70K — **queda de 65%** vs. base.

### Sensibilidade linear

Muitos analistas erram assumindo que entradas e saídas estão ligadas **linearmente** — que uma mudança de 20% nas entradas teria o dobro do efeito de uma mudança de 10%.

### Convexidade e concavidade

Os impactos podem ser **exponenciais**, não lineares:

- **Convexidade** (cenário positivo): crescimento exponencial da variável-alvo. **Procure por isso e se beneficie.**
- **Concavidade** (cenário negativo): declínio exponencial. **Evite e construa defesas** pra não "explodir".

> **Nassim Taleb:** *fazer análise de sensibilidade nas premissas não elimina o risco, mas identifica quais premissas são chave para as conclusões e, portanto, merecem escrutínio mais cuidadoso.*

---

## Fonte 2 — Artigo Wikipedia: *Variável de confusão*

> Resumo do artigo. Fonte: Wikipedia (PT-BR).

Em estatística, uma **variável de confusão** (confounder, confounding variable) é uma variável que influencia **tanto a variável dependente quanto a variável independente**, causando uma **associação espúria**. É um conceito **causal** e não pode ser descrito em termos apenas de correlações ou associações.

### Definição

Considere `X` (independente) e `Y` (dependente). Para estimar o efeito de `X` sobre `Y`, é preciso suprimir efeitos de variáveis estranhas que influenciam ambos. Dizemos que `X` e `Y` são confundidas por `Z` sempre que `Z` é causa tanto de `X` quanto de `Y`.

Formalmente, `X` e `Y` **não são confundidas** se e somente se:

```
P(y | do(x)) = P(y | x)
```

para todos os valores `X=x`, `Y=y`. A igualdade afirma que a associação observada é igual ao que seria medido em um experimento controlado, com `x` randomizado. (`do(x)` é a notação de Pearl para intervenção.)

### Exemplo do controle (droga)

Estudo da efetividade de uma droga `X` em uma população onde o uso da droga foi escolha do paciente. O **gênero** (`Z`) do paciente influencia:

- A escolha da droga.
- A chance de recuperação.

Logo, `Z` (gênero) confunde a relação entre `X` (droga) e `Y` (recuperação). A **fórmula de ajuste** (backdoor):

```
P(y | do(x)) = Σ_z P(y | x, z) P(z)
```

dá uma estimativa **não enviesada** do efeito causal de `X` sobre `Y`.

### Critério da porta dos fundos (backdoor)

O conjunto `Z` de variáveis a ajustar deve **bloquear todo caminho de `X` a `Y` que termina com uma seta para `X`**. Adicionar covariáveis erradas ao ajuste pode **introduzir viés** (viés do colisor / paradoxo de Berkson).

### Exemplo da ordem de nascimento × síndrome de Down

Idade materna confunde: ela está associada tanto à ordem de nascimento (filhos mais velhos vs mais novos) quanto à incidência de síndrome de Down. Sem controlar idade materna, a associação aparente entre ordem de nascimento e síndrome de Down é espúria.

### Como mitigar confusão

- **Estudos caso-controle:** parear casos e controles em variáveis suspeitas (idade, sexo).
- **Restrição/coorte:** estudar apenas um subgrupo homogêneo (ex.: só homens entre 40 e 50 anos).
- **Duplo-cego:** esconder o grupo dos participantes e observadores para neutralizar efeito placebo e viés do observador.
- **Randomização (RCT):** distribuir aleatoriamente os participantes — distribui confounders conhecidos *e desconhecidos* entre os grupos por sorteio.
- **Estratificação:** analisar a associação dentro de cada estrato (ex.: grupo etário).
- **Análise multivariada:** controlar como covariáveis em regressão.

> **Defesa principal:** randomização (RCT) em amostra grande — distribui confounders *desconhecidos*, que nenhum dos outros métodos consegue tratar.

### Tipos

- **Confusão por indicação** (epidemiologia): em estudos observacionais, fatores prognósticos influenciam decisão de tratamento e enviesam estimativas. RCTs são imunes.
- **Confusão operacional** / **procedimental** / **pessoal** — pela fonte (instrumento, situação, diferenças interindividuais).

---

## Fonte 3 — Transcrição: Aula sobre *Análise de Sensibilidade com Simulação Monte Carlo*

> Transcrição (limpa) de aula que aplica análise de sensibilidade via Monte Carlo ao **modelo de qualidade da água Streeter-Phelps** (concentração de oxigênio dissolvido após lançamento de efluente em um rio). O conteúdo é totalmente genérico e transferível para qualquer modelo com parâmetros incertos.

### Contexto: modelagem e tomada de decisão

- Modelos são **representações abstratas e simplificadas da realidade**. Mesmo assim, ajudam a melhorar compreensão de sistemas naturais, ecológicos ou industriais.
- A tarefa do modelador é transformar conceitos e fenômenos em **equações matemáticas**.
- Um sistema é uma estrutura que **inter-relaciona entradas (causa/estímulo) e saídas (efeito/resposta)** ao longo do tempo ou do espaço. As entradas podem ser matéria, energia ou informação.
- As **leis físicas** que descrevem essas relações (Conservação de massa, energia, quantidade de movimento) já vêm com incerteza, e o processo de medição/coleta de dados também.

### Variáveis e parâmetros

- **Variável:** valor que descreve quantitativamente um fenômeno (ex.: altura pluviométrica, taxa de infiltração).
- **Parâmetro:** valor que **caracteriza o sistema** e pode variar no espaço/tempo (ex.: rugosidade de uma seção de rio, área de uma bacia, `k₁` e `k₂` no Streeter-Phelps).
- **Variável de estado:** descreve o estado do sistema (ex.: umidade do solo, concentração de OD).

### Modelo Streeter-Phelps (revisão)

- Modela o balanço **DBO ↔ OD** após lançamento de efluente em um rio.
- Após o lançamento, microrganismos consomem OD para degradar matéria orgânica → OD cai (desoxigenação, parâmetro `k₁`).
- A reaeração (entrada de O₂ atmosférico) recupera o OD (parâmetro `k₂`).
- A concentração de OD é a **variável de estado** de interesse.
- A concentração crítica não pode ser menor que **5 mg/L** (legislação para rio classe 2).

### Etapas da modelagem

1. **Objetivos**
2. **Concepção** — como o fenômeno ocorre (ex.: balanço consumo/relação no modelo Streeter-Phelps).
3. **Modelo matemático** — equações diferenciais.
4. **Representação computacional** — Excel, MATLAB, R, Python.
5. **Calibração** — ajustar `k₁` e `k₂` para minimizar erro entre simulado e observado.
6. **Verificação** — análise dos erros do modelo.
7. **Validação** — usar segunda parcela dos dados observados para validar o modelo calibrado.
8. **Análise de sensibilidade** — verificar quanto uma alteração nos parâmetros varia a saída.

### Análise de resíduos (verificação)

Pressupostos:

1. **Média dos erros ≈ 0.**
2. **Variância dos erros constante** (homocedasticidade — heterocedasticidade indica que o modelo precisa ser ajustado, e.g., transformação log de `y`).
3. **Distribuição dos erros normal** — teste de Shapiro, Kolmogorov-Smirnov, etc.
4. **Independência:** os erros associados a observações diferentes devem ser independentes.
5. **Sem autocorrelação:** o erro em um ponto não deve estar correlacionado com erros em pontos anteriores/posteriores.

### Principais fontes de incerteza na modelagem

- **Na coleta de dados:** redução de dados pontuais em médias espaciais/temporais, erro em medição indireta.
- **Na estrutura do modelo:** conhecimento limitado dos processos, aproximações, simplificações, tratamento espacialmente concentrado, tratamento sequencial de processos concomitantes.
- **Na calibração:** subjetividade do processo de tentativa-e-erro, escolha da função objetivo (R², RMSE, etc., podem dar resultados diferentes), mínimos locais.

### Simulação Monte Carlo aplicada

Em vez de tratar variáveis e parâmetros como **valores determinísticos**, atribuímos a cada um uma **distribuição de probabilidade** (uniforme, normal, etc.). Para cada rodada:

1. Sorteia-se um valor de cada distribuição.
2. Roda-se o modelo.
3. Salva-se a saída.

Repete-se centenas/milhares de vezes (ex.: **1.000 rodadas**). A saída deixa de ser uma curva única e passa a ser uma **nuvem de curvas** (a faixa de incerteza).

### Geração de valores aleatórios

- **Distribuição uniforme:** `valor = mínimo + ALEATÓRIO() × (máximo − mínimo)`.
- A partir da média: `mínimo = média × (1 − % variação)` e `máximo = média × (1 + % variação)`.
- **Exemplo (DBO do esgoto):** se varia entre 250 e 350 mg/L, gere mil valores nesse intervalo, rode mil modelos.

### Análise da saída

- Histograma de frequência (e acumulada) dos valores de OD em cada distância.
- Probabilidade de a concentração crítica estar acima/abaixo de 5 mg/L (atende classe 2?).
- Mediana, percentis, faixa de operação típica do modelo.

### Análise de sensibilidade via Monte Carlo (regionalizada)

Procedimento:

1. **Reaproveite a nuvem de simulações Monte Carlo.**
2. **Divida os resultados em duas amostras** segundo um critério:
   - Atende à classe (≥ 5 mg/L) vs não atende.
   - Acima da mediana vs abaixo da mediana.
3. Para cada parâmetro de entrada, **compare a distribuição daquele parâmetro nos dois grupos**.
4. **Teste estatístico:**
   - Se a distribuição é conhecida → teste **t** (para amostras grandes, > 30).
   - Se a distribuição é desconhecida → teste não-paramétrico **Mann-Whitney**.
5. **Interpretação:**
   - Se as distribuições são **significativamente diferentes** → o parâmetro **é sensível** (controla o output).
   - Se são **similares** → o parâmetro **não é sensível** (pequenas variações nele não mudam o output).

### Visualização: box-plots e gráficos de dispersão

- **Box-plot** do parâmetro em cada grupo. Se as posições (mediana, quartis, mínimo, máximo) se sobrepõem → não sensível. Se diferem → sensível.
- **Gráfico de dispersão** entre parâmetro de entrada e saída do modelo.

### Resultado obtido na aula

- **`k₁` (desoxigenação):** sensibilidade **baixa** — distribuições dos dois grupos quase coincidem.
- **`k₂` (reaeração):** sensibilidade **alta** — distribuições dos dois grupos diferem substancialmente. A mediana do grupo 1 está em ~7,65 vs ~3,04 no grupo 2.

**Conclusão prática:** esforço de aquisição de dados e calibração deve se concentrar em `k₂`, não `k₁`. Análise de sensibilidade orienta **onde gastar tempo** modelando.

### Mensagem-síntese da aula

> Uma pequena variação na entrada que causa grande variação na saída → **parâmetro sensível** — concentre esforços de medição/calibração nele.
> Uma pequena variação na entrada que causa pequena variação na saída → **parâmetro insensível** — pode até ser simplificado/removido do modelo (princípio da parcimônia).

---

## Observação sobre o título

O título oficial do autoestudo é **"Análise de Sensibilidade com Machine Learning"**. O material fornecido **não menciona ML diretamente** — usa Monte Carlo + estatística clássica. A conexão com ML (que aparece na explicação em `02-explicacao.md`) é via **interpretabilidade de modelos** (SHAP, feature importance, ICE plots) — que são **a versão moderna, baseada em ML, da mesma ideia de OFAT/Sobol que o vídeo apresenta**.
