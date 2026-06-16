# Roadmap do Projeto (Perspectiva de Programação) — Material

> **Matéria:** Computação / Programação · **Autoestudo:** 02 · **Data:** 29/04/2026 · **Professor:** Jefferson de Oliveira Silva (Eixo COM)
>
> Compilação de três fontes-base que formam o "roadmap" técnico da trilha de Programação: Simulação de Monte Carlo (AWS), Cadeias de Markov (Built In) e Teste A/B (RD Station). Conteúdo limpo de navegação/rodapé. **Nota:** a terceira fonte (RD Station) chegou **truncada** no envio, cortada na seção de exemplos de teste A/B.

---

## Fonte 1 — AWS: *O que é a simulação de Monte Carlo?*

A simulação de Monte Carlo é uma **técnica matemática que prevê possíveis resultados de um evento incerto**. Programas de computador usam esse método para analisar dados passados e prever uma série de resultados futuros com base numa escolha de ação. Por exemplo, para estimar as vendas do primeiro mês de um novo produto, você fornece ao programa o histórico de vendas, e ele estima diferentes valores com base em fatores como condições de mercado, preço e orçamento de publicidade.

### Por que é importante?

É um **modelo probabilístico** que inclui um elemento de incerteza/aleatoriedade na previsão. Ao simular um resultado, você obtém resultados diferentes a cada vez. Ex.: a distância entre casa e trabalho é fixa, mas uma simulação probabilística prevê diferentes tempos de viagem considerando congestionamento, clima e avarias no veículo.

Em contraste, os **métodos convencionais de previsão são mais determinísticos**: dão uma resposta definitiva e não consideram a incerteza (podem indicar tempo mínimo e máximo, mas as duas respostas são menos precisas).

### Benefícios

Fornece **vários resultados possíveis e a probabilidade de cada um**, com base num grande conjunto de amostras de dados aleatórios. Oferece uma imagem mais compreensível do que a previsão determinística. Ex.: prever riscos financeiros requer analisar dezenas ou centenas de fatores de risco; analistas usam Monte Carlo para produzir a probabilidade de todos os resultados possíveis.

### História

John von Neumann e Stanislaw Ulam inventaram a simulação de Monte Carlo na **década de 1940**. O nome homenageia o famoso local de jogos em Mônaco, pois o método compartilha a característica aleatória da roleta.

### Casos de uso

- **Comercial:** projetar cenários realistas para decisões. Ex.: decidir se vale aumentar o orçamento de publicidade de um curso de ioga online, modelando variáveis incertas (taxa de assinatura, custo de publicidade, taxa de inscrição, retenção).
- **Finanças:** previsões de longo prazo sobre preços de ações; considerar fatores de mercado que causam mudanças drásticas no valor do investimento.
- **Jogos online:** regulamentos rígidos exigem software justo; programadores usam Monte Carlo para simular resultados e garantir jogo justo.
- **Engenharia:** simular a taxa de falha provável de um produto. Ex.: calcular a durabilidade de um motor em várias condições.

### Como funciona?

O princípio básico está na **ergodicidade**, que descreve o comportamento estatístico de um ponto móvel num sistema fechado. Num sistema ergódico, o ponto móvel acabará passando por todos os locais possíveis. O computador executa simulações suficientes para produzir o resultado final de diferentes entradas.

Exemplo do dado: um dado de seis lados tem 1/6 de chance de cair em cada número. Se você lançar seis vezes, talvez não caia em seis números diferentes. Mas ao rolar por tempo indeterminado, você alcança a probabilidade teórica de 1/6 para cada. **A precisão é proporcional ao número de simulações** — rodar 10 mil simulações é mais preciso que 100.

Usa **geradores de números aleatórios** (programas que produzem sequências imprevisíveis) para recriar a incerteza dos parâmetros de entrada.

### Monte Carlo vs. machine learning

Machine learning usa uma grande amostra de dados de entrada e saída (E/S) para treinar software a entender a correlação entre ambos. A simulação de Monte Carlo, por sua vez, usa amostras de dados de entrada e **um modelo matemático conhecido** para prever os resultados prováveis. Modelos de ML são usados para testar e confirmar os resultados das simulações de Monte Carlo.

