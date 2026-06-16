# Cadeias de Markov e o Comportamento do Usuário — Explicação

> **Matéria:** Computação / Programação · **Autoestudo:** 05 · **Data:** 13/05/2026 · **Professor:** Jefferson de Oliveira Silva
>
> Explicação do tutorial da DataCamp (ver [`01-material.md`](01-material.md)). É a **sequência direta** do [Prog-04 (Introdução às Cadeias de Markov)](../autoestudo-04-introducao-as-cadeias-de-markov/02-explicacao.md): aqui pegamos a teoria e a aplicamos a **comportamento**, com código rodando e as **propriedades formais** das cadeias.

---

## 1. Contexto geral: do "humor da CJ" ao comportamento do usuário

O tutorial usa um exemplo charmoso: a **CJ**, quando triste, ou dorme, ou corre, ou come sorvete — e o que ela faz amanhã depende do que fez hoje. Troque "CJ" por "usuário do seu app" e "dormir/correr/sorvete" por "Home / Produto / Carrinho", e você tem **exatamente** o que o título promete: modelar o **comportamento do usuário** como uma cadeia de Markov.

É essa a grande ideia deste autoestudo: a jornada de um usuário num produto digital é uma **sequência de estados** (telas, ações, status), e na maioria das vezes **o próximo passo depende principalmente de onde ele está agora**. Isso torna as cadeias de Markov uma ferramenta natural para responder perguntas de negócio como: *"de quem entra na Home, que fração chega à compra?"*, *"onde os usuários mais desistem?"*, *"se eu melhorar a página de Produto, quanto isso muda a conversão final?"*.

> O Prog-04 te deu os conceitos (estado, matriz de transição, memorylessness, distribuição estacionária). Aqui eu assumo isso e foco em: **(a)** aplicar a comportamento, **(b)** as propriedades formais que classificam uma cadeia, e **(c)** ver o código rodar e tocar a Lei dos Grandes Números.

---

## 2. Conceitos-chave

### 2.1. Recapitulando a propriedade de Markov (com a fórmula)

O tutorial traz a definição formal que vale internalizar:

```
Pr( Xn+1 = x | X1=x1, X2=x2, …, Xn=xn )  =  Pr( Xn+1 = x | Xn=xn )
```

Em português: a probabilidade do próximo estado, **dado todo o histórico**, é igual à probabilidade **dado só o estado atual**. Todo o passado (`X1…Xn-1`) é irrelevante. Aplicado a usuário: *para prever a próxima tela, basta saber em que tela ele está agora* — não importa o caminho que ele fez até ali. (É uma simplificação, e voltaremos à sua limitação.)

Um detalhe que o tutorial formaliza: a matriz de transição precisa ser uma **matriz estocástica** — cada **linha soma exatamente 1**, porque cada linha é a distribuição de probabilidade de "para onde vou a partir deste estado".

### 2.2. O exemplo trabalhado: prevendo 2 passos à frente

Esse cálculo é o coração do tutorial e merece atenção, porque é a mecânica de "prever o futuro" numa cadeia. Pergunta: começando em `Sleep`, qual a chance de estar em `Run` depois de **2 dias**?

Você **soma todos os caminhos** que levam de Sleep a Run em 2 passos:

| Caminho | Probabilidade |
|---|---|
| Sleep → Sleep → Run | 0,2 × 0,6 = 0,12 |
| Sleep → Run → Run | 0,6 × 0,6 = 0,36 |
| Sleep → Icecream → Run | 0,2 × 0,7 = 0,14 |
| **Total** | **0,62 (62%)** |

Repare que isso é **exatamente** o que significa "elevar a matriz ao quadrado" (`P²`), que vimos no Prog-04: multiplicar matrizes *é* somar todos os caminhos passando por estados intermediários. Aqui você vê a conta por extenso.

> **Tradução para usuário:** "de quem está na Home hoje, que fração estará no Carrinho depois de 2 cliques?" — mesma conta, somando todos os caminhos de 2 passos.

### 2.3. As 5 propriedades que classificam uma cadeia (o aprofundamento)

O Prog-04 mencionou tipos de estado de leve. O tutorial formaliza cinco propriedades — e elas têm leitura direta em comportamento do usuário:

