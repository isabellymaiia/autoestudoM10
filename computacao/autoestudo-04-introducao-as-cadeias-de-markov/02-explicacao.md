# Introdução às Cadeias de Markov — Explicação

> **Matéria:** Computação / Programação · **Autoestudo:** 04 · **Data:** 08/05/2026 · **Professor:** Jefferson de Oliveira Silva
>
> Este é o autoestudo **dedicado** às Cadeias de Markov. O [Prog-02 (Roadmap)](../autoestudo-02-roadmap-do-projeto-perspectiva-de-programacao/02-explicacao.md) já apresentou o básico (matriz de transição, memorylessness, vetor de estado inicial). Aqui eu **recapitulo rápido** e **aprofundo** com o que é novo: estados, grafo, transições de n passos, distribuição estacionária, tipos de estado e aplicação ao comportamento do usuário (que prepara o [Prog-05](../autoestudo-05-cadeias-de-markov-e-o-comportamento-do-usuario/02-explicacao.md)).

---

## 1. Contexto geral: recapitulando em 30 segundos

Uma **Cadeia de Markov** é um modelo de um sistema que **pula entre estados**, onde a probabilidade do próximo estado depende **só do estado atual** — não de todo o histórico. Essa é a famosa **propriedade de Markov** ou **ausência de memória (memorylessness)**.

A analogia do Banco Imobiliário do Prog-02 continua valendo: a próxima casa depende só de onde você está *agora* + o dado. Mas agora vamos abrir a "caixa-preta" e entender os mecanismos com mais profundidade — e, principalmente, **por que isso é tão útil para modelar usuários** num produto digital (e, portanto, para o teste A/B).

> Se você ainda não está confortável com "matriz de transição" e "vetor de estado inicial", vale reler a seção 3 do Prog-02 antes de continuar. Aqui eu assumo esse básico e construo por cima.

---

## 2. Conceitos-chave (aprofundando)

### 2.1. Estados e o grafo de transição

A forma mais intuitiva de enxergar uma cadeia de Markov é como um **grafo direcionado**:
- Cada **estado (state)** é um **nó** (um círculo). Estado = uma "situação" em que o sistema pode estar (Ensolarado/Chuvoso; ou página Home/Produto/Carrinho/Compra).
- Cada **transição** é uma **seta** com uma probabilidade.
- **Regra inviolável:** as setas que *saem* de um nó **somam 1** (você *tem* que ir para algum lugar — inclusive de volta para si mesmo).

```
        0.8
      ┌─────┐
      ▼     │
   ☀ Ensolarado ──0.2──▶ ☂ Chuvoso
        ▲                   │
        └────────0.4────────┘
              (Chuvoso→Chuvoso: 0.6)
```

Esse desenho **é** a cadeia de Markov. A matriz de transição é só a mesma informação numa tabela:

|  | →Ensolarado | →Chuvoso |
|---|---|---|
| **Ensolarado** | 0,8 | 0,2 |
| **Chuvoso** | 0,4 | 0,6 |

### 2.2. Prevendo o futuro: transições de n passos

Aqui está algo que o Prog-02 só mencionou de passagem e que vale destrinchar. A matriz de transição `P` te dá a probabilidade de **1 passo** no futuro. E se você quiser saber a probabilidade daqui a **2 passos**? Daqui a **10**?

A resposta é elegante: **eleve a matriz à potência**. `P²` te dá as probabilidades de 2 passos, `P³` de 3 passos, `Pⁿ` de n passos.

> **Por que isso funciona (intuição):** ir de A para C em dois passos é "somar todos os caminhos possíveis passando por algum estado intermediário" — A→A→C, A→B→C, A→C→C. Multiplicar a matriz por ela mesma faz exatamente essa soma de probabilidades de caminhos. (É a mesma lógica de multiplicação de matrizes que você vê em álgebra linear.)

**Exemplo concreto:** se hoje está ensolarado, qual a chance de estar chuvoso **depois de amanhã** (2 dias)?
- Caminho 1: Ensolarado→Ensolarado→Chuvoso = 0,8 × 0,2 = 0,16
- Caminho 2: Ensolarado→Chuvoso→Chuvoso = 0,2 × 0,6 = 0,12
- Total = **0,28** (28%). Isso é o elemento [Ensolarado][Chuvoso] da matriz `P²`.

