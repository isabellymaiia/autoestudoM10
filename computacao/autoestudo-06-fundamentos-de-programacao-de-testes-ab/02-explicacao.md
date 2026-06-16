# Fundamentos de Programação de Testes A/B — Explicação

> **Material original:** [01-material.md](01-material.md)
> **Modo:** EXPLICAR
> **Como ler:** vai do mais básico ao mais avançado. Se já souber o começo, pula. Mas se for a primeira vez que você vê teste A/B, leia tudo na ordem — cada bloco se apoia no anterior.

---

## 1. Contexto geral: por que teste A/B existe?

Imagina que você abre uma sorveteria nova. Você está em dúvida entre dois sabores pra promover na vitrine: pistache e brigadeiro. Qual chama mais cliente?

Você tem dois caminhos:

- **Caminho do "achismo":** você acha que brigadeiro vende mais porque é mais brasileiro, mais conhecido, mais óbvio. Coloca brigadeiro na vitrine. Vende razoavelmente bem. Fim.
- **Caminho do experimento:** você divide a vitrine em duas metades, brigadeiro de um lado e pistache do outro, durante duas semanas. Conta quantos cones de cada saíram. No fim, você *sabe* qual vendeu mais — e por quanto.

O segundo caminho é, em essência, um **teste A/B**. Você comparou duas opções, expostas em condições parecidas, e mediu a resposta com dados reais.

**De onde isso vem?** Não é uma invenção da internet. A ideia de experimento controlado nasceu no começo do século XX, principalmente com o estatístico **Ronald Fisher**, que projetava experimentos agrícolas — qual variedade de trigo dava mais grão? — usando aleatorização e grupos de controle. Depois, a medicina herdou a metodologia nos **ensaios clínicos** (clinical trials): grupo que recebe o remédio vs grupo que recebe placebo (uma pílula falsa, sem o princípio ativo).

A internet pegou essa metodologia e turbinou. Por quê? Porque online você pode:

- Mostrar a versão A pra metade dos visitantes e a versão B pra outra metade, **automaticamente**.
- Rodar o experimento por horas ou dias em vez de anos.
- Medir cada clique, cada compra, cada milissegundo de tempo na página.
- Repetir indefinidamente, com custo baixíssimo.

É por isso que teste A/B virou onipresente em produto digital, marketing, e-commerce, growth, e até em design de algoritmos de recomendação.

**O problema que ele resolve:** a maior parte das decisões em negócio é tomada sob incerteza. Você não sabe se o botão verde converte mais que o azul, se o título "Compre agora" funciona melhor que "Garanta o seu", se a foto do produto na esquerda vende mais que na direita. Você pode *achar* que sabe — mas frequentemente está errado. Teste A/B substitui *achismo* por **evidência estatística**.

É o coração do que se chama **data-driven decision making** — tomar decisões com dados, não com opinião.

---

## 2. Conceitos-chave

Vou montar o vocabulário do mais básico ao mais avançado. Lê na ordem.

### 2.1. Variante, controle e tratamento

Um teste A/B tem no mínimo duas **variantes** (variants):

- **A = controle** (control) — a versão atual, a que já existe.
- **B = tratamento** (treatment) — a versão nova, com a mudança que você quer testar.

Esses nomes vêm direto da medicina: o grupo que recebe placebo é o **controle**; o grupo que recebe o remédio é o **tratamento**.

> 🇬🇧 **Termos em inglês:** *control* (controle) e *treatment* (tratamento). Você também vai ouvir *champion vs challenger* — "campeão" é a versão atual, "desafiante" é a nova. Mesmo conceito, vocabulário de marketing/produto.

Se você testa mais de uma versão nova ao mesmo tempo (B, C, D…), chama-se **teste A/B/n**.

### 2.2. A variável (só uma!)

O artigo em português é categórico nisso, e está certíssimo: **mude apenas uma coisa por vez**.

Se você muda o botão (verde → azul) E o título E a foto, e a versão B converte mais — o que causou a melhora? Você não sabe. Pode ter sido o botão, pode ter sido o título, pode ter sido a combinação. Você isolou nada.

Isso é o princípio do **experimento controlado** (controlled experiment): manter tudo igual exceto uma variável. Aí, se a métrica muda, você sabe a quem creditar.

