# Métodos Mistos de Exploração e Pesquisa — Explicação

> **Matéria:** UX · **Autoestudo:** 01 · **Data:** 23/04/2026 · **Professor:** Guilherme Cestari
>
> Explicação detalhada construída a partir das três fontes do [`01-material.md`](01-material.md): o guia da Dscout (People Nerds), o framework da Nielsen Norman Group (NN/g) e o paper do HEART framework (Google).

---

## 1. Contexto geral: por que "misturar métodos"?

Imagine que você é médico e um paciente chega reclamando de cansaço. Você poderia **perguntar** a ele como se sente (e ele te diz: "ando exausto, durmo mal"). Ou poderia **medir** coisas nele: exame de sangue, pressão, um monitor de sono. Cada abordagem te dá um pedaço da verdade. O relato dele te dá o *contexto* e o *porquê* ("acho que é o estresse do trabalho"). Os exames te dão *números frios* que confirmam ou desmentem o relato ("na verdade seu ferro está baixíssimo"). Um bom diagnóstico raramente vem de uma fonte só — ele vem do **cruzamento** das duas.

**Pesquisa de usuário (User Research / UX Research)** é exatamente isso, só que o "paciente" é a pessoa que usa seu produto, e o "diagnóstico" é entender o que ela precisa, o que a trava e o que a faria feliz. E **métodos mistos** (em inglês *mixed methods*, também chamados de *hybrid methods* ou *multi-method*) é a prática de **atacar uma mesma pergunta de pesquisa usando mais de um método**, justamente para juntar esses pedaços de verdade num quadro mais completo.

O problema que isso resolve: **nenhum método sozinho é completo.** Um questionário te dá escala, mas não te diz o porquê. Uma entrevista te dá profundidade, mas com 8 pessoas você não sabe se aquilo vale pra 8 milhões. Quando você combina os dois, um cobre a fraqueza do outro. Como resume o guia da Dscout: hibridizar métodos "pega o melhor de cada ferramenta (a escala do survey, a riqueza da entrevista, a posicionalidade da etnografia) e combina para criar um quadro mais completo, verdadeiro e acionável".

Onde isso brilha: nas perguntas **espinhosas e estratégicas** — "*Devemos construir isto?*", "*O que as pessoas realmente acham disto?*". Onde isso **não** ajuda muito: perguntas estreitas e objetivas — "*Esse botão deve ser azul ou verde?*". (Guarde essa última, porque é exatamente o tipo de pergunta que o **teste A/B** — tema do nosso módulo — responde sozinho. Já volto nisso.)

---

## 2. Conceitos-chave (do mais básico ao mais avançado)

### 2.1. Qualitativo vs. Quantitativo

Esse é o par mais fundamental de toda a pesquisa.

- **Qualitativo (qualitative):** dados sobre comportamentos e atitudes coletados **diretamente** — você observa ou ouve a pessoa. São palavras, histórias, observações. A análise **não é matemática**: você lê, interpreta, agrupa em temas. Responde bem a **"por quê?"** e **"como consertar?"**. Exemplo: uma entrevista onde o usuário diz "desisti de comprar porque não confiei no site na hora de botar o cartão".
- **Quantitativo (quantitative):** dados coletados **indiretamente**, através de um *instrumento* (um questionário, uma ferramenta de analytics). O dado é predeterminado e vira número: tempo de tarefa, taxa de sucesso, clicou/não clicou. A análise **é matemática**. Responde bem a **"quantos?"** e **"quanto?"**. Exemplo: "68% dos usuários abandonam o carrinho na tela de pagamento".

> A grande sacada: qualitativo te diz **por que** a casa está pegando fogo; quantitativo te diz **quantos cômodos** já estão queimando. Você precisa dos dois para decidir onde jogar a água primeiro.

### 2.2. Atitudinal vs. Comportamental

Esse é o par que mais gera erro de interpretação na vida real. A NN/g resume numa frase genial: **"o que as pessoas dizem" vs. "o que as pessoas fazem"** — e avisa: *muito frequentemente os dois são diferentes*.

- **Atitudinal (attitudinal):** mede **crenças e opiniões declaradas**. Limitado pelo que a pessoa tem consciência e está disposta a admitir. Ex.: surveys, focus groups, card sorting.
- **Comportamental (behavioral):** observa **o que a pessoa de fato faz** com o produto. Ex.: eyetracking (pra onde ela olha), analytics (onde ela clica) e — atenção — **A/B testing**.

O clássico exemplo de divergência: numa pesquisa, 90% das pessoas dizem que "se preocupam com privacidade". No comportamento real, elas aceitam todos os cookies em 1 segundo pra ler uma receita de bolo. **O que dizem ≠ o que fazem.** Por isso métodos mistos costumam casar um método atitudinal (pra entender a percepção) com um comportamental (pra checar a realidade).