| Propriedade | Definição | Leitura em "comportamento do usuário" |
|---|---|---|
| **Irredutibilidade (irreducibility)** | dá pra chegar a qualquer estado a partir de qualquer outro | de qualquer tela, o usuário consegue (com algum caminho) chegar a qualquer outra |
| **Periodicidade (periodicity)** | o estado só se repete em múltiplos de k > 1 | raro em UX; indicaria um ciclo rígido (ex.: um wizard que sempre volta de X em X passos) |
| **Transitoriedade (transience)** | partindo do estado, há chance de **nunca** voltar | telas de **onboarding / primeiro acesso** (você passa uma vez e não volta) |
| **Recorrência (recurrence)** | você sempre acaba voltando ao estado | a tela de **catálogo/busca**, revisitada o tempo todo |
| **Estado absorvente (absorbing)** | uma vez dentro, não sai (p_ii = 1) | **Compra concluída** ou **Churn (cancelamento)** — fim da jornada |
| **Ergodicidade (ergodicity)** | aperiódico + recorrente positivo (toda a cadeia, se irredutível e ergódica) | a cadeia tem um comportamento de equilíbrio estável de longo prazo (existe distribuição estacionária) |

> A **ergodicidade** é a ponte que justifica simular: numa cadeia ergódica, observar **uma** jornada longa revela as probabilidades de **todo** o sistema (vimos isso com rigor no [Matemática-02](../../matematica/autoestudo-02-processos-estocasticos-cadeias-de-markov-e-metodo-de-monte-carlo/02-explicacao.md)).

### 2.4. Duas formas de responder à mesma pergunta: analítica vs. simulação

O tutorial é genial porque mostra **duas rotas** para o mesmo 62%:

1. **Rota analítica (matemática):** somar os caminhos → 0,62 exato. Rápido e preciso, mas fica inviável de fazer "na mão" quando há muitos estados e muitos passos.
2. **Rota da simulação (Monte Carlo):** programe a cadeia, rode a jornada **10.000 vezes** aleatoriamente, conte quantas terminaram em `Run`, e divida. Resultado: **62,42%** — converge para os 62% teóricos.

Por que a simulação funciona? Pela **Lei dos Grandes Números (Law of Large Numbers)**: conforme o número de tentativas cresce, a frequência observada converge para a probabilidade verdadeira. **Aqui está, literalmente, a fusão dos dois pilares do módulo:** a **Cadeia de Markov** define as regras de transição; o **Monte Carlo** (rodar 10.000 simulações) estima o resultado. Markov + Monte Carlo, na prática, em ~20 linhas de Python.

### 2.5. A limitação honesta (e por que importa para usuário)

A memorylessness é uma simplificação poderosa, mas às vezes **enganosa para comportamento humano**. Exemplo: um usuário que chega ao carrinho na **10ª visita** provavelmente tem intenção de compra muito diferente de quem chega na **1ª** — mas o Markov "puro" os trata igual, porque só olha o estado atual. Quando o histórico importa, usa-se **cadeias de ordem superior** (olham os últimos 2-3 estados) ou modelos com memória (os Transformers, que vimos no Prog-02). Saber *quando a suposição de Markov quebra* é sinal de maturidade.

---

## 3. Exemplo prático: adaptando o código da CJ para um funil

O mesmo código do tutorial, com os estados trocados para uma jornada de usuário (a estrutura é idêntica):

```python
import numpy as np

estados = ["Home", "Produto", "Carrinho"]
# P[i][j] = probabilidade de ir do estado i para o estado j (cada linha soma 1)
P = [[0.3, 0.6, 0.1],   # de Home
     [0.2, 0.4, 0.4],   # de Produto
     [0.1, 0.3, 0.6]]   # de Carrinho

def simular_jornada(passos, inicio=0):
    atual = inicio
    caminho = [estados[atual]]
    for _ in range(passos):
        atual = np.random.choice(len(estados), p=P[atual])
        caminho.append(estados[atual])
    return caminho

# Rode 10.000 vezes e estime onde os usuários acabam após 2 cliques (Lei dos Grandes Números)
fim = [simular_jornada(2)[-1] for _ in range(10000)]
for e in estados:
    print(e, fim.count(e)/10000)
```