> Exceção: **testes multivariados** (multivariate tests, ou MVT) testam múltiplas variáveis de propósito, em combinações. Mas a leitura é mais complexa, exigem MUITO mais tráfego, e a maioria dos times começa com A/B simples. Volto nisso no item 2.10.

### 2.3. Aleatorização (randomization)

Como você decide quem vai pro grupo A e quem vai pro grupo B?

**Resposta certa:** aleatoriamente. Cada visitante tem 50% de chance de cair em A e 50% em B (ou outra proporção, se você quiser).

**Por que aleatório e não, sei lá, "homens vão pro A, mulheres pro B"?**

Porque se você usa uma característica conhecida (gênero, idade, país) pra dividir, qualquer diferença que aparecer pode ser por causa dessa característica, e não da sua mudança. Isso se chama **confounding** — variável de confusão. A aleatorização espalha as características igualmente entre os grupos: A e B vão ter mais ou menos a mesma proporção de homens, mulheres, jovens, velhos, clientes novos, clientes recorrentes, etc. Aí qualquer diferença que sobrar é, com alta probabilidade, da sua mudança.

> 🇬🇧 **Randomization** (aleatorização) é talvez a palavra mais importante de toda a metodologia. Sem ela, você não tem teste A/B — tem comparação enviesada.

### 2.4. Métrica de sucesso (KPI)

Você precisa decidir, **antes** de rodar o teste, **o que conta como vitória**.

Exemplos de métricas:

- **Taxa de conversão** (conversion rate): % de pessoas que fizeram a ação desejada (comprar, se cadastrar, clicar).
- **CTR** (click-through rate): % de pessoas que clicaram em algo.
- **Revenue per user**: receita média por usuário.
- **Tempo na página** (time on page): quanto tempo o usuário fica.
- **Bounce rate**: % de pessoas que entraram e saíram sem interagir.

> 🇬🇧 **KPI = Key Performance Indicator** — indicador-chave de desempenho. Métrica que importa.

Você define **uma métrica primária** (a que decide o vencedor) e algumas **métricas secundárias** (que monitora pra ter contexto). Às vezes você também define **guardrail metrics** (literalmente "métricas guarda-corpo"): métricas que **não podem piorar**, mesmo que a primária melhore. Por exemplo: você quer aumentar conversão (primária), mas não pode aumentar reclamações de cliente (guardrail). Se a primária subiu mas a guardrail também subiu junto, você está trocando uma coisa por outra, e talvez não valha.

### 2.5. Hipótese

Todo experimento começa com uma **hipótese** — uma afirmação que você quer testar. Por exemplo:

> "Mudar o botão de 'Comprar' para 'Garanta o seu' vai aumentar a taxa de conversão em pelo menos 5%."

Em estatística, formalizamos isso em duas hipóteses opostas:

- **Hipótese nula (H₀, null hypothesis):** "Não há diferença entre A e B." É o que você assume como ponto de partida — o "inocente até prova em contrário" da estatística.
- **Hipótese alternativa (H₁, alternative hypothesis):** "Há diferença entre A e B." É o que você quer provar.

O teste estatístico vai te dizer **se há evidência suficiente pra rejeitar H₀**. Note: rejeitar H₀ não é o mesmo que "provar H₁" — é só dizer que os dados são incompatíveis com H₀ o bastante pra você descartar.

Isso é parecido com o tribunal: o réu é considerado inocente (H₀); o promotor tem que apresentar evidência forte o suficiente pra "rejeitar" a inocência. Se a evidência for fraca, você não declara inocente, você só *não condena*. Mesma lógica.

### 2.6. Significância estatística e p-value

Aqui entra um dos termos mais importantes — e mais mal usados — em teste A/B: o **p-value** (valor-p).

**Definição informal:** o p-value é a probabilidade de você observar dados tão extremos (ou mais) quanto os que você observou, **assumindo que H₀ é verdadeira**.

Em português direto: "se na verdade não tivesse diferença nenhuma entre A e B, qual a chance de eu ter visto uma diferença desse tamanho só por sorte?"

Se essa chance é baixa (digamos, menor que 5%), você diz: "ok, é muito improvável que isso tenha sido só sorte — provavelmente tem mesmo diferença." Aí você **rejeita H₀**.

O famoso **5% (ou 0,05)** é o **nível de significância** (significance level, α). É arbitrário, vem de uma convenção que o Fisher chutou nos anos 30 e ninguém nunca trocou. Significa: "estou disposto a estar errado 5% das vezes — ou seja, em 5% dos testes vou dizer que tem diferença quando não tem."

