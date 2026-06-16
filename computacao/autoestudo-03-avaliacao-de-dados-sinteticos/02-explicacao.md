# Avaliação de Dados Sintéticos — Explicação

> **Matéria:** Computação / Programação · **Autoestudo:** 03 · **Data:** 05/05/2026 · **Professor:** Jefferson de Oliveira Silva
>
> Explicação detalhada do artigo de Andrew Skabar (ver [`01-material.md`](01-material.md)). Este autoestudo é a continuação direta do [Autoestudo 01 — Geração de Dados Sintéticos](../autoestudo-01-geracao-de-dados-sinteticos/02-explicacao.md): lá vimos *como gerar*, aqui vemos *como avaliar se o que foi gerado presta*.

---

## 1. Contexto geral: a "pergunta de um milhão de dólares"

No Prog-01, aprendemos a **gerar** dados sintéticos e vimos, de passagem, que a qualidade se mede em três dimensões: **fidelidade, utilidade e privacidade**. Mas ficou uma pergunta no ar: *na prática, como eu sei se o meu dado sintético é bom?* É exatamente isso que este autoestudo ataca — e o autor chama de "a pergunta de um milhão de dólares" porque, sem uma resposta confiável, você pode estar tomando decisões (ou vendendo um produto) baseado em dados sintéticos que parecem bons mas são lixo.

A grande sacada do artigo é **reduzir as três dimensões a uma única pergunta elegante**:

> **"O meu dataset real e o meu dataset sintético são amostras aleatórias da mesma distribuição-mãe?"**

Se a resposta for *sim*, você ganhou tudo de uma vez. Vamos entender por quê — mas antes, o conceito central.

### A analogia da receita de família

Imagine que sua avó faz um brigadeiro perfeito, mas nunca escreveu a receita — ela cozinha "no olho". Essa **receita mental dela é a "distribuição-mãe" (parent distribution)**: a verdadeira regra que gera os brigadeiros. Cada brigadeiro que ela faz é uma **amostra aleatória (random sample)** dessa receita — todos um pouco diferentes, mas todos "da mesma família".

Agora você quer reproduzir. Você prova vários brigadeiros dela e tenta **estimar** a receita (esse é o seu **modelo**). Aí você faz os seus brigadeiros (os **dados sintéticos**). A pergunta de ouro: *os seus brigadeiros são indistinguíveis dos dela — como se tivessem saído da mesma receita — ou são cópias decoradas de brigadeiros específicos que você provou?*

- Se forem "da mesma receita" → perfeito: têm o mesmo sabor (**fidelidade**), servem pra mesma festa (**utilidade**), e ninguém consegue dizer "esse aqui é a cópia exata daquele que a vovó fez terça-feira" (**privacidade**).
- Se você só **decorou e copiou** brigadeiros específicos → você "vazou" os originais (quebra de privacidade) e na verdade nem aprendeu a receita.

Esse segundo caso tem um nome técnico crucial: **overfitting (sobreajuste)** — o modelo decorou os exemplos em vez de aprender o padrão. Segura essa palavra, ela é o vilão da história.

---

## 2. Conceitos-chave

### 2.1. Distribuição-mãe (parent distribution) e amostra aleatória

- **Distribuição-mãe (parent distribution):** a verdadeira distribuição estatística subjacente que "gera" os dados do mundo real. **Nunca a conhecemos diretamente** — só vemos amostras dela.
- **Amostra aleatória (random sample):** um punhado de pontos sorteados dessa distribuição. Os seus dados observados (reais) são uma amostra aleatória da distribuição-mãe.
- **Modelo:** a nossa *estimativa* da distribuição-mãe, construída a partir dos dados observados.

A meta da geração de dados sintéticos, reformulada: fazer o modelo bom o suficiente para que os dados sintéticos que ele produz **pareçam mais uma amostra aleatória da mesma distribuição-mãe** — nem cópias dos originais, nem coisa de outra distribuição.

### 2.2. Por que "mesma distribuição-mãe" resolve as três dimensões de uma vez

Esse é o argumento mais bonito do artigo:

| Dimensão | O que exige | Por que "mesma distribuição-mãe" garante |
|---|---|---|
| **Fidelidade (fidelity)** | mesmas propriedades estatísticas e padrões | amostras da mesma distribuição têm, por definição, as mesmas estatísticas |
| **Utilidade (utility)** | servir igual para regressão/classificação | se as estatísticas são as mesmas, um modelo treinado num funciona no outro |
| **Privacidade (privacy)** | não dá pra identificar os reais | uma amostra *aleatória* não copia pontos específicos → nada a vazar |

Por isso, atingir "mesma distribuição-mãe" é o **teto**: não dá pra fazer melhor que isso.

### 2.3. A tensão fidelidade ↔ privacidade (e por que não é "2 de 3")

Aqui está o insight que mais separa um iniciante de alguém que entende o assunto.

Você poderia pensar: "se meu dado sintético é *idêntico* ao real, a fidelidade é perfeita!" **Errado** — porque se ele é idêntico, ele *é* o dado real, e você acabou de vazar tudo (privacidade zero). Existe uma **tensão fundamental**: quanto mais perto você chega de copiar os pontos reais, melhor a fidelidade *aparenta* ser, mas pior a privacidade fica.

O ponto-chave do artigo: **as três dimensões NÃO estão em pé de igualdade.** Se um dado sintético vai bem em fidelidade e utilidade mas falha em privacidade, isso **não** é "dois acertos de três". É **falha total** — porque a única forma de falhar privacidade é por **overfitting** (o modelo decorou os pontos), e um modelo que decorou não aprendeu a distribuição de verdade, o que torna a "boa fidelidade" e a "boa utilidade" **ilusões sem sentido**. O autor critica explicitamente os fornecedores que vendem uma "nota única" somando os três testes — é a mesma lógica furada do "2 de 3".

### 2.4. O Teste de Similaridade Máxima (Maximum Similarity Test)

Como medir se dois datasets vêm da mesma distribuição-mãe? O artigo propõe um teste **geometricamente intuitivo**. A ideia: comparar "quão perto cada ponto está do vizinho mais próximo".

Dois tipos de medida:
- **Similaridade intra-conjunto máxima (maximum intra-set similarity):** para cada ponto, quão parecido ele é do vizinho **mais próximo dentro do seu próprio conjunto**.
- **Similaridade cruzada máxima (maximum cross-set similarity):** para cada ponto de um conjunto, quão parecido ele é do vizinho **mais próximo no outro conjunto**.

A lógica do teste:

> Se os dois conjuntos vêm da mesma distribuição-mãe, os pontos ficam **intercalados/misturados**. Então, em média, um ponto está tão perto do vizinho no *outro* conjunto quanto do vizinho no *seu próprio* conjunto. → **intra ≈ cross.**
>
> Se um conjunto é uma **cópia perturbada** do outro (overfitting), cada ponto sintético tem um "gêmeo" quase idêntico no conjunto real. Então ele fica **mais perto** do vizinho no outro conjunto do que do vizinho no seu próprio. → **cross > intra.** 🚨 Alarme de privacidade.

**Analogia da festa:** imagine duas turmas (vermelha e preta) numa festa.
- Se todo mundo se misturou na pista, seu vizinho mais próximo é tão provavelmente da sua turma quanto da outra (intra ≈ cross) → "mesma população".
- Se cada pessoa de vermelho está colada num clone seu de preto (casais idênticos), então o vizinho mais próximo de cada um é sempre da outra turma (cross > intra) → as turmas não são populações independentes; uma copiou a outra.

> Detalhe impressionante do experimento: bastou a similaridade cruzada ser **0,3% maior** que a intra para já dar pra identificar pares — mostrando o quão sensível a privacidade é.

### 2.5. Similaridade de Gower (Gower Similarity)

Um detalhe prático importante: dados reais misturam **variáveis numéricas** (idade, salário) e **categóricas** (cidade, sexo, sim/não). A distância euclidiana clássica não sabe lidar com "São Paulo − Recife". A **Similaridade de Gower** resolve isso: é uma medida que combina variáveis numéricas e categóricas numa só nota de similaridade (de 0 a 1). Por isso o artigo a usa.

