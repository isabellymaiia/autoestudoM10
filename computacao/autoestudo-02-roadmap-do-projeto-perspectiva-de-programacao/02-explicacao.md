# Roadmap do Projeto (Perspectiva de Programação) — Explicação

> **Matéria:** Computação / Programação · **Autoestudo:** 02 · **Data:** 29/04/2026 · **Professor:** Jefferson de Oliveira Silva
>
> Explicação detalhada a partir das três fontes do [`01-material.md`](01-material.md): Simulação de Monte Carlo (AWS), Cadeias de Markov (Built In) e Teste A/B (RD Station).

---

## 1. Contexto geral: por que esses três temas juntos?

Esse autoestudo é um **"roadmap"** — um mapa do caminho. Ele não aprofunda um tema só; ele te apresenta os **três pilares técnicos** que a trilha de Programação do módulo vai usar e aprofundar depois. Pensa neles como as três ferramentas de uma mesma caixa:

1. **Simulação de Monte Carlo** — a ferramenta de *simular o futuro incerto* ("o que pode acontecer e com que probabilidade?").
2. **Cadeias de Markov** — a ferramenta de *modelar sequências de eventos* ("dado onde estou agora, pra onde provavelmente vou?").
3. **Teste A/B** — a ferramenta de *decidir com evidência* ("a versão nova é mesmo melhor, ou foi sorte?").

O fio que costura os três é uma palavra: **incerteza**. O mundo real não é determinístico (uma conta fixa que sempre dá o mesmo resultado); ele é **probabilístico** — cheio de aleatoriedade. Esses três métodos são jeitos diferentes de domar a incerteza com matemática e código. Vamos a cada um, e depois eu mostro como eles se encaixam.

> **Analogia-guia:** imagine que você vai abrir uma cafeteria.
> - **Monte Carlo** responde: "se eu rodar mil cenários de movimento, clima e preço do café, qual a chance de eu ter lucro no 1º ano?"
> - **Markov** responde: "um cliente que pediu cappuccino hoje, o que ele provavelmente pede amanhã?"
> - **Teste A/B** responde: "o cardápio com foto vende mais que o sem foto — ou a diferença foi só do acaso da semana?"

---

## 2. Pilar 1 — Simulação de Monte Carlo

### 2.1. Determinístico vs. probabilístico

Essa distinção é o coração de tudo.

- **Determinístico (deterministic):** mesma entrada → sempre a mesma saída, sem incerteza. "A distância de casa ao trabalho é 12 km." Ponto.
- **Probabilístico / estocástico (stochastic):** inclui aleatoriedade; cada execução pode dar um resultado diferente. "O tempo de viagem varia conforme trânsito, clima e pneu furado." Aqui não há *uma* resposta — há uma *distribuição* de respostas possíveis, cada uma com sua probabilidade.

> **Estocástico** (do grego *stókhos*, "alvo/chute") é o termo técnico para "que envolve aleatoriedade". Guarde bem essa palavra — ela volta nas Cadeias de Markov.

A simulação de Monte Carlo é uma **técnica probabilística**: em vez de dar uma resposta única (como um método determinístico faria), ela te dá **muitos resultados possíveis e a probabilidade de cada um**.

### 2.2. Como funciona: rodar muito, muitas vezes

O nome vem do **cassino de Monte Carlo, em Mônaco** — porque o método se baseia na mesma aleatoriedade da roleta. Foi inventado por **John von Neumann e Stanislaw Ulam nos anos 1940** (durante o Projeto Manhattan, para simular o comportamento de nêutrons).

A ideia, na prática:
1. Você define um **modelo matemático** (uma equação que liga entradas a saídas). Ex.: `lucro = receita − despesas`.
2. Você não sabe os valores exatos das entradas, então representa cada uma como uma **distribuição de probabilidade** (a receita "provavelmente fica entre X e Y, mais provável perto de Z").
3. O computador **sorteia** valores aleatórios dessas distribuições e calcula o resultado. Uma vez. Depois sorteia de novo. E de novo. **Milhares de vezes.**
4. No fim, você tem milhares de resultados que, juntos, formam um **histograma** — a "cara" de todos os futuros possíveis.