> ⚠️ **Erro clássico:** p-value **não é** "a probabilidade de B ser melhor que A". É a probabilidade dos dados, assumindo que não tem diferença. Confundir os dois é um dos erros mais comuns em interpretação de A/B.

### 2.7. Intervalo de confiança (confidence interval)

Outra forma de reportar o resultado é dizer: "a diferença entre B e A é, com 95% de confiança, entre +2% e +8%."

Esse "entre +2% e +8%" é o **intervalo de confiança** (CI, confidence interval). Ele dá uma sensação de **tamanho do efeito** e **incerteza**, não só "deu certo / não deu".

Se o intervalo cruza o zero (ex: "entre -1% e +5%"), você não tem confiança de que houve melhora — pode até ter sido pior. Se o intervalo está todo positivo (ex: "entre +2% e +8%"), você confia que melhorou — a dúvida é só *quanto*.

CI é geralmente mais informativo que p-value isolado. Bons relatórios mostram os dois.

### 2.8. Tamanho da amostra (sample size) e poder estatístico (power)

Aqui muita gente quebra a cara. Vamos pensar:

- Se você roda o teste com 10 pessoas (5 em A, 5 em B), mesmo que B seja realmente muito melhor, você provavelmente não vai conseguir detectar isso — a aleatoriedade nessa escala domina tudo.
- Se você roda com 10 milhões, você detecta diferenças minúsculas — até diferenças que não importam na prática.

**Poder estatístico** (statistical power) é a probabilidade de detectar um efeito real, dado que ele existe. Convenção: 80% (ou seja, em 80% dos casos onde existe diferença, você consegue ver).

Pra atingir esse poder, você precisa de um certo **tamanho de amostra mínimo**. Quanto menor o efeito que você quer detectar, maior a amostra necessária. Detectar +10% de conversão é fácil; detectar +0,5% exige amostra gigante.

Existe um **cálculo de tamanho de amostra** (sample size calculator) que você faz **antes** do teste, dado:

- A taxa de conversão atual (baseline).
- O menor efeito que vale a pena detectar (MDE = minimum detectable effect).
- O nível de significância (α, geralmente 5%).
- O poder estatístico (geralmente 80%).

> 🇬🇧 **MDE = minimum detectable effect** — menor efeito detectável. "Quero detectar pelo menos uma melhora de 5%" → seu MDE é 5%.

⚠️ **Erro clássico #2:** ficar "espiando" o teste e parando quando dá significância. Isso se chama **peeking** (espiar) e infla muito o falso positivo. Você precisa decidir o tamanho da amostra antes e respeitar.

### 2.9. Testes estatísticos comuns

A pergunta que o teste estatístico responde é sempre a mesma: "essa diferença é grande o bastante pra eu acreditar que não é só sorte?". Mas o **tipo de cálculo** muda conforme a natureza da métrica:

**T-test (Independent Samples t-test, teste t de Student):**

- Usado quando a métrica é **contínua** (número com decimais, valores quaisquer): tempo na página, receita por usuário, número de itens no carrinho.
- Compara as **médias** dos dois grupos.
- É o que o artigo em inglês cita: "test whether the unknown population means of two groups are equal or not."

**Chi-squared test (qui-quadrado, χ²):**

- Usado quando a métrica é **categórica** (sim/não, converteu/não converteu, clicou/não clicou).
- Compara as **proporções** entre os grupos.
- É o que o artigo em inglês usa no exemplo da mailing list: "converteu vs não converteu" entre os dois grupos.

**Z-test pra proporções:**

- Alternativa ao chi-squared, equivalente em muitos casos.

Você não precisa decorar fórmulas — bibliotecas como `scipy.stats` (Python) ou `prop.test` (R) fazem o cálculo. Você só precisa **saber qual usar**.

Regra prática: métrica é "sim ou não"? → chi-squared. Métrica é número contínuo? → t-test.

### 2.10. Teste multivariado (MVT) vs A/B vs A/B/n

| Tipo | O que testa | Exemplo |
|---|---|---|
| **A/B** | 1 variável, 2 versões | Botão verde vs azul |
| **A/B/n** | 1 variável, N versões | Botão verde vs azul vs vermelho vs roxo |
| **MVT** (multivariate) | N variáveis simultâneas, em combinações | Botão (verde/azul) × Título ("Compre"/"Garanta") = 4 combinações |