### 2.3. Contexto de uso (Context of Use)

A terceira dimensão da NN/g: **como e se** a pessoa está usando o produto durante o estudo.

1. **Uso natural** — ela usa o produto no mundo real, com o mínimo de interferência (maior fidelidade à realidade, menos controle). Ex.: estudos etnográficos de campo, *intercept surveys*.
2. **Uso roteirizado (scripted)** — você dá tarefas específicas pra focar num fluxo (ex.: testar um checkout recém-redesenhado). O **benchmarking** é o caso mais roteirizado de todos, justamente pra garantir consistência entre participantes.
3. **Uso limitado (limited)** — uma versão reduzida/abstrata do produto pra estudar um aspecto. Ex.: *card sorting*, *concept testing*.
4. **Sem uso (decontextualized)** — a pessoa nem toca no produto; você estuda algo mais amplo, como percepção de marca ou estética.

### 2.4. O framework 3D da Nielsen Norman Group

Junte as três dimensões acima (Atitudinal↔Comportamental, Quali↔Quanti, Contexto de uso) e você tem o **mapa mental clássico do UX Research**, criado por Christian Rohrer. É um "mapa de onde cada método mora". Saber onde cada método se posiciona é o que te diz **quando** e **por que** misturar: você combina métodos que ficam em "altitudes" diferentes pra cobrir mais do mapa.

| Método | Quali/Quanti | Atitudinal/Comportamental |
|---|---|---|
| Entrevistas | Quali | Atitudinal |
| Card sorting | ambos | Atitudinal |
| Surveys | Quanti | Atitudinal |
| Usability testing | ambos | mistura (pende p/ comportamental) |
| Field studies | Quali | mistura |
| Eyetracking | Quanti | Comportamental |
| **A/B testing** | **Quanti** | **Comportamental** |
| Analytics / clickstream | Quanti | Comportamental |

### 2.5. A dimensão do tempo: generativo, formativo, somativo

Além das 3 dimensões, há uma quarta — **em que fase do desenvolvimento do produto você está**. Isso muda o objetivo da pesquisa:

- **Generativo (generative):** no começo, quando você ainda não sabe o que construir. Objetivo: **achar direções e oportunidades**. Métodos: field studies, diary studies, entrevistas, surveys, concept testing.
- **Formativo (formative):** durante o design, pra **melhorar** o que está sendo feito. "Formativo" porque *forma/molda* a solução enquanto ela ainda está mole. Métodos: card sorting, tree testing, usability testing.
- **Somativo (summative):** depois de pronto, pra **medir o desempenho** contra versões anteriores ou contra concorrentes. "Somativo" porque *soma/avalia o resultado final*. Métodos: usability benchmarking, **A/B testing**, analytics, surveys.

Mnemônico: **G**era ideias → **F**orma a solução → **S**oma/avalia o resultado.

### 2.6. Os "sequenciamentos" (como ordenar os métodos misturados)

Misturar métodos não é fazer tudo ao mesmo tempo. A Dscout insiste num ponto importante: deve ser um **fluxo único** — cada método **informa, afia e melhora** o próximo. Fazer vários testes em paralelo "pra cobrir bases" rouba o aprendizado de cada um. Três receitas:

- **Macro → micro:** comece largo e afunile. Ex.: um **survey** (n=1000) pra ver tendências amplas → depois **entrevistas** (n=10) pra entender o porquê das tendências. Bom quando o espaço do problema ainda é nebuloso.
- **Micro → macro:** comece fundo e generalize. Ex.: **entrevistas** geram temas → você "pressiona" esses temas (*pressure-test*) com um **survey** grande pra ver se valem pra todo mundo. Bom quando o tema é sensível, raro, ou você tem pouca gente disponível.
- **Iterativo/reativo:** vai e volta continuamente, cada resultado abrindo a próxima pergunta. Bom quando há tempo e orçamento.

### 2.7. Triangulação

O termo técnico por trás de tudo isso é **triangulação (triangulation)**: confirmar um achado olhando-o de **mais de um ângulo**. Se a entrevista *e* o survey *e* o analytics apontam todos para "o checkout é confuso", você tem uma certeza muito maior do que se tivesse só um deles. É o mesmo princípio do GPS: com um satélite você não acha sua posição; com três, sim.

### 2.8. Análise: top-down vs. bottom-up

Quando os dados chegam, há dois jeitos de começar a fazer sentido deles:

- **Top-down:** começa pelo **quantitativo**, que aponta os "faróis" (ex.: "criar conta é a dor #1"), e aí você mergulha no qualitativo *naquele ponto específico* pra achar as citações e exemplos.
- **Bottom-up:** começa pelo **qualitativo**, gera temas/personas a partir do zero (*grounded theory*), e depois usa um survey pra checar a frequência desses temas na população maior.