### 2.3. A distribuição estacionária (stationary distribution) — o conceito novo mais importante

Esse é o conceito que diferencia uma introdução "de verdade" de uma superficial. Pergunta: se você rodar a cadeia por **muitos e muitos passos**, o que acontece?

Resposta surpreendente: na maioria das cadeias, as probabilidades de estar em cada estado **se estabilizam num valor fixo — e esse valor não depende de onde você começou.** Esse equilíbrio de longo prazo é a **distribuição estacionária (stationary distribution)**.

> **Analogia:** imagine um shopping com várias lojas. De manhã, todo mundo entra pela porta principal (estado inicial concentrado). Mas depois de horas circulando, a fração de pessoas em cada loja se estabiliza — sempre ~10% na praça de alimentação, ~5% na livraria, etc. — independentemente de por onde entraram. Essa "foto de equilíbrio" é a distribuição estacionária.

Por que isso importa para negócio/produto?
- No clima: "no longo prazo, qual fração dos dias é chuvosa?" → a distribuição estacionária.
- Em um site: "no equilíbrio, qual fração do tempo os usuários passam em cada página?" → ajuda a dimensionar servidores, priorizar páginas.
- **PageRank do Google é literalmente uma distribuição estacionária:** a probabilidade de um "surfista aleatório" acabar em cada página da web no longo prazo. Páginas com maior probabilidade estacionária = mais "importantes" = aparecem primeiro.

### 2.4. Tipos de estado (vocabulário que enriquece a análise)

Nem todo estado se comporta igual. Três tipos que vale conhecer:
- **Estado recorrente (recurrent):** se você sai dele, vai acabar voltando (cedo ou tarde). Ex.: "navegando o catálogo" — o usuário volta a essa página várias vezes.
- **Estado transiente (transient):** depois de sair, há chance de **nunca mais voltar**. Ex.: a tela de "primeiro acesso/onboarding".
- **Estado absorvente (absorbing):** uma vez que entra, **nunca sai** (probabilidade 1 de continuar nele). Ex.: "Compra concluída" ou "Cancelou a conta (churn)". É o fim da jornada.

> Estados absorventes são ouro para análise de produto: "qual a probabilidade de um usuário acabar no estado *Compra* vs. no estado *Abandono*, e em quantos passos?" é uma pergunta clássica de cadeia de Markov com estados absorventes.

### 2.5. A força e a fraqueza (revisitando a memorylessness com olhos críticos)

A **ausência de memória** é a grande simplificação que torna Markov tratável — e também sua maior limitação:
- **Força:** simples, rápido, precisa de poucos dados (só as transições de 1 passo). Funciona surpreendentemente bem para muitos sistemas.
- **Fraqueza:** assume que o passado não importa além do presente. Mas e se o comportamento do usuário depende de quantas vezes ele já visitou? Markov "puro" não captura isso. Soluções: **cadeias de Markov de ordem superior (higher-order)**, que olham os últimos 2, 3 estados — ao custo de explodir o tamanho da matriz. (É por essa limitação que os **Transformers**, com atenção de longo alcance, dominaram a geração de texto, como vimos no Prog-02.)

---

## 3. Exemplo prático: um mini-funil de e-commerce como cadeia de Markov

Vamos modelar a jornada num site de compras. Estados: `Home`, `Produto`, `Carrinho`, `Compra` (absorvente), `Saiu` (absorvente).

```python
import numpy as np

estados = ['Home', 'Produto', 'Carrinho', 'Compra', 'Saiu']

# Matriz de transição (cada linha soma 1)
P = np.array([
    # Home  Prod  Cart  Compra Saiu
    [0.10, 0.50, 0.00, 0.00, 0.40],  # de Home
    [0.20, 0.30, 0.30, 0.00, 0.20],  # de Produto
    [0.00, 0.10, 0.20, 0.50, 0.20],  # de Carrinho
    [0.00, 0.00, 0.00, 1.00, 0.00],  # Compra (absorvente)
    [0.00, 0.00, 0.00, 0.00, 1.00],  # Saiu (absorvente)
])

# Todo mundo começa na Home
s = np.array([1, 0, 0, 0, 0])

# Para onde estão os usuários após 5 passos?
for passo in range(5):
    s = s @ P
print(dict(zip(estados, s.round(3))))
# Mostra a fração que já comprou, ainda navega, ou saiu.
```

