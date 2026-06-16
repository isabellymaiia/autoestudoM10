# Cadeias de Markov e o Comportamento do Usuário — Material

> **Matéria:** Computação / Programação · **Autoestudo:** 05 · **Data:** 13/05/2026 · **Professor:** Jefferson de Oliveira Silva (Eixo COM)
>
> Fonte única: tutorial *"Markov Chains in Python: Beginner Tutorial"*, de Sejal Jaiswal (DataCamp, 31/12/2019). Conteúdo traduzido/estruturado e limpo de navegação/rodapé, preservando o substantivo e o código.

---

## Markov Chains in Python: Beginner Tutorial

Uma **Cadeia de Markov (Markov chain)** é um sistema matemático geralmente definido como uma **coleção de variáveis aleatórias** que transitam de um estado para outro segundo certas regras probabilísticas. Esse conjunto de transições satisfaz a **Propriedade de Markov**: a probabilidade de transitar para qualquer estado em particular depende **somente do estado atual e do tempo decorrido**, e não da sequência de estados que o precedeu. Essa característica única torna os processos de Markov **sem memória (memoryless)**.

### Por que Cadeias de Markov?

Têm uso prolífico em matemática, economia, teoria dos jogos, teoria da comunicação, genética e finanças. Surgem amplamente em estatística (especialmente **estatística bayesiana**) e contextos da teoria da informação. Em problemas do mundo real: estudar sistemas de controle de cruzeiro em veículos, filas de clientes chegando a um aeroporto, taxas de câmbio, etc. O algoritmo **PageRank** (proposto para o motor de busca do Google) é baseado num processo de Markov. O *Subreddit Simulator* do Reddit gera submissões e comentários aleatórios usando cadeias de Markov.

### Cadeia de Markov

Uma cadeia de Markov é um **processo aleatório (random/stochastic process)** com a propriedade de Markov — um objeto matemático definido como uma coleção de variáveis aleatórias. Tem **espaço de estados discreto** (conjunto de valores possíveis) ou **conjunto de índices discreto** (geralmente representando o tempo). Normalmente, o termo "cadeia de Markov" é reservado para um processo com tempo discreto: a **Cadeia de Markov de Tempo Discreto (Discrete Time Markov Chain, DTMC)**.

### Cadeia de Markov de Tempo Discreto (DTMC)

Envolve um sistema que está em certo estado a cada passo, com o estado mudando aleatoriamente entre passos. Os passos costumam ser pensados como momentos no tempo (mas poderiam ser distância física ou outra medida discreta). É uma sequência de variáveis aleatórias X1, X2, X3, … com a propriedade de Markov, tal que a probabilidade de ir para o próximo estado depende **apenas do estado presente**:

```
Pr( Xn+1 = x | X1 = x1, X2 = x2, …, Xn = xn ) = Pr( Xn+1 = x | Xn = xn )
```

A probabilidade de Xn+1 depende só de Xn que o precede. Conhecer o estado anterior é tudo o que é necessário para determinar a distribuição de probabilidade do estado atual (regra da **independência condicional**).

Os valores possíveis de Xi formam um conjunto contável **S**, o **espaço de estados (state space)** da cadeia. O espaço de estados pode ser qualquer coisa: letras, números, placares de basquete ou condições do tempo. Muitas aplicações usam espaços de estados finitos ou contavelmente infinitos, por terem análise estatística mais direta.

### Modelo

Uma cadeia de Markov é representada por um **autômato probabilístico**. As mudanças de estado são chamadas **transições**; as probabilidades associadas são as **probabilidades de transição**. Pode ser visto como uma sequência de **grafos direcionados**, onde as arestas do grafo n são rotuladas pelas probabilidades de ir de um estado no tempo n para os outros estados no tempo n+1. A mesma informação é representada pela **matriz de transição**.

Se a cadeia tem N estados possíveis, a matriz é NxN, tal que a entrada (I, J) é a probabilidade de transitar do estado I para o estado J. Além disso, a matriz de transição deve ser uma **matriz estocástica (stochastic matrix)**: as entradas de **cada linha somam exatamente 1** (cada linha representa sua própria distribuição de probabilidade).

O modelo é caracterizado por: um **espaço de estados**, uma **matriz de transição** e um **estado inicial** (dado pela distribuição inicial).

### Exemplo: o humor da CJ

Quando a CJ está triste (o que não é muito usual), ela faz uma de três coisas: vai correr, devora sorvete ou tira uma soneca. A partir de dados históricos:
- Se passou o dia **dormindo (Sleep)**: no dia seguinte, 60% de chance de correr, 20% de continuar dormindo, 20% de comer sorvete.
- Se foi **correr (Run)**: 60% de correr de novo, 30% de sorvete, 10% de dormir.
- Se comeu **sorvete (Icecream)**: 10% de sorvete de novo, 70% de correr, 20% de dormir.