O princípio teórico por trás disso é a **ergodicidade**: num sistema fechado, se você deixar um ponto se mover aleatoriamente por tempo suficiente, ele acaba visitando *todos* os estados possíveis. Por isso **quanto mais simulações, mais preciso o resultado** — 10 mil rodadas dão um retrato muito mais fiel que 100. É o mesmo princípio do dado: jogue 6 vezes e o resultado é irregular; jogue 60 mil e cada face aparece bem perto de 1/6.

O motor disso tudo são os **geradores de números aleatórios (random number generators)** — programas que produzem sequências imprevisíveis, recriando a incerteza das entradas.

### 2.3. Componentes (o esqueleto de qualquer simulação)

| Componente | O que é | Exemplo |
|---|---|---|
| **Variáveis de entrada (input)** | valores aleatórios que afetam o resultado | qualidade de fabricação, temperatura |
| **Modelo matemático** | a equação que liga entrada e saída | `lucro = receita − despesas` |
| **Variável de saída (output)** | o resultado, mostrado num histograma | expectativa de vida do produto |

### 2.4. Distribuições de probabilidade

A escolha da distribuição de cada entrada é a decisão mais crítica (e a maior fonte de erro). As três mais comuns:
- **Normal (curva de sino):** simétrica, valores concentrados no meio. A maioria dos fenômenos naturais (alturas, pesos, erros de medição).
- **Uniforme:** todos os valores têm a mesma chance (uma linha reta). Ex.: a face de um dado.
- **Triangular:** definida por mínimo, máximo e o valor mais provável (a moda). Muito usada em negócios quando você só tem uma estimativa "pessimista / mais provável / otimista".

### 2.5. Monte Carlo vs. machine learning

Um contraste importante da fonte: **ML aprende o modelo a partir dos dados** (você dá entradas e saídas, ele descobre a relação). **Monte Carlo já tem o modelo** (a equação é conhecida) e usa aleatoriedade para explorar os resultados. Eles se complementam: ML pode ser usado para *testar e confirmar* os resultados de uma simulação de Monte Carlo.

### 2.6. Desafios

- **Lixo entra, lixo sai (garbage in, garbage out):** o resultado é só tão bom quanto as distribuições de entrada que você escolheu.
- **Custo computacional:** milhares de rodadas com muitas variáveis podem levar horas ou dias (daí a fonte mencionar o AWS Batch, que paraleliza isso na nuvem).

---

## 3. Pilar 2 — Cadeias de Markov

### 3.1. O que é

Uma **Cadeia de Markov (Markov chain)** é um **modelo estocástico** (lembra a palavra?) que prevê a probabilidade de uma **sequência de eventos** com base **no evento mais recente**. Foi criada pelo matemático russo Andrey Markov.

A pergunta central que ela responde: **"dado o estado em que estou agora, qual a probabilidade de eu ir para cada próximo estado?"**

### 3.2. A característica mágica: ausência de memória (memorylessness)

Essa é a propriedade que define Markov e cai em toda prova: **a propriedade de ausência de memória (memorylessness)**, também chamada de *propriedade de Markov*. Significa que **o futuro depende só do presente, não do passado**. O modelo "esqueceu" todo o caminho que percorreu até aqui — só importa onde ele está *agora*.

> **Analogia:** num jogo de tabuleiro tipo Banco Imobiliário, a casa pra onde você vai depende só de onde você está *agora* + o dado que você vai jogar. Não importa se você chegou nessa casa depois de dar 3 voltas ou se acabou de sair da prisão. O presente é tudo que conta.

