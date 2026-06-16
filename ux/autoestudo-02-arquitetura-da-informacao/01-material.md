# Arquitetura da Informação — Material

> **Matéria:** UX · **Autoestudo:** 02 · **Data:** 14/05/2026 · **Professor:** Guilherme Henrique de Oliveira Cestari (Eixo UEX)
>
> Duas fontes. A **Fonte 1** (livro *Information Architecture*, O'Reilly) veio como **excerto parcial** (início do Capítulo 4, cortado). A **Fonte 2** (artigo da NN/g) está completa. Conteúdo limpo de navegação/rodapé.

---

## Fonte 1 — Livro *Information Architecture* (O'Reilly) — Capítulo 4: *The Anatomy of an Information Architecture*

> ⚠️ **Excerto parcial** — o texto fornecido cobre apenas o início do capítulo e foi cortado ("Because it's highly probable that you'll ...").

**O que o capítulo cobre:**
- Por que é importante (e difícil) tornar uma arquitetura de informação o mais **tangível** possível.
- Exemplos que ajudam a visualizar uma arquitetura de informação tanto **de cima para baixo (top-down)** quanto **de baixo para cima (bottom-up)**.
- Formas de **categorizar os componentes** de uma arquitetura de informação, para entender e explicar melhor a IA.

Nos capítulos anteriores, a arquitetura de informação foi discutida de uma perspectiva conceitual. Este capítulo apresenta uma visão mais **concreta** do que a arquitetura de informação realmente é, para ajudar a reconhecê-la quando se a vê. Também introduz os **componentes** de uma arquitetura — importantes porque compõem a "paleta" do arquiteto de informação (detalhados nos capítulos 5–9).

### Visualizando a Arquitetura de Informação

Por que é importante conseguir visualizar a arquitetura de informação? Várias respostas:
- O campo é **novo**, e muitas pessoas não acreditam que as coisas existam até poderem vê-las.
- O campo é **abstrato**, e muitos que entendem conceitualmente a premissa básica da IA só vão realmente "sacar" quando a virem e experimentarem.
- Uma arquitetura de informação **bem projetada é invisível para os usuários** (o que, paradoxalmente, é uma recompensa bastante injusta para o sucesso da IA).

A falta de qualidades tangíveis da IA força todo arquiteto de informação a ser, em certo grau, um **vendedor** (salesperson). Porque é altamente provável que você [...] *(texto cortado no excerto fornecido).*

---

## Fonte 2 — Nielsen Norman Group: *5 Information Architecture Warning Signs in Your Analytics Reports*

> Autoras: Kathryn Whitenton e Katie Sherwin · 25 de setembro de 2016.

**Resumo:** Métricas de analytics como pageviews, conversões, entradas (entrances), taxas de rejeição (bounce rates) e frequência de buscas (search queries) podem ajudar a identificar problemas na sua estrutura de categorias.

Uma boa **arquitetura de informação (information architecture, IA)** é essencial para oferecer uma boa UX e atingir os objetivos de negócio. Mas como saber se uma IA é "boa"? Comece olhando seus dados de analytics.

Sistemas de analytics registram todas as ações dos usuários; revisar os padrões de comportamento nesses dados direciona a atenção para categorias de conteúdo confusas, ausentes ou de baixo desempenho, que deveriam ser otimizadas ou investigadas em testes com usuários. Os dados de analytics são especialmente úteis quando há uma **grande coleção de conteúdo** (posts, produtos, artigos de suporte): apresentar o conteúdo em categorias compreensíveis e interessantes deixa os usuários mais propensos a navegar (e melhora o ranking de busca).

> *Exemplo recorrente:* o site Gardendesign.com tem 3 conjuntos de categorias analisáveis: o menu global no topo, a lista de navegação de tópicos à esquerda, e as páginas de categoria em destaque no corpo da home.

Para usar analytics para melhorar a IA, é preciso: (1) **identificar quais métricas considerar**; (2) **interpretar cada métrica** segundo o contexto do design, das metas do usuário e das metas de negócio. Essa interpretação é crítica, pois algumas categorias de nicho servem a objetivos importantes mesmo exibindo "sinais de alerta".

### 1. Baixo tráfego para categorias (Low Traffic)

O volume de tráfego a uma categoria é o indicador mais óbvio de quão útil/interessante ela é. Pode ser medido pelos views da página principal da categoria ou agregando os views de todas as páginas dentro dela. (Termos variam por ferramenta: 'pageviews', 'visits', etc.) **Exclua views repetidos do mesmo usuário** — o volume pode ser inflado por *pogo-sticking* (ir e voltar repetidamente entre a categoria e os artigos). Use a métrica de **views únicos**.

**Como interpretar baixo tráfego** (em relação à importância estratégica):
- O tráfego é comparável ao de outras categorias? (Calcule o tráfego médio por categoria e a razão de cada uma com a média. Se a categoria recebe só 5% da média, pode ser irrelevante para a maioria.)
- Há outros fatores (como layout) que explicam a diferença? Categorias mais **visualmente proeminentes** ou que aparecem várias vezes têm mais tráfego — não compare categorias com proeminência muito diferente. (Na Gardendesign, 3 categorias duplicadas no corpo da home teriam tráfego inflado pelo design, não por interesse real.)
- Você esperaria mais tráfego pela importância do tópico? Categorias mission-critical às vezes não recebem o tráfego esperado — vale testar **nomes alternativos** para aumentar descoberta (discoverability) e localização (findability).
- A categoria é estrategicamente importante mesmo com baixo uso? (Pode ser usada raramente, ou só por um pequeno grupo valioso — então vale mantê-la.)

Se a resposta a tudo for "não", considere **eliminar ou desfatizar** a categoria (há um custo de oportunidade em manter tópicos que ninguém quer).

### 2. Baixas conversões (Low Conversions)

Conversões representam ações desejáveis (compras, cadastros) e devem ser configuradas como **metas (goals)** no analytics. Categorias de alto tráfego podem ter poucas conversões — sinal de que são menos estratégicas do que o número bruto de visitas sugere.

**Como interpretar:** antes de decidir, entenda o que conta como conversão e busque outros sinais de valor:
- A categoria é fonte significativa de tráfego para **outras páginas importantes**? (Ex.: "How-to Info" não gera assinaturas, mas leva à seção de Produtos, que gera receita de afiliados.)
- O conteúdo faz parte de uma **jornada mais longa** (várias visitas antes de converter)? A conexão pode não ser medida bem se as métricas só capturam conversões da mesma sessão, ou se visitas posteriores vêm de outros dispositivos.

Se as conversões são baixas e não há outro valor estratégico, é candidata a eliminar ou renomear.

### 3. Altas taxas de rejeição em páginas de categoria (High Bounce Rates)

O objetivo de uma página de categoria é levar tráfego ao conteúdo listado. Se os usuários chegam e saem imediatamente, sem clicar em nada, algo está errado.

**Como interpretar:** considere de onde os usuários vieram e o que veem ao chegar:
- O rótulo (label) descreve com precisão a categoria, ou pode ser mal interpretado? Alto abandono costuma vir de **expectativas não atendidas** — um rótulo de anúncio/busca deve descrever com precisão a página (uma galeria de fotos não deveria se chamar "Como Projetar um Jardim").
- O layout impede de ver o conteúdo? Vale visitar a página ou rodar um **teste rápido de usabilidade**. Se todas as categorias usam o mesmo template, é improvável que só uma tenha problema de layout — mas editores às vezes fazem modificações pontuais que prejudicam a usabilidade.

### 4. Baixas taxas de entrada (Low Entrance Rates)

A primeira página que o usuário vê numa visita é sua **entrada (entrance) / landing page**. Entradas são estrategicamente valiosas: representam oportunidade de **expandir a audiência** (especialmente filtrando por novos visitantes). Se uma categoria tem poucas entradas, não atrai usuários efetivamente.

**Como interpretar:**
- As entradas são menores que o esperado? Se o tópico é significativo (ex.: "Jardins Premiados", seu melhor conteúdo), o problema pode ser promoção fraca ou rótulo ruim.
- A baixa entrada é comum em **todos os canais**? Segmente por fonte. (Ex.: bom tráfego social mas fraco em busca → problema de **SEO**, usando termos diferentes dos que as pessoas buscam.)
- A categoria converte bem entre os poucos que atrai? Se sim, vale manter pelo nicho.

Sempre cheque a taxa de entrada antes de eliminar uma categoria, para não remover um ponto de entrada importante.

### 5. Alto volume de buscas (High Volume of Search Queries)

As buscas indicam **o que as pessoas querem** — e sugerem que elas **não acharam** na IA atual. Gere a lista dos termos mais buscados. Os mais frequentes podem valer ser adicionados ou priorizados nas categorias (ex.: se "xeriscape" é muito buscado, considere criar uma categoria).

**Como interpretar:**
- A busca já é representada por uma categoria? Se sim, considere **promovê-la** mais para facilitar a localização.
- Há conteúdo suficiente para justificar uma categoria, e ela se alinha às metas de negócio? Nem todo termo popular precisa de categoria própria — só eleve os de vantagem estratégica significativa.

### Conclusão

Interprete os dados de analytics no **contexto mais amplo** de estratégia de conteúdo, necessidades de negócio e usuário, e valor de SEO. Olhe todas essas dimensões antes de remover, renomear ou manter uma categoria.

Em casos ambíguos, **complemente o analytics com outros tipos de dado**: por exemplo, **conduza um teste A/B para estudar o efeito de renomear uma categoria**, ou monte uma breve **pesquisa (survey)** numa página de categoria para entender as motivações do visitante. Focando nos sinais de alerta acima, dá para analisar e melhorar a IA de forma eficiente.