MVT permite descobrir **interações** (ex: o botão verde funciona melhor com o título "Compre" mas pior com "Garanta"). Mas exige tráfego muito maior, porque cada combinação precisa ser estatisticamente válida.

**Quando usar cada um:**

- A/B: padrão. Comece por aqui.
- A/B/n: quando você tem várias ideias mutuamente exclusivas pra uma mesma dimensão.
- MVT: quando você tem muito tráfego, várias dimensões pra otimizar, e suspeita de interações.

### 2.11. CRO vs A/B testing

O artigo levanta essa distinção e ela é importante:

- **A/B testing** é uma **técnica**.
- **CRO** (Conversion Rate Optimization, otimização de taxa de conversão) é uma **disciplina/estratégia** que usa A/B testing como uma de suas ferramentas, junto com:
  - **Heatmaps** (mapas de calor: onde os usuários clicam, até onde scrollam).
  - **Session recordings** (gravações de sessão: ver o que o usuário fez na tela).
  - **User research qualitativa** (entrevistas, surveys).
  - **Análise de funil** (onde as pessoas desistem).
  - **Análise quantitativa** dos dados do produto.

CRO é o "porquê" e o "o quê"; A/B testing é o "como provar". Bom CRO depende de boas hipóteses — e boas hipóteses vêm da qualitativa, não dos próprios testes.

### 2.12. Eventos de ativação (activation events)

Esse é o conceito mais avançado do material (veio do vídeo do "A/B Test Like a Pro #6").

**O problema:** imagina que você testa uma mudança no botão de checkout. Você joga 50% dos visitantes do site no grupo A e 50% no B. Mas a maioria dos visitantes nunca chega no checkout! Eles entram na home, olham, e saem. Pra esses, sua mudança nunca foi vista.

Se você incluir esses usuários na análise, eles vão "diluir" o efeito — porque eles não foram realmente afetados. Vai parecer que o efeito é menor do que de fato é.

**Solução: evento de ativação.** Você só conta na análise os usuários que **chegaram a ver** a mudança (entraram no checkout, no caso). O "evento de ativação" é o gatilho que marca: "agora esse usuário está oficialmente exposto ao experimento."

Isso aumenta a sensibilidade do teste sem trapacear estatisticamente — desde que você defina o evento de ativação **antes** de começar o teste.

### 2.13. Múltiplos testes simultâneos

**Dúvida natural:** "posso rodar 5 testes ao mesmo tempo no meu site?"

**Resposta:** sim, mas com cuidados.

- Se os testes são em **partes diferentes do produto** (um na home, outro no checkout), e os usuários são distribuídos aleatoriamente em cada um *independentemente*, os efeitos se "anulam" estatisticamente. É chamado de **mutually exclusive layers** (camadas mutuamente exclusivas) — você empilha experimentos sem que um contamine o outro.
- Se os testes são na **mesma área** ou um afeta o outro, você pode ter **interação**: o efeito do teste 1 muda dependendo de qual variante do teste 2 o usuário viu. Aí você precisa ou tornar os testes mutuamente exclusivos (cada usuário só entra num deles), ou modelar a interação como MVT.

Empresas como Microsoft e Booking.com rodam centenas/milhares de testes simultâneos com sistemas sofisticados de layering.

### 2.14. Análise no data warehouse (BigQuery e cia.)

A descrição do vídeo menciona **BigQuery** — o data warehouse do Google. Por quê?

Ferramentas como Google Optimize, Optimizely, VWO têm um console pronto que mostra resultados pra métricas pré-configuradas (conversão, cliques). Mas e quando você quer testar uma métrica customizada que o console não suporta? Por exemplo: "qual variante gera maior LTV (lifetime value, valor de vida do cliente) nos próximos 90 dias?".

Aí você exporta os dados brutos do experimento (qual usuário caiu em qual variante) pro BigQuery, junta com seus dados de venda/comportamento via SQL, e calcula a métrica que quiser. Esse é o padrão em empresas mais maduras: a ferramenta de A/B faz o split e logging, mas a análise séria acontece no data warehouse.

---

## 3. Exemplo prático: chi-squared em Python

