# Hipóteses em Usabilidade & Concepção dos Redesigns de Interface — Explicação

> **Matéria:** UX · **Autoestudo:** 03 · **Data:** 21/05/2026
>
> Explicação a partir das três fontes do [`01-material.md`](01-material.md): Polonio P1 (Leis de Jakob, Fitts, Hick, Miller, Postel), Polonio P2 (Pico-final, Estética-usabilidade, von Restorff, Tesler, Doherty) e Apple Human Interface Guidelines.

---

## 1. Contexto geral: por que UX precisa de psicologia (e por que isso é o coração do teste A/B)

Imagine que você é arquiteta de casas. Pra projetar uma boa casa, você precisa saber sobre **materiais** (concreto, madeira), sobre **estrutura** (cálculo, vento, peso), sobre **conforto** (iluminação, temperatura), mas também — e principalmente — sobre **como gente vive numa casa**: quantos passos até o banheiro, qual a altura confortável da bancada, por onde a luz natural deve entrar.

Em UX é igual. Você pode dominar Figma, conhecer React, saber design system inteiro — mas se não souber **como a mente humana processa informação, decide, memoriza, sente e reage ao tempo**, você está projetando casa sem saber que gente mora nela. Daí o nome do autoestudo: **"Hipóteses em Usabilidade & Concepção dos Redesigns de Interface"**. As 10 leis da psicologia e as guidelines da Apple são exatamente o **catálogo de hipóteses fundamentadas** sobre o comportamento humano frente a interfaces.

E aqui está a ligação **direta com o módulo de Teste A/B**:

> Quando você diz "vou testar A vs B", a pergunta seguinte é: **por que você acha que B vai ganhar?** A resposta não pode ser "achismo". Ela precisa ser uma **hipótese**, e uma boa hipótese se ancora em conhecimento sobre comportamento humano. As Leis de Yablonski são justamente **hipóteses já testadas pela psicologia, esperando pra serem aplicadas em A/B tests específicos do seu produto.**

Por exemplo:
- "Vou reduzir o menu de 12 itens pra 5 (Lei de Hick) → hipótese: conversão sobe."
- "Vou aumentar o botão CTA de 32x32 pra 48x48 (Lei de Fitts) → hipótese: taps acidentais caem, conversão sobe."
- "Vou colocar um skeleton screen na home (Limiar de Doherty) → hipótese: bounce rate cai."

Cada lei é um **gerador de hipóteses** pra teste A/B. É por isso que esse autoestudo é uma das pontes mais fortes que UX faz com o tema central do módulo.

---

## 2. Conceitos-chave

Vou agrupar as 10 leis em **5 grupos temáticos**, porque elas conversam entre si:

### Grupo A — Carga cognitiva e decisão

Aqui estão as leis que tratam de **como a mente processa muita informação**.

#### 2.1. Lei de Miller (1956) — a mágica do número 7±2

**Enunciado:** "A pessoa média pode manter apenas 7 (±2) itens em sua memória de trabalho."

**O que é:** George Miller descobriu que a **memória de curto prazo** (working memory) humana é limitada — e o limite gira em torno de 7 unidades. Mas a sacada não é o número 7 — é o conceito de **chunking** (separação em blocos).

**O que é chunking:** agrupar informações em "pedaços" que o cérebro trata como uma unidade. Um telefone `5551234567` é 10 dígitos (extrapolando o limite). Quebrado em `(555) 123-4567`, vira **3 chunks** — fácil de memorizar.

**Aplicação em UI:**
- Quebrar formulários longos em **etapas** (multi-step forms).
- **Hierarquia visual** em textos (títulos, subtítulos, parágrafos).
- Listas com **separação por blocos** em vez de tijolo único de texto.
- Cartão de crédito digitado com espaços a cada 4 dígitos.

> **Termo em inglês:** *working memory* (memória de trabalho) = o "RAM" mental que guarda o que você está usando AGORA, antes de jogar fora.