### Componentes

- **Variáveis de entrada (input):** valores aleatórios que afetam o resultado. Ex.: qualidade de fabricação e temperatura influenciam a durabilidade de um smartphone. Expressas como um intervalo de amostras de valores aleatórios.
- **Variável de saída (output):** o resultado da análise. Ex.: a expectativa de vida de um dispositivo (seis meses, dois anos). Mostrada num histograma ou gráfico.
- **Modelo matemático:** equação que descreve a relação entre saída e entrada. Ex.: lucro = receita − despesas. O software substitui receitas e despesas por valores prováveis conforme a distribuição de probabilidade e repete a simulação. Pode levar horas quando há muitas variáveis aleatórias.

### Distribuições de probabilidade em Monte Carlo

Funções estatísticas que representam um intervalo de valores distribuídos entre limites. Podem ser **discretas** (números inteiros/sequência finita; cada valor tem probabilidade > 0; plotadas em tabela) ou **contínuas** (curva entre dois pontos no eixo x). Tipos comuns:

- **Distribuição normal (curva de sino):** formato simétrico de sino; representa a maioria dos eventos da vida real. Probabilidade alta na mediana, diminuindo nas extremidades. Ex.: peso dos alunos de uma sala.
- **Distribuição uniforme:** variáveis aleatórias com chance igual; aparecem como uma linha plana horizontal. Ex.: lançar um dado.
- **Distribuição triangular:** usa valores mínimo, máximo e mais provável (moda); pico no valor mais provável. Ex.: prever volumes de vendas.

### Etapas para realizar

1. **Estabelecer o modelo matemático** — definir a equação que reúne saída e entrada.
2. **Determinar os valores de entrada** — escolher as distribuições de probabilidade. Ex.: temperatura de um celular provavelmente é uma curva de sino.
3. **Criar um conjunto de dados de amostra** — grande conjunto aleatório baseado na distribuição (na faixa de 100 mil para resultados precisos).
4. **Configurar e executar o software de Monte Carlo** — usar amostras e modelo; aguardar os resultados.
5. **Analisar os resultados** — ver a distribuição no histograma; calcular média, desvio padrão e variância para verificar se está dentro da expectativa.

### Desafios

- **Altamente dependente dos valores de entrada e da distribuição** — erros na escolha da distribuição levam a resultados imprecisos.
- **Capacidade computacional excessiva** — pode levar horas ou dias num único computador.

### Como o AWS Batch ajuda

AWS Batch executa cargas de trabalho em lote e escala recursos de nuvem automaticamente para simulações de Monte Carlo, simulando sistemas complexos em menos tempo, sem gerenciamento manual de alocação de recursos nem instalação de software de lote separado.

---

## Fonte 2 — Built In: *Markov Chain Explained* (Vatsal Patel)

> Atualizado por Matthew Urwin, 22/10/2024.

### Definição

Uma **Cadeia de Markov (Markov chain)** é um **modelo estocástico (stochastic model)** que usa matemática para prever a probabilidade de uma sequência de eventos ocorrer com base no **evento mais recente**. Foi criada por Andrey Markov. Exemplo comum: o jeito como o Google prevê a próxima palavra da sua frase no Gmail. Até o algoritmo PageRank do Google é um tipo de cadeia de Markov.

O objetivo principal do processo de Markov é **identificar a probabilidade de transição de um estado para outro**. Um dos principais atrativos: o estado futuro de uma variável estocástica depende **apenas do seu estado presente**. (Variável estocástica = variável cujos valores dependem de ocorrências aleatórias.)

### Característica principal: ausência de memória (memorylessness)

A principal característica do processo de Markov é a **propriedade de ausência de memória (memorylessness)**. O modelo "esqueceu" em que estado o sistema esteve. As previsões dependem **somente do estado atual**, independentes de estados passados e futuros.

Isso é bênção e maldição. Ao prever palavras (como o Gmail), o benefício é que a previsão não depende de algo escrito parágrafos atrás. Mas você não consegue prever texto baseado no contexto de um estado anterior — problema comum em NLP (processamento de linguagem natural).

