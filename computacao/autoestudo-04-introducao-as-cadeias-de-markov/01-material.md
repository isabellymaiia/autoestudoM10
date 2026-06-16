# Introdução às Cadeias de Markov — Material

> **Matéria:** Computação / Programação · **Autoestudo:** 04 · **Data:** 08/05/2026 · **Professor:** Jefferson de Oliveira Silva (Eixo COM)
>
> Duas fontes. A primeira (vídeo) **não teve transcrição fornecida** — reconstrução temática. A segunda (Built In) é o mesmo artigo já usado no [Prog-02](../autoestudo-02-roadmap-do-projeto-perspectiva-de-programacao/01-material.md) (Fonte 2); reproduzido aqui por ser a fonte oficial deste autoestudo dedicado.

---

## Fonte 1 — Vídeo: *Cadeias de Markov Claramente Explicadas*

> ⚠️ **Transcrição não fornecida.** Reconstrução temática (não literal), no espírito de canais didáticos como o Normalized Nerd / StatQuest.

- Uma **Cadeia de Markov** é um modelo de um sistema que pula entre **estados (states)**, onde a probabilidade do próximo estado depende **apenas do estado atual**.
- Tudo é representado por um **grafo direcionado**: cada **nó** é um estado, cada **seta (aresta)** tem uma probabilidade de transição. As setas que saem de um nó **somam 1**.
- Exemplo didático típico: prever o clima. Estados = {Ensolarado, Chuvoso}. "Se hoje está ensolarado, há 80% de chance de amanhã também estar; 20% de chuva." Isso vira uma matriz de probabilidades.
- A **matriz de transição** organiza todas essas probabilidades. Multiplicando o estado atual pela matriz, prevê-se o próximo; repetindo, prevê-se vários passos à frente.
- Conforme você avança muitos passos, a cadeia tende a uma **distribuição estacionária (stationary distribution)** — as probabilidades de estar em cada estado se estabilizam, independentemente de onde você começou.
- Aplicações citadas: predição de texto, comportamento de usuários, PageRank do Google, previsão do tempo, modelos financeiros.

---

## Fonte 2 — Built In: *Markov Chain Explained* (Vatsal Patel)

> Atualizado por Matthew Urwin, 22/10/2024. *(Mesmo artigo da Fonte 2 do Prog-02.)*

### Definição

Uma **Cadeia de Markov (Markov chain)** é um **modelo estocástico (stochastic model)** que usa matemática para prever a probabilidade de uma sequência de eventos com base no **evento mais recente**. Criada por Andrey Markov. Exemplo comum: o Google prevendo a próxima palavra no Gmail. Até o **PageRank** do Google é um tipo de cadeia de Markov.

O objetivo principal do processo de Markov é **identificar a probabilidade de transição de um estado para outro**. Um dos principais atrativos: o estado futuro de uma variável estocástica depende **apenas do seu estado presente**. (Variável estocástica = variável cujos valores dependem de ocorrências aleatórias.)

### Característica principal: ausência de memória (memorylessness)

A propriedade de **ausência de memória (memorylessness)**: o modelo "esqueceu" em que estado o sistema esteve. As previsões dependem **somente do estado atual**, independentes de estados passados e futuros.

Bênção e maldição: ao prever palavras (como o Gmail), a previsão não depende de algo escrito parágrafos atrás (bom), mas também não consegue usar contexto distante (ruim) — problema comum em NLP.

### Como criar um modelo de cadeia de Markov

Depende de duas peças: a **matriz de transição** e o **vetor de estado inicial**.

**Matriz de transição (transition matrix), "P":** matriz NxN que representa a distribuição de probabilidade das transições. A **soma de cada linha é 1** (matriz estocástica). Um grafo direcionado conectado vira uma matriz de transição; cada elemento é o peso de probabilidade de uma aresta entre dois nós.

```
     +-----+-----+-----+
     |  A  |  B  |  C  |
+-----+-----+-----+-----+
|  A  |  .2 |  .3 |  .5 |   - soma da linha = 1
+-----+-----+-----+-----+   - .3 = probabilidade de A ir para B
|  B  |  .6 |  0  |  .4 |
+-----+-----+-----+-----+
|  C  |  .1 | .7  |  .2 |   - .7 = probabilidade de C ir para B
+-----+-----+-----+-----+
```
(Ex.: 60% de chance de ir de B para A.)

**Vetor de estado inicial (initial state vector), "S":** vetor Nx1 com a probabilidade de começar em cada um dos N estados.

Com os dois, o produto P × I determina o estado inicial; para prever estados futuros, eleva-se P à **M-ésima potência**.

### Exemplo: predição de texto

Cada palavra é um estado; a probabilidade de ir de uma palavra a outra é calculada pela **frequência** no corpus:
```
Hello --> ['Everyone', ',', 'Everyone', 'Everyone', 'There', 'There', 'There', ...]
P(palavra) = Frequência da Palavra / Total de Palavras na Lista
P(Everyone) = 9 / 20 ;  P(,) = 1 / 20 ;  P(There) = 10 / 20
```
Se "Hello" é a única palavra inicial, o vetor de estado inicial é Nx1 com 100% em "Hello".

### Implementação em Python (gerar texto estilo Shakespeare)

```python
from collections import defaultdict
import string
import random

class Markov():
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self.remove_punctuations(self.get_text())
        self.model = self.model()

    def get_text(self):
        '''Lê o arquivo e retorna o texto linha por linha numa lista'''
        text = []
        for line in open(self.file_path):
            text.append(line)
        return ' '.join(text)

    def remove_punctuations(self, text):
        '''Retorna o texto sem pontuações'''
        return text.translate(str.maketrans('','', string.punctuation))

    def model(self):
        '''Mapeia cada palavra às palavras que a seguem (chave -> lista de próximas)'''
        words = self.text.split(' ')
        markov_dict = defaultdict(list)
        for current_word, next_word in zip(words[0:-1], words[1:]):
            markov_dict[current_word].append(next_word)
        markov_dict = dict(markov_dict)
        print('Successfully Trained')
        return markov_dict

def predict_words(chain, first_word, number_of_words=5):
    '''Prevê a próxima palavra da sequência a partir de first_word'''
    if first_word in list(chain.keys()):
        word1 = str(first_word)
        predictions = word1.capitalize()
        for i in range(number_of_words-1):
            word2 = random.choice(chain[word1])
            word1 = word2
            predictions += ' ' + word2
        predictions += '.'
        return predictions
    else:
        return "Word not in corpus"

if __name__ == '__main__':
    m = Markov(file_path='Shakespeare.txt')
    chain = m.model
    print(predict_words(chain, first_word='do', number_of_words=10))
```

### FAQ

- **Vida real:** predição de texto do Gmail; comportamento de usuário em redes sociais; tendências de ações; sequências de DNA.
- **Por que usar:** quando o próximo resultado é aleatório e depende só do estado atual.
- **É IA?** Não em si, mas é peça-chave em tecnologias de IA, inclusive IA generativa.