Esse modelo responde perguntas de negócio direto: *"que fração dos visitantes acaba comprando?"*, *"em qual etapa eles mais abandonam?"*. **E a ponte com teste A/B:** se você mudar a página de Produto (um teste A/B!) e isso aumentar a probabilidade de transição `Produto→Carrinho`, você pode **simular** (com a cadeia + Monte Carlo, do Prog-02) o impacto disso na taxa de compra final — antes mesmo de o resultado completo do teste sair.

---

## 4. Cases reais no mundo

- **Google PageRank:** o algoritmo que fundou o Google é uma cadeia de Markov gigante (cada página da web é um estado). A distribuição estacionária do "surfista aleatório" define a relevância. Talvez a aplicação de Markov mais valiosa da história.
- **Gmail / teclados de celular:** o autocomplete e a sugestão de próxima palavra usam predição sequencial no espírito de Markov (hoje turbinada por redes neurais).
- **Análise de jornada e churn:** empresas de SaaS modelam a jornada do cliente como cadeia de Markov para prever **churn** (cancelamento — um estado absorvente) e atribuir conversões a canais de marketing (o modelo de atribuição "Markov chains" do Google Analytics faz isso).
- **Spotify / Netflix:** sequências de músicas/episódios assistidos podem ser modeladas como transições entre estados para recomendar o "próximo".

---

## 5. Conexão com o módulo

- **Prog-02 (Roadmap):** apresentou Markov como um dos três pilares. Este autoestudo aprofunda o pilar.
- **Prog-05 (Cadeias de Markov e o Comportamento do Usuário):** é a sequência natural — pega tudo isto e aplica diretamente a modelar usuários, como no exemplo do funil acima.
- **Prog-07/08 (Monte Carlo):** Markov define *as regras* de transição; Monte Carlo *roda* milhares de jornadas seguindo essas regras para estimar resultados. Dupla inseparável.
- **Matemática-01 (Distribuições):** o vetor de estado é uma **distribuição de probabilidade** sobre os estados; a distribuição estacionária é seu equilíbrio. E **Matemática-02 (Processos Estocásticos)** é o guarda-chuva teórico que contém as cadeias de Markov.
- **Teste A/B (tema do módulo):** mudanças testadas via A/B alteram probabilidades de transição; modelar o funil como Markov permite *projetar* o impacto de uma variante na conversão final.

---

## 6. Resumo estruturado

- **Cadeia de Markov** = sistema que pula entre **estados**; o próximo depende **só do atual** (memorylessness).
- **Grafo de transição:** nós = estados, setas = probabilidades; setas que saem de um nó **somam 1**. Mesma info que a **matriz de transição P**.
- **n passos:** `Pⁿ` dá as probabilidades de transição depois de n passos (soma de todos os caminhos).
- **Distribuição estacionária:** o equilíbrio de longo prazo, **independente do início**. É o que o **PageRank** calcula.
- **Tipos de estado:** recorrente (volta), transiente (pode não voltar), **absorvente** (não sai — ex.: Compra, Churn).
- **Força:** simples, poucos dados. **Fraqueza:** ignora o passado distante (daí ordem superior / Transformers).
- **Aplicação:** funis, jornada do usuário, churn, atribuição — e simular o impacto de testes A/B na conversão.

---

## 7. Auto-reflexão (pra pensar sozinha)

1. No grafo do clima (Ensolarado 0,8/0,2; Chuvoso 0,4/0,6), sem fazer a conta exata: você acha que, no longo prazo, há mais dias ensolarados ou chuvosos? Por quê? (Dica: olhe quais transições são mais "fortes".)
2. Por que "Compra concluída" e "Cancelou a conta" são modelados como estados **absorventes**, e por que isso é útil para um negócio querer calcular a probabilidade de cair em cada um?
3. A propriedade de memorylessness assume que dá no mesmo um usuário ter chegado ao carrinho na 1ª visita ou na 10ª. Em que situação real essa suposição te enganaria — e como uma cadeia de "ordem superior" ajudaria?