### Como criar um modelo de cadeia de Markov

Depende de duas peças-chave: a **matriz de transição** e o **vetor de estado inicial**.

**Matriz de transição (transition matrix):** denotada "P", é uma matriz NxN que representa a distribuição de probabilidade das transições de estado. A **soma das probabilidades em cada linha é 1** (matriz estocástica). Um grafo direcionado e conectado pode ser convertido numa matriz de transição: cada elemento representa um peso de probabilidade associado a uma aresta que conecta dois nós.

```
     +-----+-----+-----+
     |  A  |  B  |  C  |   - Representa a rede
+-----+-----+-----+-----+   - matriz de transição NxN
|  A  |  .2 |  .3 |  .5 |   - elementos guardam probabilidades
+-----+-----+-----+-----+   - soma da linha = 1
|  B  |  .6 |  0  |  .4 |   - .3 = probabilidade de A ir para B
+-----+-----+-----+-----+
|  C  |  .1 | .7  |  .2 |   - .7 = probabilidade de C ir para B
+-----+-----+-----+-----+
```
(Ex.: há 60% de chance de ir do estado B para o estado A.)

**Vetor de estado inicial (initial state vector):** denotado "S", é um vetor Nx1 que representa a distribuição de probabilidade de começar em cada um dos N estados possíveis.

Dadas essas duas dependências, o produto P × I determina o estado inicial. Para prever a probabilidade de estados futuros, eleva-se a matriz de transição P à "M-ésima" potência.

### Exemplo: predição de texto

Aplicação comum em data science. Suponha um grande corpo de texto: cada frase é uma sequência de palavras, cada palavra é um estado, e você associa a probabilidade de ir de um estado a outro. A forma mais simples de calcular essas probabilidades é pela **frequência** da palavra no corpus.

```
Hello --> ['Everyone', ',', 'Everyone', 'Everyone', 'There', 'There', 'There', ...]
```

Se houvesse 20 palavras na lista após "Hello":
```
P(palavra) = Frequência da Palavra / Número Total de Palavras na Lista
P(Everyone) = 9 / 20
P(,) = 1 / 20
P(There) = 10 / 20
```

O vetor de estado inicial estaria associado à probabilidade de todas as palavras com que você poderia começar a frase. Se "Hello" é a única palavra inicial, o vetor seria Nx1 com 100% da probabilidade na palavra "Hello".

### Implementação em Python (cadeia de Markov para gerar texto de Shakespeare)

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
        '''
        Mapeia cada palavra para uma chave cujos valores são as palavras que a seguem.
        Ex.: text = 'hello my name is V hello my name is G ...'
            >> {'hello': ['my', 'my', 'my'], 'my': ['name', 'name', 'current'],
                'name': ['is', 'is', 'is'], 'is': ['V', 'G', 'F', 'a'], ...}
        '''
        words = self.text.split(' ')
        markov_dict = defaultdict(list)
        # cria lista de todos os pares de palavras
        for current_word, next_word in zip(words[0:-1], words[1:]):
            markov_dict[current_word].append(next_word)
        markov_dict = dict(markov_dict)
        print('Successfully Trained')
        return markov_dict

def predict_words(chain, first_word, number_of_words=5):
    '''
    Dado o resultado de markov_model e o número de palavras, prevê a próxima palavra da sequência.
    Ex.: generate_sentence(chain, first_word='do', number_of_words=3) >> Do not fail.
    '''
    if first_word in list(chain.keys()):
        word1 = str(first_word)
        predictions = word1.capitalize()
        # Gera a segunda palavra da lista de valores. Define a nova palavra como a primeira. Repete.
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

**Resumo da fonte:** uma cadeia de Markov é um modelo estocástico que descreve a probabilidade de uma sequência de eventos com base no estado do evento anterior. Os dois componentes-chave são a matriz de transição e o vetor de estado inicial. Serve para tarefas como geração de texto.

### FAQ

