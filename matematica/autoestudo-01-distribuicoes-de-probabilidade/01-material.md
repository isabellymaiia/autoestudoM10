# Distribuições de Probabilidade — Material

> **Matéria:** Matemática · **Autoestudo:** 01 · **Data:** 06/05/2026 · **Professor:** Diogo Martins Gonçalves de Morais (Eixo MTF)
>
> ⚠️ **Material original não fornecido.** Os autoestudos referenciados são vídeos do canal **StatQuest** (Josh Starmer). Como as transcrições não foram disponibilizadas, o que segue é uma **reconstrução/resumo do conteúdo conhecido desses vídeos**, com base no estilo e na abordagem consagrados do StatQuest — **não é uma transcrição literal**. Substituir por versão fiel quando o material original estiver disponível.

## Fontes referenciadas

1. **Vídeo 1 — "O que é uma distribuição estatística?"** (StatQuest: *What is a statistical distribution?*)
2. **Vídeo 2 — "The Normal Distribution, Clearly Explained!!!"** (StatQuest)

---

## Resumo reconstruído — Vídeo 1: O que é uma distribuição estatística?

> Reconstrução temática (não literal).

- A motivação começa com **medições**: imagine medir a altura (ou qualquer característica) de muitas pessoas. Cada medição é um valor.
- Para visualizar muitos valores, construímos um **histograma**: dividimos o eixo dos valores em "caixas" (bins) e contamos quantas medições caem em cada caixa. As barras mais altas indicam os valores mais comuns.
- À medida que coletamos **mais e mais dados** e usamos caixas cada vez mais finas, o "contorno" do histograma tende a se aproximar de uma **curva suave**. Essa curva é a **distribuição**.
- Uma **distribuição** descreve, portanto, **quão frequentes (ou prováveis) são os diferentes valores** que uma variável pode assumir. Ela responde: "onde os dados se concentram?" e "quão espalhados eles estão?".
- Distinção entre **dados discretos** (valores contáveis: número de filhos, resultado de um dado) e **dados contínuos** (qualquer valor num intervalo: altura, peso, tempo).
- A distribuição permite **fazer previsões** sobre a probabilidade de futuras medições caírem em determinada faixa, mesmo sem ter medido todo mundo.
- Existem **várias formas** de distribuição (simétrica, assimétrica, com um pico, com dois picos etc.). A forma depende do fenômeno que gera os dados.

---

## Resumo reconstruído — Vídeo 2: The Normal Distribution, Clearly Explained!!!

> Reconstrução temática (não literal).

- A **distribuição normal (normal distribution)**, também chamada de **distribuição gaussiana (Gaussian distribution)** ou **curva de sino (bell curve)**, é a distribuição mais comum e importante da estatística.
- Tem o formato de um **sino simétrico**: o pico fica no centro, e a curva decai igualmente para os dois lados.
- É **totalmente definida por dois parâmetros**:
  - a **média (mean, μ)** — onde fica o centro/pico da curva;
  - o **desvio padrão (standard deviation, σ)** — quão larga/espalhada é a curva. Desvio padrão pequeno → curva alta e estreita; desvio padrão grande → curva baixa e larga.
- A **área total sob a curva é igual a 1** (100% das probabilidades). A área sob um trecho da curva representa a probabilidade de um valor cair naquela faixa.
- **Regra empírica (68–95–99,7):**
  - ~**68%** dos dados caem dentro de **±1 desvio padrão** da média;
  - ~**95%** caem dentro de **±2 desvios padrão**;
  - ~**99,7%** caem dentro de **±3 desvios padrão**.
- A curva nunca toca o eixo horizontal (estende-se ao infinito nas duas pontas), mas as caudas ficam extremamente finas.
- Muitos fenômenos do mundo real se aproximam de uma normal: alturas, pesos, erros de medição, notas de prova etc. — por isso ela é tão central na estatística e em testes de hipóteses.

---

> **Observação de fidelidade:** os números, exemplos e a ordem exata de exposição dos vídeos podem diferir desta reconstrução. A explicação detalhada (`02-explicacao.md`) foi construída sobre os conceitos consolidados do tema "distribuições de probabilidade" e da "distribuição normal".