### 2.9. O framework HEART (Google) — medindo UX em larga escala

A terceira fonte (paper de Rodden, Hutchinson & Fu, do Google, no CHI 2010) ataca um problema específico do lado **quantitativo**: *como medir experiência do usuário quando você tem milhões de usuários numa aplicação web?* A resposta é o **HEART**, cinco categorias de métricas centradas no usuário:

- **H**appiness — satisfação, percepção (ex.: NPS, nota de satisfação). *[atitudinal]*
- **E**ngagement — nível de envolvimento (ex.: sessões por usuário por semana). *[comportamental]*
- **A**doption — quantos *novos* usuários começam a usar (ex.: contas criadas no mês). *[comportamental]*
- **R**etention — quantos *continuam* usando ao longo do tempo (ex.: % que volta após 30 dias). *[comportamental]*
- **T**ask success — eficiência/eficácia em tarefas (ex.: taxa de conclusão, tempo, erros). *[comportamental]*

E o pulo do gato do paper é o processo **Goals → Signals → Metrics** (Metas → Sinais → Métricas): em vez de medir "o que dá pra medir", você primeiro define a **meta** de cada categoria, depois que **sinal** de comportamento indicaria sucesso, e só então a **métrica** exata. Isso evita o erro clássico de afogar o time em números que não significam nada.

> **Por que o HEART importa para métodos mistos (e para A/B testing):** o HEART te dá o *vocabulário quantitativo* da experiência. Quando você roda um teste A/B, precisa escolher **qual métrica** vai julgar o vencedor — e Happiness/Engagement/Adoption/Retention/Task-success são exatamente as famílias de métricas que você considera. O lado qualitativo (entrevistas) te diz *qual* mudança testar; o HEART te diz *como medir* se ela funcionou.

### 2.10. "Hackeando" métodos mistos (quando falta tempo/grana)

Nem sempre dá pra rodar um estudo completo. A Dscout lista jeitos baratos de dar um "tempero quantitativo" a uma pesquisa qualitativa:

- **Benchmarking study:** mede métricas (tempo na tarefa, taxa de conclusão) *e* conversa com o usuário.
- **Heuristic evaluation (avaliação heurística):** conta quantas vezes o produto viola uma lista de boas práticas (ex.: as **10 Heurísticas de Nielsen**).
- **A/B testing:** quando você não sabe como uma mudança vai afetar uma métrica, rode um teste A/B e **meça o impacto de verdade**.
- **Olhar o analytics (Google Analytics etc.):** achou um padrão na entrevista? Vá ao analytics ver se os números confirmam.

---

## 3. Exemplo prático: o caso *Tech and Us* (Dscout)

O guia traz um caso real de métodos mistos em ação, num estudo sobre como as pessoas se sentem em relação às big techs. Repare como ele **alterna quali e quanti várias vezes**, num fluxo iterativo:

1. **Quali generativo (n=100):** perguntas abertas + vídeos de 60s sobre percepção de tecnologia. Descoberta: as pessoas *falam* de desconfiança e regulação, mas a percepção geral é **majoritariamente positiva**. → Isso deu *direção*.
2. **Quanti / survey (n=1.000):** espelharam o estudo num questionário grande pra validar. Resultado: positividade ainda maior.
3. **Quanti de validação da amostra:** perceberam um viés — só tinham pesquisado lares "conectados". Refizeram com amostra probabilística incluindo lares rurais sem internet. Resultado: **quase não mudou** (ou seja, o achado era robusto).
4. **Quali de novo (n=100):** voltaram ao qualitativo pra entender o **porquê** da positividade, com perguntas abertas e vídeos selfie.

Note o padrão: **macro ↔ micro ↔ macro ↔ micro**, cada etapa respondendo uma dúvida levantada pela anterior. Isso é triangulação na prática.

---

## 4. Cases reais no mundo (e a ponte com teste A/B)

**Google — HEART na vida real.** O framework HEART não é teoria de paper: ele nasceu *dentro* do Google e é usado em produtos como Gmail, YouTube e Chrome pra decidir o que medir. Quando o YouTube decide se um novo layout é "melhor", a pergunta não é só "as pessoas clicam mais?" (Engagement) mas também "elas voltam?" (Retention) e "concluem o que queriam?" (Task success) — e essas métricas são o **critério de vitória de testes A/B** rodados em escala de bilhões de usuários.