- **Como cadeias de Markov são usadas na vida real?** Predição de texto do Gmail; também prever comportamento de usuário em redes sociais, tendências de mercado de ações e sequências de DNA.
- **Por que usar cadeias de Markov?** Em situações onde o próximo resultado é aleatório e o próximo estado depende só do estado atual.
- **Cadeia de Markov é IA?** Não é IA em si, mas é peça-chave em tecnologias de IA — processos de Markov ajudam a prever resultados, inclusive em IA generativa.

---

## Fonte 3 — RD Station: *O que é teste A/B, o que você pode testar e como começar a fazer*

> Autora: Bruna Dourado · 8 de maio de 2024.

Embora existam boas práticas no Marketing Digital, cada empresa tem seu próprio público. Por isso, somente a partir de testes é possível ter certeza sobre qual abordagem funciona melhor. Um dos testes mais conhecidos é o **teste A/B**, que divide o tráfego de uma página, email ou anúncio em duas versões: a atual e a "desafiante" (com modificações). Depois, mede-se qual versão apresenta maior taxa de conversão.

### O que é teste A/B?

Também conhecido como **teste split, teste de comparações ou teste de divisão**. Duas versões um pouco diferentes de um mesmo conteúdo são comparadas para determinar qual oferece melhores resultados. Usado para avaliar a eficácia de anúncios, landing pages, assuntos de email, fluxos de automação. Um grupo vê a versão "A", outro grupo similar vê a versão "B"; depois os resultados são comparados (taxa de cliques, taxa de conversão, tempo na página).

### Por que fazer testes A/B

Aumentar a conversão/engajamento é uma das dores mais comuns dos times de Marketing. Os testes A/B oferecem **feedback real de mercado, mensurado com precisão e baseado em dados** — não é uma pesquisa em que alguém responde uma coisa e faz outra. Como as versões são distribuídas **aleatoriamente no mesmo espaço de tempo**, não há risco de fatores externos influenciarem a conversão (ambiente controlado), tornando os resultados mais confiáveis.

### Onde os testes A/B podem ser utilizados

- **Anúncios:** textos, imagens, CTAs e posicionamentos (Google Ads, Redes Sociais).
- **Email Marketing:** assunto, conteúdo, CTAs, remetentes.
- **Landing Pages:** layouts, textos, cores, elementos visuais.
- **CTAs:** cor, texto, posicionamento, design dos botões.
- **Ofertas:** descontos, promoções, incentivos.
- **Segmentação:** diferentes segmentos de público.
- **Automação de Marketing:** tempo de espera, canal (email ou WhatsApp).

### O que testar (e a regra de ouro)

**Não se recomenda testar mais de um elemento por vez** — se você muda vários elementos, é impossível saber qual foi responsável pelo resultado. Itens que mais costumam alterar a conversão:
- imagens e vídeos;
- descrições da oferta;
- assuntos de Email Marketing;
- tamanho e campos do formulário;
- call-to-action (botões);
- headline (título em destaque);
- caminhos num fluxo de automação;
- indicadores de confiabilidade (depoimentos, certificados).

### Quando fazer

Quando há necessidade/potencial de otimizar uma métrica importante (acessos, aberturas, cliques, geração de Leads). Situações úteis: lançamento de campanha, otimização contínua, antes de mudanças significativas, e para validar/refutar hipóteses de melhoria.

### Quando NÃO fazer

- **Volume insuficiente:** é preciso um bom volume de acessos para validade estatística. Empresas iniciantes podem não ter número significativo de pessoas impactadas; falta de volume leva a decisões prematuras e incorretas. (Use uma calculadora de teste A/B para o tamanho da amostra.)
- **Prioridades:** é difícil encontrar variáveis que realmente fazem diferença; experimentos que fracassam ou têm diferença pouco relevante raramente são relatados. Iniciantes podem ter mais retorno terminando de montar a estrutura de Marketing Digital.

### Como saber a hora de parar — intervalo de confiança

Você para um teste A/B quando alcança o **intervalo de confiança (confidence interval)** necessário, pois a **significância estatística (statistical significance)** indica que os resultados são confiáveis e não aconteceram ao acaso.