Isso é **bênção e maldição**, como diz a fonte:
- **Bênção:** simplicidade. Para prever a próxima palavra que você digita, o modelo não precisa lembrar o que você escreveu 3 parágrafos atrás.
- **Maldição:** ele *não consegue* usar contexto distante. Por isso modelos de linguagem modernos (Transformers, como o GPT) superaram Markov em NLP — eles *têm* memória de longo alcance.

### 3.3. Os dois ingredientes

Para construir uma cadeia de Markov você precisa de duas coisas:

**1. Matriz de transição (transition matrix), "P":** uma tabela NxN com a probabilidade de ir de cada estado para cada outro estado. Regra de ouro: **cada linha soma 1** (porque, a partir de um estado, você *tem* que ir para algum lugar — as probabilidades de todos os destinos somam 100%). Uma matriz assim é chamada **matriz estocástica**.

```
        para A   para B   para C
de A  [  .2      .3       .5   ]   ← soma = 1
de B  [  .6      0        .4   ]   ← soma = 1
de C  [  .1      .7       .2   ]   ← soma = 1
```
(Lê-se: estando em A, há 20% de continuar em A, 30% de ir pra B, 50% de ir pra C.)

**2. Vetor de estado inicial (initial state vector), "S":** um vetor Nx1 com a probabilidade de você *começar* em cada estado.

Com esses dois, você multiplica matrizes para prever o futuro: elevando a matriz P à **M-ésima potência**, você descobre as probabilidades de estado depois de M passos.

### 3.4. Exemplo clássico: predição de texto

O exemplo da fonte é o **autocomplete**. Pegue um texto grande: cada palavra é um *estado*, e a probabilidade de ir de uma palavra à próxima é calculada pela **frequência** com que elas aparecem juntas no corpus. Se depois de "Hello" aparecem, em 20 ocorrências, 10 vezes "There" e 9 vezes "Everyone", então `P(There | Hello) = 10/20 = 50%`. O código Python da fonte faz exatamente isso: monta um dicionário `palavra → [palavras que vêm depois]` e sorteia a próxima.

```python
# o coração do modelo: mapear cada palavra às que a seguem
for current_word, next_word in zip(words[0:-1], words[1:]):
    markov_dict[current_word].append(next_word)
# ...e depois sortear a próxima a partir da atual:
word2 = random.choice(chain[word1])
```

---

## 4. Pilar 3 — Teste A/B

Esse é o **tema central do módulo**, então aqui o roadmap toca o destino final. (E ele dialoga diretamente com o [Autoestudo 06: Fundamentos de Programação de Testes A/B](../autoestudo-06-fundamentos-de-programacao-de-testes-ab/02-explicacao.md).)

### 4.1. O que é

**Teste A/B** (também *split test*, teste de divisão, teste de comparações) é uma técnica de experimentação: você divide o público **aleatoriamente** em dois grupos no **mesmo período**, mostra a **versão A (controle)** para um e a **versão B (desafiante/variante)** para o outro, e compara qual converte melhor.

Dois termos-chave:
- **Controle (control):** a versão atual, o "ponto de comparação".
- **Desafiante / variante (challenger/variant):** a versão modificada que você quer testar.

Por que isso funciona tão bem? Porque a divisão **aleatória** e **simultânea** transforma o teste num **experimento controlado**: como tudo mais é igual (mesmo período, públicos parecidos), a única diferença é a mudança que você fez — então qualquer diferença no resultado pode ser **atribuída a ela**. É o método científico aplicado a marketing e produto. Isso é o que a UX-01 chamaria de método **comportamental, quantitativo e somativo**.

### 4.2. A regra de ouro: um elemento por vez

**Nunca mude mais de um elemento num mesmo teste A/B.** Se você troca o título *e* o botão *e* a imagem de uma vez e a conversão sobe, você não sabe *qual* foi o responsável. (Mudar vários ao mesmo tempo de forma estruturada é outro método, o *teste multivariado*.)

### 4.3. O ponto mais importante: significância estatística e intervalo de confiança