**Booking.com — o casamento clássico quali + A/B.** A Booking é famosa por rodar **milhares de testes A/B simultâneos**. Mas A/B testing sozinho só responde "qual variação venceu" — ele **não te diz o que testar**. As ideias de *quais* mudanças valem o teste vêm de pesquisa qualitativa: entrevistas, gravações de sessão, observação de onde os usuários travam. Ou seja: **quali (generativo) gera a hipótese → A/B (somativo) mede o impacto.** É métodos mistos puro.

**Microsoft / Bing.** O time de experimentação da Microsoft conta um caso célebre: uma mudança aparentemente trivial na forma de exibir títulos de anúncios, sugerida e depois validada por A/B, gerou +12% de receita. A ideia surgiu de análise qualitativa de comportamento; o **veredito** veio do experimento controlado.

**Spotify, Netflix, Airbnb** seguem a mesma lógica: pesquisa qualitativa (entrevistas, diary studies) descobre *necessidades e fricções*; testes A/B e analytics *medem e validam* as soluções em larga escala.

> **A frase que conecta tudo:** o teste A/B é um método **comportamental, quantitativo e somativo** (ele mora num cantinho bem específico do mapa 3D da NN/g). Ele é poderosíssimo pra responder *"qual versão é melhor?"*, mas **cego** pra responder *"por quê?"* e *"o que mais deveríamos tentar?"*. É aí que ele precisa dos métodos qualitativos. Teste A/B sem pesquisa qualitativa é como ter um juiz de futebol sem ninguém pra escalar o time: ele sabe apontar o vencedor, mas não sabe quem deveria estar em campo.

---

## 5. Conexão com o módulo

Este é o **primeiro autoestudo de UX** do módulo, então ele funciona como uma *fundação* para várias coisas que virão. A conexão mais forte já disponível no [README](../../README.md):

- **Computação — [Autoestudo 06: Fundamentos de Programação de Testes A/B](../../computacao/autoestudo-06-fundamentos-de-programacao-de-testes-ab/02-explicacao.md).** Aquele autoestudo trata do *como* tecnicamente rodar um teste A/B. Este aqui te dá o **lugar do teste A/B no ecossistema de pesquisa**: ele é *um* método (comportamental/quantitativo/somativo) que quase nunca deve andar sozinho. Os dois se complementam diretamente — um te ensina a executar o experimento, o outro te ensina *quando ele faz sentido* e *com o que combiná-lo*.

E olhando o cronograma à frente, este autoestudo planta sementes para vários outros temas do módulo: **Formulação de Hipóteses Estatísticas** (Matemática) — a hipótese que o A/B testa muitas vezes nasce do qualitativo; **Experimentação em produtos digitais** (Negócios); e vários autoestudos de UX sobre usabilidade, arquitetura da informação e protótipos, que são exatamente os métodos formativos descritos aqui.

---

## 6. Resumo estruturado

- **Métodos mistos** = atacar uma pergunta de pesquisa com mais de um método pra ter um quadro mais completo. Brilha em perguntas estratégicas/ambíguas, não em perguntas estreitas.
- **4 dimensões pra posicionar qualquer método:**
  1. **Quali ↔ Quanti** — "por que/como" vs. "quantos/quanto".
  2. **Atitudinal ↔ Comportamental** — "o que dizem" vs. "o que fazem" (frequentemente divergem!).
  3. **Contexto de uso** — natural / roteirizado / limitado / sem uso.
  4. **Tempo** — generativo (achar direção) / formativo (melhorar) / somativo (medir).
- **Sequenciamentos:** macro→micro, micro→macro, iterativo. Sempre **fluxo único**: cada método informa o próximo.
- **Triangulação:** confirmar o mesmo achado por ângulos diferentes = mais confiança.
- **Análise:** top-down (quanti guia o quali) ou bottom-up (quali gera temas, quanti valida).
- **HEART (Google):** Happiness, Engagement, Adoption, Retention, Task success — o vocabulário quantitativo da UX, escolhido via **Goals → Signals → Metrics**.
- **Teste A/B** = método comportamental + quantitativo + somativo. Mede "qual venceu", mas precisa do qualitativo pra saber *o que testar* e *por quê*.

---

## 7. Auto-reflexão (pra pensar sozinha)

1. Pense num produto que você usa todo dia. Se você quisesse descobrir *por que* as pessoas abandonam ele, qual **sequenciamento** usaria — macro→micro ou micro→macro? Por quê?
2. Uma pesquisa diz que 80% dos usuários "adorariam" um modo escuro no app. Por que essa informação **atitudinal** não basta pra decidir construir o modo escuro — e qual método **comportamental** confirmaria a decisão?
3. Se você fosse rodar um teste A/B numa nova tela de checkout, quais das 5 métricas do **HEART** você escolheria como critério de vitória, e qual método **qualitativo** você rodaria *antes* pra decidir o que mudar na tela?