#### 2.2. Lei de Hick (1952) — quanto mais opções, mais lento

**Enunciado:** "O tempo necessário para tomar uma decisão aumenta com o número e a complexidade das opções disponíveis."

**O que é:** descoberta por Hick e Hyman, é uma das leis mais ferozmente aplicadas em UX. **Quanto mais opções**, mais tempo o cérebro leva pra decidir — e mais provável é o usuário **desistir** (paralisia de decisão).

**Aplicação em UI:**
- Menus de navegação enxutos.
- Pricing pages com **3 planos** (não 7) — e com **um destacado** (Lei de von Restorff entra aqui também).
- Onboarding com poucas perguntas por tela.
- O case dos **controles de TV simplificados** (5 botões grandes em vez de 50).

**Cuidado paradoxal:** simplificar demais pode esconder coisas importantes. Veja a Lei de Tesler, logo abaixo.

#### 2.3. Lei de Tesler — a complexidade irredutível

**Enunciado:** "Todos os processos têm um núcleo de complexidade que não pode ser removido — apenas transferido. Tome cuidado para não simplificar ao ponto de abstração."

**O que é:** observada por Larry Tesler (inventor do "copy-paste"). Toda tarefa tem um **mínimo irredutível de complexidade**. Você não pode "abolir" — só pode escolher **quem carrega**: o sistema ou o usuário.

**Exemplo:** num e-mail, alguém precisa informar destinatário e remetente. Você pode **abstrair** (sugestão por autocompletar, livro de endereços), mas **não pode sumir** com essa complexidade. Alguma parte do esforço sempre fica.

**Aplicação em UI:**
- Checkout: **"endereço de cobrança = endereço de entrega"** → o sistema assume a complexidade, mas a informação continua existindo.
- Filtros de busca: o sistema pode ter padrões inteligentes, mas o usuário precisa dizer o que quer encontrar.
- **Cuidado com a abstração excessiva** — se você esconde demais, o usuário não consegue tomar decisões fundamentadas.

> **A tensão entre Hick e Tesler é o coração do design:** simplifique, mas não vire abstração que esconde o essencial. A linha entre os dois é **a arte do designer**.

### Grupo B — Familiaridade e convenção

#### 2.4. Lei de Jakob (Nielsen, 2000) — não reinvente a roda

**Enunciado:** "Usuários passam a maior parte do tempo em outros sites e preferem que o seu funcione da mesma maneira que os outros que eles já conhecem."

**O que é:** Jakob Nielsen (pai da usabilidade junto com Don Norman) observou que **familiaridade é mais valiosa que originalidade**. O usuário gasta tempo aprendendo o seu site = tempo que ele NÃO gasta convertendo.

**Aplicação em UI:**
- **Carrinho de compras** sempre no topo direito, **busca** no topo central, **perfil** ao lado.
- **Hambúrguer de 3 linhas** = menu mobile.
- **Logo no canto superior esquerdo** que volta pra home.
- **Footer** com links institucionais.

**O custo de quebrar a Lei de Jakob:** o Snapchat, por anos, foi famoso por ter **UI não-convencional** — e isso era barreira de entrada pra usuários mais velhos. Em **2018, o redesign** que aproximou mais das convenções perdeu (na verdade — gerou backlash brutal). É o caso clássico de **ambos os lados serem perigosos**: quebrar convenção afasta novatos; copiar demais afasta a base que ama a originalidade.

> **Conexão com teste A/B:** sempre que você for inovar na UI, **A/B-teste contra a versão "convencional"**. Não jogue toda sua base num design não-validado.

#### 2.5. Lei de Postel — seja conservador no envio, liberal na recepção

**Enunciado:** "Seja conservador no que faz, seja liberal no que aceita dos outros."

**O que é:** Jon Postel a formulou pra **engenharia de redes** (princípio da robustez), mas é uma das leis mais bonitas pra UX. Tradução prática: o **sistema deve tolerar entradas variadas do usuário**, sem rejeitar por detalhe.