Aqui está o conceito que separa "achismo" de "ciência" — e que conecta diretamente com a Matemática do módulo.

Imagine jogar uma moeda 200 vezes. Deu cara 116 vezes (58%). A moeda é viciada? **Não necessariamente** — pode ter sido azar/sorte da amostra. A estatística mede isso com o **intervalo de confiança (confidence interval)**: a probabilidade de a diferença observada (controle vs. experimento) representar a realidade da população inteira, e não um acaso.

- No exemplo da moeda, 58% dá um intervalo de confiança de ~90% — que parece alto, mas é **estatisticamente baixo** para decidir.
- A regra prática: só dê um teste como válido com **intervalo de confiança ≥ 95%** (99% é ótimo).

> **Significância estatística (statistical significance)** = a garantia de que o resultado **não aconteceu por acaso**. É o critério de parada do teste: você para quando atinge a confiança necessária, não quando "parece" que uma versão ganhou.

Exemplo da fonte que mostra por que isso importa:
- LP A: 46% conversão · LP B: 40% · confiança 90% → **inconclusivo** (a diferença pode ser ruído; trocar pode até piorar).
- LP A: 52% · LP B: 40% · confiança 99,9% → **conclusivo** (pode trocar com segurança).

### 4.4. Quando NÃO fazer teste A/B

A fonte é honesta sobre isso (e é maduro entender): **se você não tem volume de tráfego suficiente, não faça.** Sem amostra grande, você nunca atinge significância estatística e toma decisões prematuras. Para iniciantes com pouco tráfego, montar a estrutura de marketing rende mais que rodar testes que nunca conclusivos. (Para saber o tamanho de amostra necessário, usa-se uma **calculadora de teste A/B** — que faz *power analysis*.)

---

## 5. Como os três pilares se conectam (o "roadmap" de verdade)

Aqui está o desenho que justifica juntar os três num só autoestudo:

```
        INCERTEZA DO MUNDO REAL
                  │
   ┌──────────────┼──────────────┐
   ▼              ▼              ▼
MONTE CARLO    MARKOV        TESTE A/B
(simular     (modelar      (decidir com
 cenários)    sequências)   evidência)
   │              │              │
   └──── alimentam e validam ────┘
                  │
        DECISÃO DE PRODUTO
```

- **Markov gera o comportamento, Monte Carlo o simula.** Cadeias de Markov são frequentemente o "motor" dentro de uma simulação de Monte Carlo: você modela como o usuário transita entre páginas/estados (Markov) e roda milhares de simulações (Monte Carlo) para estimar resultados como conversão ou churn.
- **Monte Carlo planeja o teste A/B.** Antes de rodar um A/B caro, você pode *simular* o experimento via Monte Carlo para estimar quanto tempo ele levará para atingir significância e qual tamanho de amostra precisa.
- **Teste A/B é o juiz final.** Simulação prevê; o A/B *confirma na realidade* qual versão é melhor, com significância estatística.
- E lembrando o [Autoestudo 01 (Geração de Dados Sintéticos)](../autoestudo-01-geracao-de-dados-sinteticos/02-explicacao.md): os **dados sintéticos** que você gera para testar pipelines de A/B muitas vezes são produzidos exatamente por modelos *agent-based* e de simulação — ou seja, por Monte Carlo e Markov. Tudo se amarra.

---

## 6. Cases reais no mundo

