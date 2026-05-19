# Fundamentos de Programação de Testes A/B

> **Data:** 19/05/2026 — 10:00h
> **Matéria:** Computação
> **Autoestudo:** 01

Este material compila três fontes: (1) artigo em PT sobre fundamentos e estratégia de teste A/B, (2) artigo em EN sobre implementação em Python, e (3) descrição de vídeo sobre tópicos avançados.

---

## Parte 1 — Teste A/B: o que é e como implementar na estratégia do seu negócio

> Fonte: artigo em português.

O teste A/B é uma das estratégias mais utilizadas por empreendedores e gestores de marketing para aprimorar resultados.

Um dos principais pontos fortes do marketing digital é o seu poder de permitir testes e mensurar resultados. É isso que permite a compreensão das ações que estão gerando os resultados esperados e das que precisam de ajustes.

Uma das maneiras mais populares e eficazes de experimentar, analisar e monitorar resultados é o teste A/B.

### O que são testes A/B?

Testes A/B, também conhecidos como **teste de divisão** ou **teste bucket**, são experimentos feitos para comparar duas versões de uma página.

Basicamente, ele divide o tráfego de uma página em duas versões: uma já existente e outra nova, desenvolvida com algumas modificações. O objetivo é medir qual das versões apresenta uma maior **taxa de conversão**.

São bastante utilizados em estratégias de marketing digital, como e-mail marketing, landing pages, anúncios, etc. E devem ser feitos entre páginas que tem **uma só variável**, e não várias.

Por exemplo, uma variável tem um botão verde, enquanto a outra tem um botão azul. Ou seja, não é uma página que tem um botão verde e a outra que tem um formulário.

### Por que os testes A/B são importantes?

Os testes A/B são ótimas ferramentas para obter um retorno real por parte da audiência, já que geram dados reais e mensuráveis sobre ela.

É comum que profissionais fiquem em dúvida se devem ou não seguir um palpite. É claro que a experiência pode falar mais alto algumas vezes, mas é indispensável trabalhar com foco na análise de dados, não em "achismos". É o que chamamos de **data driven marketing**.

Uma das grandes vantagens de atuar no ambiente digital é ter acesso aos dados dos consumidores. Isso torna as estratégias de venda mais eficientes, uma vez que você consegue entender com clareza o comportamento e as necessidades dos compradores.

### Onde usar os testes A/B?

Canais:

- Páginas de um site
- Landing pages
- E-mail marketing
- Anúncios no Google (Google Ads)
- Anúncios em redes sociais (Facebook Ads e outros)

Elementos dentro desses canais:

- Títulos
- Links de navegação
- Botões de CTA (Call to Action)
- Assunto do e-mail
- Imagens ou vídeos
- Oferta
- Textos variados

Apesar de o teste A/B poder ser utilizado em todos esses canais, a escolha deve ser feita com atenção. Não é preciso apostar em todas as possibilidades de uma só vez — analise os objetivos, implemente aos poucos e analise os resultados.

### Benefícios de fazer testes A/B

1. **Facilidade de implementação** — basta ter audiência apropriada e uma boa ferramenta. O processo é simples, sem exigência de conhecimentos profundos.
2. **Decisões mais acertadas** — gera números concretos, possibilitando tomada de decisão baseada em dados.
3. **Compreensão profunda da audiência** — entender o que os consumidores querem. Lançando uma campanha de e-mail com dois ou três títulos diferentes, é possível compreender qual mais agradou à audiência.

### Como fazer testes A/B?

1. **Defina a variável a ser testada** — um teste de cada vez, pra evitar confusão na análise.
2. **Estabeleça uma meta para o teste A/B** — aprimorar geração de leads, acessos, aumentar taxa de abertura, de cliques, etc.
3. **Use uma ferramenta de teste A/B** — Google Optimize, Optimizely, entre outras.
4. **Divida os grupos de amostra** — aleatoriamente, com a mesma quantidade de pessoas em cada grupo.
5. **Escolha uma métrica para definir o vencedor** — alinhada com a meta.
6. **Analise os resultados** — mensurar, rever, ajustar.