### 2.6. O teste TSTR (Train on Synthetic, Test on Real)

Esse é o teste de **utilidade** na prática, e o nome é autoexplicativo: **Treinar no Sintético, Testar no Real**.

1. Pegue só o dado **sintético** e treine um modelo de ML (classificador ou regressor) nele.
2. Teste esse modelo no dado **real**.
3. Se ele vai bem no real (apesar de nunca ter visto dado real no treino), então o sintético capturou os padrões que importam → **alta utilidade**.

Métricas usadas:
- **AUC (Area Under the ROC Curve):** para classificação. Vai de 0,5 (chute aleatório) a 1,0 (perfeito). Mede quão bem o modelo separa as classes.
- **MAE (Mean Absolute Error / Erro Absoluto Médio):** para regressão (no caso, o Boston Housing). Quanto **menor**, melhor.

O achado lindo do artigo: o gerador com **maior similaridade cruzada** (sem violar privacidade) foi também o que teve **melhor TSTR**. Ou seja, as duas formas de medir qualidade concordaram — boa fidelidade estatística "anda junto" com boa utilidade prática.

### 2.7. Os geradores testados (e a surpresa)

O artigo testou seis geradores, das grandes famílias que já vimos no Prog-01:
- **Baseados em Cópula (Copula):** GaussianCopula, CopulaGAN.
- **Baseados em GAN:** CTGAN, CopulaGAN.
- **Baseados em VAE:** TVAE.
- **Imputação sequencial (sequential imputation):** synthpop (usa árvores de decisão), UNCRi (usa vizinhos mais próximos + validação cruzada).

**A grande surpresa:** as **GANs** (CTGAN, CopulaGAN) — as mais "badaladas" e modernas — foram **consistentemente as piores**. E os métodos de **imputação sequencial** (synthpop, UNCRi) foram os melhores.

**Por quê?** A explicação técnica vale ouro: GANs e VAEs tentam modelar a **distribuição multivariada inteira** de uma vez — `P(x₁, x₂, x₃, …)` — que é dificílimo. Já a imputação sequencial quebra o problema: gera uma variável de cada vez, condicionada às anteriores — `P(x₇ | x₁, x₂, …)` — que são **distribuições univariadas**, muito mais fáceis de estimar bem. É o velho "dividir para conquistar".

> Lição: **o método mais sofisticado/popular nem sempre é o melhor.** Para dados tabulares, técnicas mais "simples" frequentemente ganham das GANs.

### 2.8. A pontuação única proposta

O autor fecha propondo uma métrica honesta:

> **Razão = (similaridade cruzada máxima média) ÷ (similaridade intra-conjunto máxima média no observado)**

- Razão **próxima de 1 (sem passar de 1)** = excelente: sintético e real são indistinguíveis em distribuição, sem cópia.
- Razão **> 1** = 🚨 os sintéticos estão *perto demais* dos reais → overfitting / quebra de privacidade.
- Sempre acompanhada de uma **checagem visual dos histogramas** (sanity check) — nunca confie só no número.

---

## 3. Exemplo prático: a lógica do teste em pseudocódigo

```python
# Conceito do Maximum Similarity Test (usando Gower para tipo misto)
intra_real  = [max_similarity(x, resto_de(real))      for x in real]      # vizinho no mesmo conjunto
intra_synth = [max_similarity(x, resto_de(synth))     for x in synth]
cross       = [max_similarity(x, synth)               for x in real]      # vizinho no outro conjunto

razao = media(cross) / media(intra_real)

if razao > 1:
    print("🚨 Privacidade comprometida (overfitting): sintéticos perto demais dos reais")
elif razao_proxima_de(1):
    print("✅ Provavelmente mesma distribuição-mãe: fidelidade + utilidade + privacidade")
# e sempre: plote os histogramas de intra_real, intra_synth e cross para conferir
```

---

## 4. Cases reais no mundo