**Aplicação em UI:**
- Campo de telefone que aceita `(11) 99999-9999`, `11999999999`, `+5511999999999` — todos viram a mesma coisa internamente.
- Campo de email que **aceita maiúsculas** (mesmo o email sendo case-insensitive).
- **CEP** que aceita com ou sem traço.
- **Face ID, voz, biometria** = formas alternativas de input.
- **Design responsivo** = sistema aceita "input" de tamanho de tela variado.

**Lei correlata pra interfaces:** **mensagens de erro humanas**. Em vez de "Erro: formato inválido", diga "Use um email como exemplo@dominio.com".

### Grupo C — Interação física

#### 2.6. Lei de Fitts (1954) — alvo grande, perto, fácil de acertar

**Enunciado:** "O tempo para acessar um alvo é uma função da distância e do tamanho do alvo."

**O que é:** lei clássica de **interação humano-computador**. Quanto **maior** o alvo e quanto **mais perto** do ponto de partida (cursor, dedo), **mais rápido** o usuário acerta.

**Os números que você precisa saber:**

| Diretriz | Tamanho mínimo do alvo |
|---|---|
| **Apple HIG** | 44 × 44 pt |
| **Google Material** | 48 × 48 dp |
| **WCAG (Acessibilidade web)** | 44 × 44 CSS px |
| **Nielsen Norman Group** | 1 × 1 cm |
| **Espaçamento entre alvos** (Material) | 8 dp mínimo |

**Por que a Apple manda 44×44?** Porque o estudo do **MIT Touch Lab** mostrou que a polpa de um dedo adulto médio mede 8–10 mm² — um alvo menor que isso é tap loteria.

**Aplicação em UI:**
- Botões CTA grandes e centrais (no thumb zone — **zona do polegar**, que Steven Hoober mapeou).
- Em mobile, **botão primário na parte inferior** da tela (mais perto do polegar).
- **Espaço respirável** entre links pra evitar tap acidental no vizinho.

> **Conexão com teste A/B:** o **CTA size A/B test** é um clássico. Botão 32px vs 48px é talvez o teste mais documentado em e-commerce. **Quase sempre o maior ganha** — até certo ponto onde vira agressivo.

### Grupo D — Atenção e percepção

#### 2.7. Efeito von Restorff (1933) — o destoante é lembrado

**Enunciado:** "Quando vários objetos semelhantes estão presentes, é mais provável que aquele que difere dos demais seja lembrado."

**O que é:** Hedwig von Restorff descobriu que se você mostra uma lista `vermelho, vermelho, vermelho, AZUL, vermelho, vermelho`, o cérebro **destaca e memoriza o azul**. É o **paradigma do isolamento**.

**Aplicação em UI:**
- **Tabela de planos** com o plano "Recomendado" destacado em cor diferente, com badge "Mais Popular".
- **Notificações em vermelho** sobre o ícone normal.
- **Botão primário (preenchido) vs secundário (outline)** — guia a atenção pra ação principal.
- **Tooltips coloridos** sobre conteúdo monocromático.

**Cuidado:** se você destaca **tudo**, nada é destaque. É como negrito em texto — se a frase inteira é negrita, **a frase inteira deixa de ter ênfase**.

#### 2.8. Efeito estética-usabilidade (Tractinsky, 2000) — bonito parece funcional

**Enunciado:** "Em geral usuários percebem um design esteticamente agradável como mais utilizável."

**O que é:** o estudo "What is beautiful is usable" de Noam Tractinsky mostrou que **mesmo quando duas interfaces têm a mesma usabilidade objetiva**, a mais bonita é **percebida como mais fácil de usar**.

**Dados impactantes:**
- Usuários formam opinião sobre um site em **50 milissegundos** (estudo Lindgaard et al.).
- Essa opinião **raramente muda** depois — o "primeiro impacto" é durável.