- **Monte Carlo — finanças:** o cálculo de **Value at Risk (VaR)** em bancos roda simulações de Monte Carlo com centenas de fatores de risco para responder "qual a chance de eu perder mais de X amanhã?". A NASA usa para estimar risco de falha de missões; meteorologia usa para previsões probabilísticas ("70% de chance de chuva").
- **Markov — Google:** o algoritmo **PageRank** (que fez o Google) é uma cadeia de Markov gigante: modela um "surfista aleatório" clicando em links, e a probabilidade de ele acabar numa página define a relevância dela. O **Smart Compose** do Gmail também usa ideias de predição sequencial.
- **Teste A/B — os clássicos:** o Google testou **41 tons de azul** em links para achar o que gerava mais cliques (rendeu ~US$ 200 milhões/ano). A **Booking.com** roda milhares de testes A/B simultâneos. A campanha de **Obama em 2008** usou teste A/B na página de inscrição e aumentou cadastros em ~40%. A Microsoft (Bing) tem um time inteiro de experimentação onde mudanças triviais validadas por A/B renderam milhões.

---

## 7. Conexão com o módulo

- **Tema central:** este roadmap aponta direto para o **Teste A/B**, coração do Módulo 10, e prepara o terreno para o [Autoestudo 06 de Programação](../autoestudo-06-fundamentos-de-programacao-de-testes-ab/02-explicacao.md).
- **Trilha de Programação à frente:** Monte Carlo e Markov reaparecem aprofundados em **Prog-04 (Cadeias de Markov e o Comportamento do Usuário)**, **Prog-05/07 (Monte Carlo p/ Simulação de Cenários)** e **Prog-08 (Monte Carlo como Quantificação da Incerteza)**. Este autoestudo é a "porta de entrada" deles.
- **Matemática:** as **distribuições de probabilidade** (normal, uniforme, triangular) e o **intervalo de confiança / significância estatística** que aparecem aqui são exatamente o conteúdo de **Matemática-01 (Distribuições de Probabilidade)** e **Matemática-03 (Formulação de Hipóteses Estatísticas — Z-score e Teste t)**.
- **UX:** o teste A/B como método **comportamental/quantitativo/somativo** foi situado no mapa de pesquisa em [UX-01 (Métodos Mistos)](../../ux/autoestudo-01-metodos-mistos-de-exploracao-e-pesquisa/02-explicacao.md).

---

## 8. Resumo estruturado

- **O roadmap = 3 ferramentas contra a incerteza:** Monte Carlo (simular), Markov (sequenciar), Teste A/B (decidir).
- **Determinístico** (resposta única) **vs. estocástico/probabilístico** (distribuição de respostas com aleatoriedade).
- **Monte Carlo:** roda um modelo matemático milhares de vezes com entradas aleatórias (sorteadas de distribuições) → histograma de resultados. Mais simulações = mais precisão (ergodicidade). Componentes: entrada, modelo, saída.
- **Cadeias de Markov:** modelo estocástico onde **o futuro só depende do presente** (memorylessness). Definido por **matriz de transição** (linhas somam 1) + **vetor de estado inicial**. Ex.: autocomplete por frequência de palavras.
- **Teste A/B:** experimento controlado — **controle (A) vs. desafiante (B)**, divisão aleatória e simultânea. Regra de ouro: **um elemento por vez**. Só decida com **significância estatística** (intervalo de confiança ≥ 95%). Sem volume suficiente, não faça.
- **Conexão:** Markov vira motor de Monte Carlo; Monte Carlo dimensiona o A/B; A/B confirma na vida real. Dados sintéticos (Prog-01) saem desses mesmos modelos.

---

## 9. Auto-reflexão (pra pensar sozinha)

1. Você quer estimar a chance de uma nova cafeteria dar lucro no 1º ano. Quais seriam suas **variáveis de entrada**, qual o **modelo matemático**, e por que uma simulação de Monte Carlo te diria mais do que uma única previsão determinística?
2. A propriedade de **memorylessness** das Cadeias de Markov é uma simplificação. Pensa num caso de comportamento de usuário em que essa suposição ("o futuro só depende do agora") seria **boa** e um caso em que ela seria **ruim/enganosa**.
3. Um colega rodou um teste A/B, viu a versão B ganhar com 90% de confiança e quer publicá-la já. Usando o exemplo da moeda, que argumento você daria para ele esperar mais — e qual nível de confiança você exigiria?