O artigo em inglês usa o **chi-squared test for independence** (qui-quadrado de independência) pra avaliar se uma "mailer bonita" converte mais que uma "mailer simples". Vamos fazer um exemplo análogo, comentado.

**Cenário:** você testa duas versões de uma landing page. Quer saber se a taxa de cadastro muda.

- **Variante A (controle):** 1000 visitantes, 100 se cadastraram → taxa = 10%
- **Variante B (tratamento):** 1000 visitantes, 130 se cadastraram → taxa = 13%

Pergunta: essa diferença de 3 pontos percentuais é real ou pode ser só sorte?

```python
from scipy.stats import chi2_contingency

# Tabela de contingência:
# linhas    = variante (A controle, B tratamento)
# colunas   = converteu? (sim, não)
#                  sim   não
observed = [
    [100, 900],   # A: 100 conversões em 1000 visitantes
    [130, 870],   # B: 130 conversões em 1000 visitantes
]

chi2, p_value, dof, expected = chi2_contingency(observed)

print(f"Estatística chi²: {chi2:.4f}")
print(f"p-value:          {p_value:.4f}")
print(f"Graus de liberdade: {dof}")

alpha = 0.05
if p_value < alpha:
    print(f"\np-value < {alpha} → rejeitamos H₀.")
    print("Há diferença estatisticamente significativa entre A e B.")
else:
    print(f"\np-value ≥ {alpha} → não rejeitamos H₀.")
    print("Sem evidência forte de diferença.")
```

**Saída esperada:**

```
Estatística chi²: 4.7872
p-value:          0.0287
Graus de liberdade: 1

p-value < 0.05 → rejeitamos H₀.
Há diferença estatisticamente significativa entre A e B.
```

**Como ler isso:**

- A função `chi2_contingency` recebe a tabela de contagens observadas e calcula:
  - `chi2`: o valor da estatística qui-quadrado (quanto maior, maior a diferença entre observado e o que esperaríamos sob H₀).
  - `p_value`: a probabilidade de observar uma diferença tão grande quanto essa, se H₀ fosse verdade.
  - `dof`: graus de liberdade (degrees of freedom). Pra uma tabela 2×2, é 1.
  - `expected`: as contagens que esperaríamos sob H₀ (não usado aqui, mas útil pra debug).
- O p-value 0,029 é menor que 0,05 → você rejeita H₀ e conclui que provavelmente há diferença real.
- Mas atenção: o teste só te diz **se** há diferença. **Quanto** é a diferença você lê das proporções (13% vs 10% → lift de 30% relativo, ou +3 pontos percentuais absolutos). E **se vale a pena** depende do contexto de negócio.

> 🇬🇧 **Lift** é o termo padrão pra "ganho percentual relativo": (13 − 10) / 10 = 30% de lift. Você vai ver muito esse termo.

Se quiser fazer pra **métrica contínua** (ex: receita média por usuário), você usaria `scipy.stats.ttest_ind` em vez de `chi2_contingency`. Mesmo espírito, função diferente.

---

## 4. Cases reais

Onde o teste A/B já moveu bilhões? Bastante lugar:

**Booking.com** é o exemplo lendário. Eles rodam **mais de 1.000 testes A/B simultâneos** a qualquer momento, e basicamente todo botão, tooltip e cor passou por experimento. Têm uma cultura interna chamada de **"every change should be a test"**. O ex-Diretor de Experimentação deles (Lukas Vermeer) tem palestras públicas explicando como eles operam. Booking atribui boa parte do seu crescimento a essa cultura.

**Netflix** publicou um post famoso sobre testar **diferentes imagens (thumbnails)** pro mesmo título. A mesma série pode mostrar a foto de um personagem pra você e de outro personagem pra mim, dependendo do que historicamente te atrai. Eles documentaram aumentos de 20-30% no engajamento de títulos individuais só trocando a arte da capa.

**Amazon** testa praticamente todo elemento da página de produto. Existe uma anedota famosa sobre eles terem testado e descoberto que **mostrar a foto do produto à esquerda** (com texto à direita) converte mais que o contrário em culturas que leem da esquerda pra direita — mas o contrário em culturas que leem da direita pra esquerda. Localização de design baseada em dados.