**Exemplo da moeda:** se você joga uma moeda 200 vezes, teoricamente metade deveria ser cara. Suponha que deu cara 116 vezes (58%). Você pode afirmar que a moeda é tendenciosa? O intervalo de confiança quantifica a confiança no teste: indica a probabilidade de a variação entre controle (50% cara) e experimento (58% cara) representar de fato toda a população, e não um segmento tendencioso por acaso. O resultado de 58% tem intervalo de confiança de ~90% — **estatisticamente baixo**. Para validar um experimento, recomenda-se **95% ou mais**, sendo **99% um ótimo índice**.

**Por que tomar decisões a partir de dados relevantes** — exemplos de Landing Page:
- Cenário fraco: LP A = 500 visitantes, 46% conversão; LP B = 500 visitantes, 40% conversão; intervalo de confiança = 90% → sem relevância estatística (a nova página pode ter conversão semelhante ou menor).
- Cenário forte: LP A = 500 visitantes, 52% conversão; LP B = 500 visitantes, 40% conversão; intervalo de confiança = 99,9% → a diferença é estatisticamente relevante.

### Ferramentas de teste A/B

- **RD Station Marketing:** plataforma completa com vários tipos de teste A/B (ofertas, assuntos, textos, templates de email, landing pages, templates de WhatsApp).
- **Firebase:** plataforma do Google com infraestrutura de back-end para apps, inclusive testes.
- **VWO:** plataforma de testes para otimizar a jornada do público.

### Exemplos práticos (cases RD Station)

**Landing Page:** nos primeiros 7 dias de divulgação de um material rico, de 9.772 usuários só 2.916 converteram (29,84%); a meta era >30%. No Desktop a taxa era boa (37,69%), mas no Mobile só 24,9%. **Hipótese:** mover o formulário para a parte superior da página melhoraria a visualização/acessibilidade no mobile. Após 7 dias de teste no RD Station, a variante venceu com **45%** de conversão. Na semana seguinte: 10.267 usuários, 4.348 conversões = **42,35%** (69,26% via Mobile). A vencedora também elevou a conversão Desktop em 63,75%.

**Assunto de Email:** a Contacta Segurança Digital queria aumentar a taxa de abertura de emails de nutrição. Ao enviar um artigo sobre SSL, testou dois assuntos:
- "*|PRIMEIRO_NOME|*, você sabe o que é certificado SSL?"
- "Saiu no blog: O que é certificado SSL?"

Enviado para 469 contatos (50% versão A, 50% versão B); a abertura geral foi de **45,78%**, permitindo definir o melhor assunto e seguir com ele.

### Como fazer teste A/B no RD Station Marketing

Teste A/B de Landing Pages e Email está nos planos Pro e Advanced; o teste em fluxos de automação é exclusivo do Advanced.

- **Landing Pages:** ativar teste (botão "Criar Teste A/B" ao criar/editar) → editar a variação B (gera-se uma cópia exata da original; o formulário é o mesmo nas duas) → publicar a página → analisar após um período (ex.: 1 semana) nas estatísticas → definir vencedor. Para escolher qual versão exibir, usa-se um algoritmo de **randomização**. Só funciona com Landing Pages de conversão (não páginas de agradecimento).
- **Email Marketing:** ativar "Teste A/B para Assunto do email" → configurar as versões A e B do assunto → enviar/agendar normalmente (50% recebem A, 50% B, aleatoriamente) → analisar estatísticas (seletor de versão A, B ou geral). Atenção ao intervalo de confiança.
- **Automação de Marketing:** arrastar a ação "Teste A/B" para o fluxo → montar os caminhos A e B (ex.: email no A, email levemente diferente no B) → salvar e ativar (evitar editar os caminhos depois de iniciado) → analisar na aba de testes A/B → definir vencedor (o caminho perdedor fica desabilitado; Leads parados em esperas terminam o caminho em que estavam). Apenas um teste A/B por fluxo de cada vez.

### Faça seu teste A/B na prática

Existem diversas possibilidades de usar o teste A/B para otimizar resultados de Marketing. Mesmo já tendo aplicado as táticas mais conhecidas, sempre é possível testar variações e encontrar melhorias. O público tem particularidades que só se descobrem testando — pense em hipóteses que você pode testar para aumentar suas taxas de conversão.