### Qual a diferença entre CRO e teste A/B?

- **Teste A/B**: compara variáveis de marketing, com o objetivo de definir a que gera retorno melhor.
- **CRO (Conversion Rate Optimization)**: estratégia mais ampla, conjunto de práticas voltadas para o aumento das conversões de um site. Aproveita o tráfego que as páginas já têm, sem necessariamente atrair mais visitantes.

### Qual a diferença entre testes multivariados e testes A/B?

- **Testes multivariados**: testam mais de uma variável de uma única vez.
- **Testes A/B**: testam só uma variável (com duas ou mais variações) por vez.

O foco é sempre chegar a uma conclusão de qual é a melhor opção entre as testadas.

### Ferramentas para realizar teste A/B

1. **Google Optimize** — ferramenta do Google, versão gratuita e paga. Integrada com Google Analytics.
2. **Optimizely** — uso simples, requer adicionar uma linha de JavaScript no site.
3. **VWO** — recursos amplos, não só A/B mas otimização de conversões em geral. 30 dias de teste gratuito.

### Quando fazer o teste A/B?

Quando há necessidade de entender qual das opções viáveis de uma ação é a que mais faz sentido para o negócio. Por exemplo, ao lançar um produto novo e estar em dúvida sobre qual mensagem usar pro público.

### Perguntas Frequentes

**Como fazer o teste A/B?** Defina a variável, a meta, a ferramenta, divida os grupos, escolha a métrica e analise os resultados.

**Quando fazer um teste A/B?** Quando há a necessidade de entender qual das opções viáveis de uma ação gera resultado.

**Para que serve o teste A/B?** Gerar retorno real sobre a audiência, fazendo com que se trabalhe focado em dados reais e mensuráveis.

**O que é o teste A/B do Facebook?** Ferramenta do Facebook que permite anunciantes desenvolverem testes comparativos para entender quais estratégias geram mais resultados.

---

## Parte 2 — A/B Testing and how to implement it in Python using just a few lines of code

> Fonte: artigo em inglês, por Zipporah Luna (Medium, jul/2021).

A brief explanation of how A/B testing is helping businesses make strategic decisions and how to implement it in Python using just a few lines of code.

### What is A/B Testing?

An A/B Test is a randomised experiment containing two groups, A & B, that receive different experiences. Within an A/B Test, we look to understand and measure the response of each group.

### How to measure and understand A/B Testing results?

To measure and understand the results of your conducted A/B Tests, you can use the **Two-Sample hypothesis test** or **Independent Samples t-test**.

> "The two-sample t-test (also known as the independent samples t-test) is a method used to test whether the unknown population means of two groups are equal or not."

### Some examples of A/B Testing put into practice

- Online advertisement strategies
- Email subject lines when contacting customers
- Testing the effect of mailing customers a coupon versus a control group
- Netflix testing different images for the same movie
- Amazon testing new website features to stay ahead of their competition

### How to Implement in Python?

**Sample Problem:** Identify if a nicer looking promotional mailer would get more customers to sign-up for a delivery club that costs $100.

Etapas (descritas no artigo, com prints/snippets de código no original):

1. Import Required Packages
2. Get observed frequencies
3. State hypotheses
4. Calculate and get results
5. Result Summary

### Result Summary

The sample problem assessed the difference in sign-up rate to the club between two different mailers that were sent. Based on the data provided and using the **chi-squared test for independence**, the recommendation to ABC Grocery (and its marketing department) is that they can stop sending an expensive looking mailer — or even a simple mailer — to save costs, as it does not help in getting customers to sign-up for the delivery club promo.

---

## Parte 3 — A/B Test Like a Pro #6: Advanced Topics in A/B Testing

> Fonte: descrição de vídeo.

Este vídeo aborda tópicos avançados em testes A/B, como:

- **Eventos de ativação** — o que são e quando usá-los.
- **Execução de múltiplos testes A/B simultaneamente** — se é possível e como.
- **Análise dos resultados dos testes no BigQuery** — como testar objetivos que não são suportados no console.