- **Synthetic Data Vault (MIT):** as bibliotecas testadas no artigo (CTGAN, TVAE, GaussianCopula) nasceram no MIT e são o padrão open-source de geração de dados tabulares sintéticos — usadas por bancos e seguradoras para compartilhar dados sem vazar clientes. Este autoestudo mostra que escolher o gerador "na fé da fama" (GAN) pode dar errado: **é preciso avaliar**.
- **Saúde:** ao gerar prontuários sintéticos para pesquisa, a regra "razão ≤ 1" é literalmente a fronteira entre um dataset publicável e um **vazamento de dados de pacientes** (com risco legal sob LGPD/GDPR — conexão direta com o Prog-01).
- **Datasets clássicos:** o estudo usa o **Iris** (flores, R.A. Fisher, 1936) e o **Boston Housing** — datasets que são o "rato de laboratório" de ML há décadas, o que torna os resultados comparáveis e confiáveis.

---

## 5. Conexão com o módulo

- **Prog-01 (Geração de Dados Sintéticos):** par direto. Lá geramos e citamos fidelidade/utilidade/privacidade; aqui aprofundamos **como medir** essas três, e descobrimos que privacidade tem peso especial (falhar nela invalida o resto).
- **Teste A/B (tema do módulo):** lembra que no Prog-02 falamos em usar dados sintéticos para *testar pipelines de A/B antes de tocar usuários reais*? Este autoestudo é o controle de qualidade desse insumo: se o dado sintético não passa no Maximum Similarity Test, qualquer simulação de A/B feita sobre ele é não-confiável. Lixo entra, lixo sai.
- **Matemática:** os conceitos de **distribuição**, **amostra aleatória** e **distribuição-mãe** são exatamente a base de **Matemática-01 (Distribuições de Probabilidade)** e da estatística inferencial de **Matemática-03 (Hipóteses Estatísticas)**. A ideia de "essas duas amostras vêm da mesma população?" é *literalmente* a pergunta de um teste de hipóteses — o mesmo raciocínio por trás de decidir se a variante B de um teste A/B é mesmo diferente do controle A.
- **UX-01 (Métodos Mistos):** o TSTR é um exemplo de método **quantitativo** rigoroso; e a crítica do autor à "nota única dos fornecedores" ecoa a importância de não simplificar demais a avaliação.

---

## 6. Resumo estruturado

- **A pergunta central:** real e sintético são **amostras aleatórias da mesma distribuição-mãe**? Se sim, ganha-se fidelidade + utilidade + privacidade de uma vez.
- **Distribuição-mãe** = a verdadeira distribuição subjacente (nunca conhecida); **modelo** = nossa estimativa dela; **amostra aleatória** = os dados que vemos.
- **As 3 dimensões não são iguais:** falhar **privacidade** = overfitting = invalida fidelidade e utilidade. Não existe "2 de 3".
- **Maximum Similarity Test:** compara similaridade **intra-conjunto** vs. **cruzada**. Mesma distribuição → intra ≈ cross. Cópia/overfitting → cross > intra (🚨 privacidade).
- **Similaridade de Gower:** medida que lida com variáveis numéricas **e** categóricas juntas.
- **TSTR (Train on Synthetic, Test on Real):** treina no sintético, testa no real → mede **utilidade** (AUC p/ classificação, MAE p/ regressão).
- **Surpresa dos geradores:** **imputação sequencial** (synthpop, UNCRi) bateu as **GANs** (CTGAN, CopulaGAN), porque estimar distribuições **univariadas condicionais** é mais fácil que a multivariada inteira.
- **Métrica final:** razão `cross / intra` próxima de **1 sem exceder** = ótimo; **> 1** = vazamento. Sempre conferir histogramas.

---

## 7. Auto-reflexão (pra pensar sozinha)

1. Um fornecedor te vende um dataset sintético com "nota de qualidade 92/100" combinando fidelidade, utilidade e privacidade. Por que, segundo o artigo, essa nota única pode estar **escondendo** uma falha grave?
2. No Teste de Similaridade Máxima, o que significaria, na prática, encontrar uma razão `cross/intra` de **1,4**? O que você concluiria sobre o gerador que produziu esses dados?
3. Por que os métodos de imputação sequencial conseguem ser melhores que as GANs em dados tabulares — e como isso se relaciona com a ideia de "dividir um problema difícil em vários problemas fáceis"?