Esse mini-modelo já responde "de quem começa na Home, que fração está no Carrinho após 2 cliques?". **E a ponte com teste A/B:** se um teste A/B na página de Produto aumentar a transição `Produto→Carrinho` de 0,4 para 0,5, você muda *um número na matriz* e re-simula para **projetar** o impacto na conversão final — antes mesmo de o teste completo terminar.

---

## 4. Cases reais no mundo

- **PageRank (Google):** a aplicação mais famosa — o "surfista aleatório" navegando links é uma cadeia de Markov; a distribuição estacionária define a relevância das páginas.
- **Modelos de atribuição de marketing:** o Google Analytics tem um modelo de atribuição "baseado em cadeias de Markov" que distribui o crédito de uma conversão entre os canais (e-mail, busca, social) modelando a jornada como transições entre estados — exatamente o tema deste autoestudo.
- **Previsão de churn (SaaS):** empresas modelam a jornada do assinante com `Churn` como **estado absorvente** e calculam a probabilidade e o tempo esperado até o cancelamento.
- **Reddit Subreddit Simulator:** citado no próprio tutorial — gera posts e comentários automáticos via cadeias de Markov treinadas em texto real.

---

## 5. Conexão com o módulo

- **Prog-04 (Introdução às Cadeias de Markov):** este é o "nível 2" — pega a teoria e aplica a comportamento, com código e propriedades formais.
- **Prog-02 / Matemática-02 (Monte Carlo & Processos Estocásticos):** a simulação que aproxima os 62% é Monte Carlo puro, justificada pela **Lei dos Grandes Números**. Markov define as regras; Monte Carlo as roda.
- **Matemática-01 (Distribuições):** cada linha da matriz é uma distribuição de probabilidade; o resultado da simulação converge para a distribuição teórica.
- **Teste A/B (tema do módulo) e Negócios-01 (Experimentação):** modelar o funil como Markov permite **traduzir** o efeito local de um teste A/B (melhorar uma transição) em impacto **global** na conversão. É a ponte entre "a variante venceu" e "quanto isso vale no fim do funil".
- **UX (jornada e arquitetura da informação):** a sequência de telas que o usuário percorre é, ao mesmo tempo, objeto de UX e os "estados" da cadeia.

---

## 6. Resumo estruturado

- **Comportamento do usuário como cadeia de Markov:** telas/ações = **estados**; o próximo passo depende (sobretudo) só do estado atual.
- **Propriedade de Markov (fórmula):** `Pr(Xn+1 | todo o passado) = Pr(Xn+1 | Xn)`. Matriz de transição **estocástica** (linhas somam 1).
- **Prever n passos:** somar todos os caminhos = elevar a matriz à potência. Ex.: Sleep→Run em 2 dias = 62%.
- **5 propriedades:** irredutibilidade, periodicidade, transitoriedade/recorrência, **ergodicidade**, **estado absorvente** (Compra/Churn).
- **Duas rotas para a resposta:** analítica (somar caminhos) vs. **simulação Monte Carlo** (rodar 10.000 vezes → 62,42%), justificada pela **Lei dos Grandes Números**.
- **Limitação:** memorylessness ignora o histórico (1ª vs. 10ª visita) → ordem superior / Transformers quando o passado importa.
- **Aplicação-chave:** projetar o impacto de um teste A/B (mudança numa transição) na conversão final do funil.

---

## 7. Auto-reflexão (pra pensar sozinha)

1. No exemplo da CJ, refizemos a conta de "Sleep→Run em 2 dias = 62%" somando 3 caminhos. Tente, no papel, calcular a chance de "Sleep→Icecream em 2 dias". (Dica: liste os 3 caminhos e some os produtos.)
2. Por que rodar a simulação **10.000 vezes** dá ~62%, mas rodar só **10 vezes** daria um número instável e provavelmente errado? Qual lei explica isso — e como ela se conecta com o "volume mínimo" exigido num teste A/B?
3. Modelar a jornada do usuário com Markov assume que a 1ª e a 10ª visita ao carrinho são iguais. Dê um exemplo de produto onde essa suposição te levaria a uma conclusão errada sobre conversão.