**Aplicação em UI:**
- Investir em **estética desde o protótipo**, não só na fase final.
- **Tipografia limpa**, **espaçamento generoso**, **paleta de cores intencional**.
- Linhagem **Braun → Apple → Dieter Rams**: "menos, mas melhor".

**Risco:** usuários podem **mascarar problemas reais de usabilidade** em interfaces bonitas durante teste com usuários. Por isso, em pesquisa qualitativa, é importante **observar o comportamento real**, não só perguntar opinião. (Conecta com [UX-01 — Métodos Mistos](../autoestudo-01-metodos-mistos-de-exploracao-e-pesquisa/02-explicacao.md): use **misto** quanti + quali pra não cair nessa armadilha.)

### Grupo E — Tempo e emoção

#### 2.9. Regra do pico-final (Kahneman, 1993) — o pico e o fim definem a memória

**Enunciado:** "Pessoas julgam uma experiência baseadas em como se sentiram no ponto mais alto (pico) e no final, em vez de na soma total."

**O que é:** Daniel Kahneman (Nobel de Economia 2002) descobriu isso num **experimento com mão na água gelada**. Versão 1: 60s a 14°C. Versão 2: 60s a 14°C + 30s a 15°C (apenas 1° mais quente). A maioria preferia **repetir a versão 2** — mesmo sendo objetivamente mais longa de desconforto. Por quê? O **final** foi menos ruim, e o cérebro guardou isso.

**Aplicação em UI:**
- **Onboarding com um final feliz** (animação de confete, "Pronto! Bem-vinda!").
- **Estados de erro com humor / empatia** ("Ops! Vamos tentar de novo?" em vez de "ERROR 500").
- **Confirmação visual depois de pagamento** — não simplesmente um spinner e redirect.
- **Uber mostrando o motorista chegando** = transforma um "pico ruim" (esperar sem saber) em "pico aceitável" (esperar sabendo).

> **Conexão com teste A/B:** se você só mede **CSAT/NPS no final**, esse score reflete pico + fim, **não a experiência média**. Por isso, melhorar o final ou eliminar o pior pico costuma render mais em métricas do que melhorias distribuídas.

#### 2.10. Limiar de Doherty (1982) — interaja na velocidade do cérebro

**Enunciado:** "Produtividade aumenta quando computador e usuário interagem a um ritmo que garante que nenhuma das partes precisa esperar pela outra."

**O que é:** estudo da IBM nos anos 80 descobriu que **abaixo de 400 ms**, o usuário se sente "em controle"; acima disso, perde foco. Hoje a régua é ainda mais dura:

| Tempo de resposta | Percepção |
|---|---|
| **< 100 ms** | Instantâneo |
| **100–300 ms** | Perceptível, sensação de "lentidão começando" |
| **300–1000 ms** | Desconforto, percepção de espera |
| **> 1 s** | **Atenção desvia**, tarefa "pula da cabeça" |
| **> 10 s** | Usuário acha que travou |

**Aplicação em UI:**
- **Skeleton screens** (esqueleto do layout antes do conteúdo carregar) — Facebook, LinkedIn, Twitter usam.
- **Otimistic UI** (mostrar a ação como se já tivesse acontecido, antes do backend confirmar) — Instagram com curtidas.
- **Spinners + barras de progresso** quando passa de 1s.
- **Animações curtas (200–400ms)** que "preenchem" o tempo de espera com algo visual.

> **Insight curioso (Yablonski):** às vezes **adicionar um delay proposital aumenta a confiança percebida** — se um app de "análise de crédito" responde em 50ms, parece que não analisou nada. Um delay artificial de 2 segundos sinaliza "estou trabalhando duro pra você". É **psicologia do desempenho percebido**, não do desempenho real.

### Grupo F — Apple Human Interface Guidelines (a materialização das leis)

A Apple não fala explicitamente "Lei de Fitts" — mas se você ler as **Dos and Don'ts**, vai ver que **cada regra é a aplicação concreta de uma ou mais leis**:

| Apple guideline | Lei subjacente |
|---|---|
| **Formatting Content** — caber sem zoom/scroll horizontal | Doherty (esforço cognitivo de scroll) + Jakob (convenção) |
| **Touch Controls** — gestos naturais | Jakob (familiaridade) |
| **Hit Targets** — mínimo 44×44 pt | **Fitts** (tamanho do alvo) |
| **Text Size** — mínimo 11 pt | Acessibilidade + Doherty |
| **Contrast** — texto vs fundo legível | von Restorff + Acessibilidade |
| **Spacing** — não sobrepor texto | Miller (chunking visual) |
| **High Resolution** — @2x, @3x | Estética-usabilidade |
| **Distortion** — manter aspect ratio | Estética-usabilidade |
| **Organization** — controles perto do conteúdo | **Fitts** (distância) + Tesler (não esconder) |
| **Alignment** — alinhar elementos relacionados | Miller (chunking) + Hick (clareza) |

**Por que a Apple faz isso e o Google também (Material Design)?** Porque **convenção é poder** — quando bilhões de pessoas aprendem que "44 pontos é botão tocável", qualquer designer que quebre essa regra está pagando custo de aprendizado.

---

## 3. Exemplo prático: redesign de um checkout com hipóteses

Imagine o checkout de uma loja online com **alta taxa de abandono** (70%). O time decide redesenhar. Cada mudança vira uma **hipótese A/B-testável fundamentada em uma das leis**:

| # | Mudança proposta | Lei aplicada | Hipótese de A/B test |
|---|---|---|---|
| 1 | Quebrar checkout em **3 etapas** com barra de progresso | Miller (chunking) + Doherty (progresso visual) | Conclusão sobe em ≥5% |
| 2 | Reduzir formas de pagamento de **8 para 3** (cartão, Pix, boleto) | Hick (menos = mais rápido) | Tempo médio cai em 15% |
| 3 | Botão "Finalizar" **48×48 px** no centro-baixo do mobile | Fitts (zona do polegar) | Taps acidentais caem em 30% |
| 4 | **"Endereço de cobrança = entrega"** marcado por padrão | Tesler (abstração da complexidade) | Tempo de preenchimento cai 25% |
| 5 | Layout limpo, tipografia legível, cores neutras | Estética-usabilidade | NPS sobe; tempo de página sobe (engajamento) |
| 6 | Mensagens de erro humanas ("verifique o número do cartão") | Postel (liberal na recepção) | Tentativas com sucesso por sessão sobem |
| 7 | Tela de "Compra confirmada!" com animação + nome do produto | Pico-final | NPS pós-compra sobe |
| 8 | **Skeleton screen** durante carregamento da página | Doherty | Bounce rate cai |
| 9 | Plano "Frete Grátis acima de R$100" destacado em verde | von Restorff | Cesta média sobe |
| 10 | Manter botão "Carrinho" no topo direito (convenção) | Jakob | (Sem teste — manter convenção) |

Cada uma dessas é um **A/B test independente** (ou um teste multivariado). Note que **a lei psicológica é a fonte da hipótese**, e o teste A/B é a **validação empírica** dessa hipótese no seu produto específico.

---

## 4. Cases reais no mundo

### Booking.com — laboratório vivo das 10 leis

A Booking.com é famosa por rodar **mais de 1000 testes A/B simultâneos**. Quase todos são fundamentados em alguma dessas leis:

- **Hick:** redução de filtros visíveis.
- **von Restorff:** badges "Reserva mais procurada!", "Últimos 2 quartos!".
- **Pico-final:** confirmação por email com agradecimento caloroso e voucher digital bem desenhado.
- **Postel:** campo de busca aceita "rio", "rj", "rio de janeiro", "Rio de Janeiro - RJ".

### Instagram + Optimistic UI (Doherty na prática)

Quando você dá ❤️ numa foto, **o coração vermelho aparece instantaneamente** — mesmo que o request HTTP ainda esteja em viagem. Se o backend falhar, o app silenciosamente desfaz. **Resultado:** a percepção de velocidade é "instantânea" mesmo em 4G ruim.