**Microsoft Bing** tem um caso muito citado por **Ronny Kohavi** (autor do livro *Trustworthy Online Controlled Experiments*, leitura quase obrigatória da área): uma mudança aparentemente boba — exibir mais informações nos resultados de busca — gerou um aumento de receita de **mais de US$ 100 milhões/ano**. Ninguém imaginava o impacto até rodar o teste.

**Google** ficou famoso por testar **41 tons de azul** pra ver qual link convertia mais. Isso virou meme dentro e fora da empresa. Mostra dois lados: (a) o poder do teste extremo, (b) o risco de se viciar em otimização local e perder visão de design.

**Obama 2008** — vale citar fora do mundo tech: a campanha presidencial de Obama em 2008 rodou A/B tests no site de captação de doação. Mudaram a foto do banner principal e o texto do botão de "Sign Up" pra "Learn More". Aumentaram a taxa de cadastro em ~40%, o que se traduziu em **US$ 60 milhões a mais arrecadados**. Caso público, virou estudo de caso em escolas de negócios.

---

## 5. Conexão com o módulo

Esse é o autoestudo **01** do módulo, e ele é o ponto de partida que vai ramificar pras outras matérias. Algumas pontes que você vai cruzar adiante:

- **Matemática:** vai aprofundar a parte estatística — p-value, distribuições amostrais (especialmente a normal e a binomial), teste de hipótese, intervalo de confiança, teorema do limite central. Tudo o que aqui foi "convenção" (por que 5%? por que 80%?) vai ganhar a fundação matemática.
- **Negócios:** "qual o lift mínimo que vale a pena testar?", priorização de hipóteses (frameworks como **ICE** — Impact, Confidence, Ease), e como traduzir teste em decisão estratégica. Aqui o foco é o "o quê" e "por quê", complementar ao "como" desse autoestudo.
- **UX:** geração de hipóteses qualitativas (entrevistas, usability testing, heuristic evaluation) que alimentam os testes A/B. Sem boas hipóteses, você está testando ruído.
- **Liderança:** cultura de experimentação. Como convencer um time/diretoria a aceitar que metade das ideias vai falhar (e tudo bem). Como lidar com o stakeholder que veio com a "ideia que tem certeza que vai funcionar" e quer pular o teste.

Quando esses autoestudos chegarem, vou puxar a conexão concreta com este aqui.

---

## 6. Resumo estruturado

- **Teste A/B = experimento controlado e aleatorizado** entre uma variante A (controle) e uma B (tratamento), pra comparar uma métrica de sucesso.
- **Regra de ouro:** mude *uma* coisa por vez. Aleatorize. Defina a métrica antes.
- **Pilares estatísticos:** hipótese (H₀ vs H₁), p-value, nível de significância (α, geralmente 5%), poder (geralmente 80%), tamanho de amostra mínimo, intervalo de confiança.
- **Testes estatísticos:** chi-squared pra métricas categóricas (converteu/não), t-test pra métricas contínuas (receita, tempo).
- **Variantes:** A/B (2 versões) → A/B/n (várias versões na mesma dimensão) → MVT (várias dimensões simultâneas, mais caro estatisticamente).
- **CRO** é a disciplina guarda-chuva; A/B testing é uma das suas ferramentas.
- **Avançado:** eventos de ativação (analisar só quem foi exposto), testes simultâneos com layers exclusivas, análise customizada em data warehouse (BigQuery).
- **Erros clássicos:**
  - Confundir p-value com "probabilidade de B ser melhor".
  - Espiar o teste (peeking) e parar quando der significância.
  - Mudar várias coisas ao mesmo tempo.
  - Não calcular tamanho de amostra antes.
  - Ignorar significância prática (estatisticamente significativo ≠ vale a pena implementar).
- **Cultura:** Booking, Netflix, Amazon, Microsoft, Google e até campanhas políticas usam A/B testing como motor de decisão. É padrão da indústria, não exotismo.

---

## 7. Auto-reflexão (não precisa responder)

1. Pensa num produto digital que você usa todo dia (Instagram, iFood, Spotify). Que elementos dele você acha que devem estar sendo A/B testados *agora* sem você saber?
2. Se o p-value do seu teste deu 0,06 (logo acima de 0,05), você implementa a mudança ou não? Por quê? Que outras informações você gostaria de ter antes de decidir?
3. Por que faria sentido um teste A/B "perder" (a variante B ser pior que A) ser considerado um *resultado de valor* pra empresa, mesmo que você decida não implementar B?