Três estados: `Sleep`, `Run`, `Icecream`. A matriz de transição é 3x3. As setas que saem de um estado somam exatamente 1; idem as linhas da matriz.

**Pergunta:** "Começando no estado `Sleep`, qual a probabilidade de a CJ estar correndo (`Run`) ao fim de 2 dias de tristeza?"

Caminhos possíveis de `Sleep` → `Run` em 2 passos:
- Sleep→Sleep→Run = 0,2 · 0,6
- Sleep→Run→Run = 0,6 · 0,6
- Sleep→Icecream→Run = 0,2 · 0,7

Probabilidade total = (0,2·0,6) + (0,6·0,6) + (0,2·0,7) = **0,62** → **62%** de chance de estar correndo após 2 dias, começando em Sleep.

### Propriedades importantes das cadeias de Markov

- **Redutibilidade (Reducibility):** uma cadeia é **irredutível** se é possível chegar a qualquer estado a partir de qualquer estado (existe um caminho com probabilidade positiva entre quaisquer dois estados).
- **Periodicidade (Periodicity):** um estado é **periódico** se a cadeia só pode retornar a ele em múltiplos de algum inteiro k > 1. É **aperiódico** se k = 1.
- **Transitoriedade e Recorrência (Transience and Recurrence):** um estado 'i' é **transiente** se, partindo de 'i', há probabilidade não-nula de **nunca** retornar a 'i'. É **recorrente (persistente)** caso contrário. Recorrente **positivo** se espera-se retornar em número finito de passos; **nulo** caso contrário.
- **Ergodicidade (Ergodicity):** um estado é **ergódico** se é aperiódico e recorrente positivo. Se todos os estados de uma cadeia irredutível são ergódicos, a cadeia é ergódica.
- **Estado absorvente (Absorbing State):** um estado 'i' é **absorvente** se é impossível sair dele (p_ii = 1 e p_ij = 0 para i ≠ j). Se todo estado pode alcançar um estado absorvente, a cadeia é uma **cadeia de Markov absorvente**.

### Cadeias de Markov em Python

```python
import numpy as np
import random as rm

# O espaço de estados
states = ["Sleep","Icecream","Run"]

# Sequências possíveis de eventos
transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

# Matriz de transição (probabilidades)
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]
```

Sempre garanta que as probabilidades somem 1:

```python
if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
    print("Somewhere, something went wrong. Transition matrix, perhaps?")
else: print("All is gonna be okay, you should move on!! ;)")
```

A função que prevê a sequência de estados (humor) usando `numpy.random.choice` (o argumento `p` recebe a distribuição de probabilidade, isto é, a linha da matriz de transição):

```python
def activity_forecast(days):
    activityToday = "Sleep"
    print("Start state: " + activityToday)
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2; activityList.append("Sleep"); pass
            elif change == "SR":
                prob = prob * 0.6; activityToday = "Run"; activityList.append("Run")
            else:
                prob = prob * 0.2; activityToday = "Icecream"; activityList.append("Icecream")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.5; activityList.append("Run"); pass
            elif change == "RS":
                prob = prob * 0.2; activityToday = "Sleep"; activityList.append("Sleep")
            else:
                prob = prob * 0.3; activityToday = "Icecream"; activityList.append("Icecream")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "II":
                prob = prob * 0.1; activityList.append("Icecream"); pass
            elif change == "IS":
                prob = prob * 0.2; activityToday = "Sleep"; activityList.append("Sleep")
            else:
                prob = prob * 0.7; activityToday = "Run"; activityList.append("Run")
        i += 1
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

activity_forecast(2)
```

Saída exemplo:
```
Start state: Sleep
Possible states: ['Sleep', 'Sleep', 'Run']
End state after 2 days: Run
Probability of the possible sequence of states: 0.12
```

Para aproximar a probabilidade teórica de 62%, repete-se a simulação milhares de vezes e conta-se a fração que termina em `Run`:

```python
# (mesma activity_forecast, mas retornando activityList em vez de imprimir)
list_activity = []
count = 0
for iterations in range(1,10000):
        list_activity.append(activity_forecast(2))
for smaller_list in list_activity:
    if(smaller_list[2] == "Run"):
        count += 1
percentage = (count/10000) * 100
print("The probability of starting at state:'Sleep' and ending at state:'Run'= " + str(percentage) + "%")
# Saída: ~62.42%
```

### Nota — Lei dos Grandes Números

Como aproximamos os 62%? Isso é a **Lei dos Grandes Números (law of large numbers)**: as frequências de eventos com a mesma probabilidade de ocorrência se equilibram, **mas só se houver tentativas suficientes**. Em outras palavras, conforme o número de experimentos aumenta, a proporção real de resultados converge para a proporção teórica/esperada.

### Conclusão

Cadeias de Markov simples são um dos tópicos fundamentais para começar com data science em Python. Foram introduzidas a cadeia de Markov e algumas de suas propriedades.

> *Autora: Sejal Jaiswal — Software Developer, Data Scientist.*