### Spotify Wrapped — Pico-final em escala anual

Toda final de ano, o Spotify lança o **Wrapped** — uma jornada visual estilo Stories com seus dados anuais. É um **pico emocional intencional** no fim do ano de uso do produto. O resultado: virou **fenômeno cultural** e drive de retenção. Pico-final aplicado em escala estratégica.

### Netflix — A/B testing de thumbnails (estética + von Restorff + atenção limitada)

A Netflix **A/B-testa as miniaturas (capas) dos títulos** com até **9 variantes diferentes** por título. Cada usuário vê a capa que historicamente mais aciona o play **dele**. Por trás: **efeito estética-usabilidade** + von Restorff + Doherty (a decisão precisa acontecer em segundos no scroll).

### Snapchat — quebrando Jakob (e pagando o preço)

O Snapchat **deliberadamente quebrou a Lei de Jakob** por anos: navegação por gestos, sem labels óbvios. Isso criou **barreira de entrada brutal pra usuários mais velhos** — mas paradoxalmente **fidelizou os adolescentes** que dominaram o "código secreto". Em 2018, quando redesenharam pra ficar mais "convencional", **a base original revoltou** — o redesign foi parcialmente revertido. Lição: **quem é seu público determina se Jakob te ajuda ou te limita**.

### Amazon 1-Click — Tesler em forma de patente

O famoso **botão "Comprar com 1 clique"** da Amazon (patenteado em 1999) é a aplicação literal da Lei de Tesler: a complexidade do checkout existe, mas foi **transferida pro sistema** (endereço, pagamento, frete já salvos). Resultado: bilhões em receita extra ao longo dos anos.

---

## 5. Conexão com o módulo

Esse autoestudo é, na minha opinião, **a ponte mais forte** que a matéria de UX faz com o tema central do módulo. Algumas conexões:

### 5.1. Leis psicológicas = banco de hipóteses para A/B testing

Como já adiantei na introdução: **toda lei aqui gera hipóteses testáveis**. Quando você vai planejar um teste A/B no seu produto:

1. Identifique um problema (ex: abandono no checkout).
2. **Olhe as 10 leis** e pergunte: "Qual delas explicaria esse problema?"
3. Use a lei pra **formular a hipótese da mudança**.
4. **Teste A/B** pra validar no seu contexto específico.

Isso é **a profissionalização de "achismo"** — saímos do "eu acho que o botão maior vai converter mais" pra "a Lei de Fitts prevê que um alvo maior reduz tempo de tap; nossa hipótese é que isso aumenta conversão em ≥3%".

### 5.2. Pontes com outros autoestudos

- **[UX-01 — Métodos Mistos de Pesquisa](../autoestudo-01-metodos-mistos-de-exploracao-e-pesquisa/02-explicacao.md):** combina quanti (A/B test mede impacto) com quali (entrevistas explicam o "por que"). A estética-usabilidade alerta: **não confie só em perguntar — observe.**
- **[UX-02 — Arquitetura da Informação](../autoestudo-02-arquitetura-da-informacao/02-explicacao.md):** AI é onde Miller (chunking), Hick (opções) e Tesler (complexidade) se encontram. Boa AI = aplicação dessas três simultaneamente.
- **[Negócios-01 — Experimentação em Produtos Digitais](../../negocios/autoestudo-01-experimentacao-em-produtos-digitais/02-explicacao.md):** o caso clássico é o time de produto que mistura design (UX laws) com experimentação (testes A/B) — a hipótese vem do conhecimento de UX; a validação vem do experimento.
- **[Computação-06 — Programação de Testes A/B](../../computacao/autoestudo-06-fundamentos-de-programacao-de-testes-ab/02-explicacao.md):** a infra de A/B test é o que permite **rodar essas hipóteses de UX a baixo custo**. Sem feature flag e bucketing, cada redesign vira "all or nothing".
- **[Matemática-01 — Distribuições de Probabilidade](../../matematica/autoestudo-01-distribuicoes-de-probabilidade/02-explicacao.md):** a Lei de Hick tem **fórmula logarítmica**; a regra do pico-final é estudo psicométrico — quantitativo na base.
- **[Computação-04 e 05 — Cadeias de Markov](../../computacao/autoestudo-04-introducao-as-cadeias-de-markov/02-explicacao.md):** o **comportamento de navegação** que von Restorff e Doherty afetam pode ser modelado como cadeia de Markov pra prever o efeito no funil.

### 5.3. A lição maior: hipóteses sem dados são chutes; dados sem hipóteses são ruído

A combinação que esse autoestudo deixa clara:

- **Leis de UX sozinhas** → "minha intuição diz que isso vai funcionar".
- **A/B test sem hipótese** → "vamos testar e ver" (= ruído estatístico, sem aprendizado).
- **Lei de UX + A/B test** → "minha hipótese, fundamentada em ciência cognitiva, prevê X — vamos validar empiricamente". **Esse é o método profissional.**

---

## 6. Resumo estruturado

### As 10 Leis de Yablonski

| Lei | Ano | Resumo em uma frase | Aplicação principal |
|---|---|---|---|
| **Jakob** | 2000 | Familiaridade vence originalidade | Convenções de UI |
| **Fitts** | 1954 | Alvo grande + perto = rápido | Tamanho de botão, zona do polegar |
| **Hick** | 1952 | Mais opções = decisão mais lenta | Reduzir menus, simplificar escolhas |
| **Miller** | 1956 | Memória de trabalho = 7±2 chunks | Chunking, hierarquia |
| **Postel** | (rede) | Conservador no envio, liberal na recepção | Tolerar entradas variadas |
| **Pico-final** | 1993 | Memória = pico + final, não média | Onboarding/checkout com final memorável |
| **Estética-usabilidade** | 2000 | Bonito parece funcional (50ms!) | Investir em estética cedo |
| **von Restorff** | 1933 | O destoante é lembrado | Destaque do plano recomendado |
| **Tesler** | — | Complexidade não some, só transfere | Abstrair com cuidado |
| **Doherty** | 1982 | Resposta < 400ms = controle do usuário | Skeleton, optimistic UI |

### Apple HIG — Dos & Don'ts

- **Hit targets ≥ 44 × 44 pt.**
- **Texto ≥ 11 pt** e contraste suficiente.
- **Sem zoom/scroll horizontal** pra conteúdo principal.
- **Imagens @2x e @3x** pra Retina; sem distorção.
- **Controles perto do conteúdo** que modificam.
- **Alinhar** pra mostrar relação entre elementos.
- **Espaçamento** que não deixe texto se sobrepor.

### A grande síntese

> **Lei psicológica = hipótese pronta. A/B test = validação no seu contexto. O designer profissional usa as duas em conjunto.**

---

## 7. Auto-reflexão

Três perguntinhas pra você pensar:

1. Pega um app que você usa todo dia (Instagram, Spotify, iFood, Nubank...). **Identifique pelo menos 3 das 10 leis** aplicadas — e **uma que você acha que está sendo violada**. Como você A/B-testaria a correção?
2. A **Lei de Jakob** e a **Lei de Tesler** parecem se opor à inovação ("siga convenções", "não simplifique demais"). **Onde está o equilíbrio entre seguir convenção e inovar?** O Snapchat foi um vencedor ou um perdedor desse equilíbrio?
3. O **efeito estética-usabilidade** diz que bonito parece funcional. Isso significa que devemos investir mais em estética do que em usabilidade real? Que **riscos éticos** esse efeito traz pra pesquisa com usuários — e como o módulo de [UX-01 (métodos mistos)](../autoestudo-01-metodos-mistos-de-exploracao-e-pesquisa/02-explicacao.md) ajuda a mitigar?
