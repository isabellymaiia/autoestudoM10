# Hipóteses em Usabilidade & Concepção dos Redesigns de Interface — Material original

> **Matéria:** UX · **Autoestudo:** 03 · **Data:** 21/05/2026
>
> Compilação de três materiais de referência:
>
> 1. **Leis da Psicologia Aplicadas à UX — Parte 1**, Thaís Polonio (Medium, 19/08/2021) — resumo do livro de Jon Yablonski.
> 2. **Leis da Psicologia Aplicadas à UX — Parte 2**, Thaís Polonio (Medium, 10/11/2021).
> 3. **UI Design Dos and Don'ts** — Apple Developer / Human Interface Guidelines.

---

# Parte 1 — Leis da Psicologia Aplicadas à UX (Polonio, P1)

> Usando a psicologia para projetar produtos e serviços melhores | Um resumo do livro de Jon Yablonski.

Sabemos que o designer é um profissional multidisciplinar e precisa ter conhecimento em diversas áreas: a psicologia é uma delas. Na área de experiência do usuário, o trabalho é feito de e para pessoas, e isto exige certo conhecimento na área de psicologia para que possamos entender, ainda que de maneira introdutória, como os usuários se comportam e interagem com as interfaces digitais. Em sua publicação, Jon Yablonski trouxe de maneira rápida e de fácil entendimento os principais conceitos de psicologia aplicados a UX. Neste artigo, farei um apanhado dos primeiros cinco conceitos (do total de dez) de maneira resumida sobre o que aprendi.

## Lei de Jakob

> "Os usuários passam a maior parte do tempo em outros sites e preferem que o seu site funcione da mesma maneira que todos os outros sites que já conhecem."

Esta Lei foi apresentada em 2000 por **Jakob Nielsen** (especialista em usabilidade), que a descreveu como a tendência de os usuários aplicarem seus conhecimentos com base em suas experiências cumulativas em sites anteriores. Em outras palavras, quanto menos tempo o usuário precisar gastar entendendo uma interface, mais tempo ele terá para realizar seus objetivos, e a familiaridade desempenha um papel fundamental neste processo.

Podemos ver exemplos nos sites de comércio eletrônico. A maioria utiliza dos mesmos elementos para causar familiaridade: campos de busca, perfil, carrinho de compras. (Exemplos citados: Zattini/Netshoes, Amazon.)

Esta Lei não defende que não possamos inovar, apenas que devemos fazê-lo com cautela. É o clássico **"em time que está ganhando, não se mexe"**.

## Lei de Fitts

> "O tempo para acessar um alvo é uma função da distância e do tamanho do alvo."

Quando projetamos bons produtos e serviços, prezamos sempre pela usabilidade. Neste sentido, a Lei de Fitts defende que:

- Os alvos de toque devem ser **grandes o suficiente** para que os usuários cliquem sem dificuldades, e para isto temos as recomendações de tamanho mínimas (podendo ser excedidas sempre que necessário):
  - **Apple — Human Interface Guidelines:** 44 x 44 pt (pontos)
  - **Google — Material Design Guidelines:** 48 x 48 dp (density independent pixels)
  - **WCAG — Web Content Accessibility Guidelines:** 44 x 44 CSS px (pixels)
  - **Nielsen Norman Group:** 1 x 1 cm (centímetros)

- É preciso um bom **espaçamento entre os ícones** para que não sejam clicados erroneamente, e para isto usamos as diretrizes do Google Material Design, que recomendam que os alvos de toque sejam separados por um espaço de **8 dp**. A nível de informação, Jon trouxe o estudo da MIT Touch Lab, onde diz que o dedo de um adulto médio mede entre **10 e 14 mm** e a média da ponta do dedo fica entre **8 e 10 mm²**.

- Dimensionamento e espaçamento mencionados, é hora de falar sobre a **posição dos alvos de toque**. Esta parte nem sempre é óbvia, pois muda de acordo com o contexto do usuário, dispositivo etc. Considerando os smartphones, algumas áreas podem ser difíceis de clicar quando seguramos o dispositivo com apenas uma mão. Segundo **Steve Hoober**, as pessoas preferem visualizar e tocar no **centro da tela**, portanto é aí a precisão mais alta. (Referência visual: **Thumb Zone — Steven Hoober**.)

Ainda nesta Lei, podemos citar a **acessibilidade** exemplificando com o iPhone, que permite acesso à metade superior da tela (recurso de "alcançabilidade").

## Lei de Hick

> "O tempo necessário para tomar uma decisão aumenta com o número e a complexidade das opções disponíveis."

Redundância e excesso criam confusão; é baseado nisto que nós, designers, buscamos sintetizar informações e facilitar processos. Formulada em **1952** pelos psicólogos **William Edmund Hick** e **Ray Hyman**, a Lei de Hick aponta que aumentar o número de opções disponíveis aumenta de forma **logarítmica** o tempo de decisão. Resumindo: as pessoas demoram mais para tomar uma decisão quando têm mais opções para escolher.

Existe uma fórmula real para representar essa relação (apresentada pela CRO-Tool).

É fato que você não precisa entender de matemática para tirar uma conclusão disso tudo: a Lei de Hick busca **diminuir a carga cognitiva do usuário**, tornando as decisões mais simples, claras e fáceis. Um exemplo clássico são os controles de TV modificados para simplificar a interface — onde somente os comandos "essenciais" ficam disponíveis para escolha.

## Lei de Miller

> "A pessoa média pode manter apenas 7 (+/- 2) itens em sua memória de trabalho."

Este conceito tem muita similaridade com os conceitos básicos do design, como **hierarquia** e **chunking** (separação em blocos). Quando publicou seu artigo, em **1956**, **George Miller** observou que a capacidade de retenção de memória em adultos jovens era de aproximadamente 7. Não se concentrando apenas no número 7, mas no conceito de separação em blocos, Miller concluiu que:

> "O tamanho dos blocos não parecia importar — sete palavras individuais podiam ser mantidas na memória de curto prazo tão facilmente quanto sete letras. Embora existam fatores que influenciem quantos blocos um indivíduo pode reter (contexto, familiaridade com o conteúdo, capacidade específica), a lição é a mesma: a memória de curto prazo humana é limitada e o chunking nos ajuda a reter informações com mais eficácia."

**Exemplos:**
- Um número de telefone (EUA) com e sem aplicação de chunking (`5551234567` vs `(555) 123-4567`).
- Uma lista quando não separada por blocos e quando sim.

Neste caso, a **hierarquia textual, formatação e contraste** também se aplicam. Em UX, estamos falando de **simplificar a informação e facilitar a compreensão**, e podemos usar as bases do design para isso (evitando o famoso "muro de texto"). (Exemplo visual: Conta Azul Design.)

## Lei de Postel

> "Seja conservador no que faz, seja liberal no que aceita dos outros."

Foi assim que **Jon Postel** introduziu o que chamou de **princípio da robustez**, onde a ideia no início era ser uma diretriz para a engenharia de redes, no que diz respeito à transferência de dados por meio de redes de computadores. Essa filosofia, quando aplicada à experiência do usuário, significa **projetar boas experiências humanas**. Neste sentido, a Lei de Postel tem uma abordagem de design parecida com a filosofia da interação humano-computador:

> "Devemos prever praticamente qualquer coisa em termos de entrada, acesso e capacidade, fornecendo uma interface confiável e acessível."

O exemplo mais comum são os **formulários de entrada**, muito presentes no ambiente digital. Em essência é por meio deles que a interação entre humanos e computador acontece: um produto ou serviço requer informações, estas que serão disponibilizadas pelo usuário e enviadas para processamento. Colocando a Lei de Postel em prática ainda nos formulários: **seja conservador com o número de informações solicitadas** — quanto mais energia e esforço cognitivo exigir dos usuários, menor será a qualidade das decisões tomadas.

A **flexibilidade do sistema** também é levada em consideração, visto que muitas vezes ocorre uma divergência entre a informação que o usuário fornece e a que o sistema espera receber; para isto os computadores devem ser robustos para aceitar os variados tipos de entrada humana. Isto pode ser feito de diversas maneiras, mas as preferíveis são as que exigem menos esforço.

**Exemplos:**
- **Apple Face ID** permite desbloquear seu iPhone/iPad e autenticar compras com segurança.
- **Design responsivo**, baseado em grades fluidas e imagens flexíveis. Permite que o conteúdo responda de maneira fluida a diferentes contextos de visualização.
- **Componente de pesquisa aprimorado**, que oferece uma caixa de pesquisa e suporte de voz para dispositivos compatíveis.

---

# Parte 2 — Leis da Psicologia Aplicadas à UX (Polonio, P2)

> Continuação do resumo do livro de Jon Yablonski: Regra do pico-final, Efeito estética-usabilidade, Efeito von Restorff, Lei de Tesler e Limiar de Doherty.

## Regra do pico-final

> "As pessoas julgam uma experiência, em grande parte, baseadas em como se sentiram no ponto mais alto (pico) e no final, em vez de na soma total ou média de cada momento da experiência."

Para entendermos melhor a Regra do pico-final, temos de ter em mente que o ser humano é sensorial e que a emoção afeta diretamente a sua experiência com determinado produto ou serviço.

**Daniel Kahneman**, em **1993**, começou a explorar os estudos nesta área através de um experimento, onde participantes foram submetidos a duas versões diferentes de uma única experiência desagradável:

- **Versão 1:** os participantes mergulhavam a mão em água a 14 °C por 60 segundos.
- **Versão 2:** os participantes mergulhavam a outra mão em água a 14 °C por 60 segundos e, em seguida, a mantinham submersa por mais 30 segundos enquanto a água era aquecida a 15 °C.

Quando questionados sobre qual experimento estes participantes repetiriam, **a maioria estava disposta a repetir o segundo** — apesar da exposição a temperaturas desagradáveis ter sido **mais longa**. Aliando este estudo a outros posteriores juntamente com **Donald Redelmeier**, Kahneman concluiu que os pacientes avaliavam o desconforto de sua experiência **com base na intensidade da dor nos piores momentos e nos momentos finais**, independente da duração ou variação na intensidade da dor durante o procedimento.

**Exemplo cotidiano de UX:** a **Uber**. Quando o aplicativo passou a fornecer o tempo estimado de chegada e trouxe maior transparência operacional e clareza em relação a cada etapa do processo, fazendo com que o cliente sinta que está continuamente avançando em direção ao seu objetivo. Ao se concentrar na percepção das pessoas sobre o tempo de espera, a Uber conseguiu **reduzir sua taxa de cancelamento** e reduzir o que poderia se tornar um pico emocional negativo na experiência. (Exemplo: Uber Express POOL.)

## Efeito estética-usabilidade

> "Em geral os usuários percebem um design esteticamente agradável como um design mais utilizável."

A estética da interface de um sistema afeta a percepção dos usuários sobre sua usabilidade, confiança e credibilidade — foi o que disse o estudo **"O que é bonito é utilizável"**, de **Noam Tractinsky**, em **2000**.

> "Estudos mostraram que as pessoas formam uma opinião sobre um site em **50 milissegundos** depois de vê-lo, e que o apelo visual é um fator determinante principal. Curiosamente, a opinião formada durante esse breve período raramente muda à medida que os usuários passam mais tempo no site." — Lindgaard, Gary Fernandes, Cathy Dudek e J. Brown

Vejamos que duas empresas cruciais na história do Design colocaram a estética no centro das suas escolhas e acabaram fazendo uso do efeito estética-usabilidade em seus produtos.

A primeira é a **Braun**, empresa alemã de eletrônicos, que sob a direção de **Dieter Rams** influenciou designers através do equilíbrio entre **minimalismo funcional e beleza estética**. Rams enfatizava o **"menos, mas melhor"**, e sua abordagem de que a função deve seguir a forma resultou diretamente em alguns dos produtos mais bem projetados já fabricados. (Exemplo: Toca-discos Braun SK4, pioneiro da nova linguagem do Design.)

Seguindo o legado do minimalismo funcional, temos a **Apple**. A influência da filosofia de design da Braun nos produtos da Apple é bastante aparente em dispositivos como iPhone, iPad e iMac, onde há o equilíbrio entre a estética minimalista e a facilidade de uso.

Para concluir, não podemos deixar de lado que assim como as pessoas tendem a acreditar que experiências bonitas também funcionam melhor, elas tendem a **relevar mais os problemas de usabilidade**. Portanto, temos de nos atentar para que os problemas de usabilidade não sejam mascarados durante os testes com usuários.

## Efeito von Restorff

> "Quando vários objetos semelhantes estão presentes, é mais provável que aquele que difere dos demais seja lembrado."

Vivemos na era da informação e nosso julgamento sobre o que é relevante ou não acontece de forma muito rápida, pois nossa atenção é um recurso limitado. Pensando nisso, a psiquiatra alemã **Hedwig von Restorff** realizou um estudo, em **1933**, empregando o **paradigma do isolamento**: os participantes do estudo foram apresentados a uma lista de itens categoricamente semelhantes e lembraram melhor dos itens que eram distintamente diferentes.

> "Em outras palavras, a memória é aprimorada para itens de um conjunto que são visual ou conceitualmente isolados dos outros itens."

Como designers, temos como dar ênfase visual através das **cores, formas, tamanhos, posições e movimentos**, podendo guiar e influenciar a atenção dos usuários.

**Exemplos visuais citados:**
- Uso do contraste para chamar a atenção do usuário para ações importantes.
- Pistas visuais na aplicação do Efeito von Restorff em uma tabela de preços (linha do plano "recomendado" destacada).
- Uso do Efeito von Restorff para chamar a atenção para as notificações (badges vermelhos).

## Lei de Tesler

> "Todos os processos têm um núcleo de complexidade que não pode ser removido e, portanto, deve ser assumido pelo sistema ou pelo usuário. Tome cuidado para não simplificar as interfaces ao ponto de abstração."

**Larry Tesler**, ao observar a maneira que os usuários interagiam com um aplicativo, chegou à conclusão que a maneira como lidam é tão importante quanto o próprio aplicativo. É importante reduzir a complexidade do aplicativo e da interface, no entanto, **sempre há uma quantidade inerente de complexidade que não pode ser removida**.

Uma maneira comum e cotidiana de ilustrar a Lei de Tesler é através do **aplicativo de e-mail**. Nele, você precisa informar quem está enviando o e-mail e quem irá receber — sem uma destas informações, o e-mail não poderá ser enviado. Para reduzir a complexidade, algumas ferramentas de sugestão de destinatário aparecem quando você começa a digitar o endereço, mas é válido ressaltar que **a complexidade não desapareceu completamente, ela apenas foi abstraída** para reduzir o esforço exigido do usuário.

Outro caso bastante comum onde podemos aplicar a Lei de Tesler é nas **páginas de pagamento em sites de compra online**. É inevitável que tenhamos que preencher informações pessoais para efetuar as compras, mas é possível simplificar: hoje, alguns sites já disponibilizam a opção do endereço de cobrança ser o mesmo do endereço de envio, o que diminui a complexidade sem que ela tenha desaparecido completamente.

Durante este processo de simplificação, temos de nos atentar para que as informações básicas para que os usuários tomem decisões fundamentadas estejam presentes, para **não simplificar tanto ao ponto da abstração**. A Lei de Tesler desafia a nós, designers, para, mais uma vez, fazer o **gerenciamento da complexidade**.

## Limiar de Doherty

> "A produtividade aumenta quando um computador e seus usuários interagem a um ritmo que garante que nenhuma das partes precisa esperar pela outra."

Um dos principais recursos para boas experiências do usuário é o **desempenho**, por isso Jon Yablonski trouxe cinco observações importantes:

1. Forneça **feedback do sistema em até 400 ms** para manter a atenção dos usuários e aumentar a produtividade.
2. Use o **desempenho percebido** para melhorar o tempo de resposta e reduzir a percepção de espera.
3. A **animação** é uma maneira de envolver visualmente as pessoas enquanto o carregamento ou o processamento está acontecendo em segundo plano.
4. As **barras de progresso** ajudam a tornar os tempos de espera toleráveis, independentemente da sua precisão.
5. Adicionar propositalmente um atraso a um processo pode aumentar seu valor percebido e incutir uma sensação de confiança, mesmo quando o processo em si leva menos tempo.

Existem muitos fatores que podem afetar o desempenho dos sites e aplicativos; o mais significativo é o **peso da página**. De acordo com a **HTTP Archive**, o peso médio das páginas era próximo a **609 KB no desktop e 262 KB no mobile (2010–2011)**. **Em 2019**, este número salta para **1940 KB em desktops e 1745 KB no celular**.

Se avaliarmos o **tempo de resposta** — outro fator determinante:

- **100 ms** → parece instantâneo.
- **100 a 300 ms** → começa a ficar perceptível ao olho humano e as pessoas começam a sentir menos controle.
- **> 1 segundo** → a atenção é desviada e informações importantes da tarefa começam a se perder. (Intrigante: nos primórdios da computação, **2 segundos** eram um limite aceitável.)

**Exemplos:**
- O **Facebook** exibe um esboço da tela (**skeleton screen**) para ajudar o site a parecer que carrega mais rápido.
- A **Apple** fornece uma barra de progresso durante as atualizações.

Para finalizar, Jon Yablonski nos chama para um debate importante: o da nossa responsabilidade, como designers, para entender e perceber como **a mente humana é suscetível à tecnologia persuasiva** e como o comportamento pode ser moldado.

> "Os objetivos corporativos da empresa e os objetivos humanos do usuário final raramente estão alinhados e, na maioria das vezes, os designers são um canal entre eles. É hora de enfrentarmos essa tensão e aceitarmos que é nossa responsabilidade criar produtos e experiências que apoiem os objetivos e o bem-estar dos usuários. Devemos construir tecnologia que melhore a experiência humana em vez de substituí-la por interação virtual e recompensas."

---

# Parte 3 — UI Design Dos and Don'ts (Apple)

> Apple Developer / Human Interface Guidelines.
>
> "Engaging user experiences are built on a foundation of solid interface design. Before you start coding, consider these fundamental design concepts for building clean, efficient interfaces for a broad set of users."

Eixos centrais que a Apple aborda: **Interactivity · Readability · Graphics · Clarity**.

## Formatting Content

Create a layout that fits the screen of a device. Users should see primary content **without zooming or scrolling horizontally**.

## Touch Controls

Use UI elements that are **designed for touch gestures** to make interaction with your app feel easy and natural.

## Hit Targets

Create controls that measure **at least 44 points x 44 points** so they can be accurately tapped with a finger.

> **44 pt x 44 pt minimum.**

## Text Size

Text should be **at least 11 points** so it's legible at a typical viewing distance without zooming.

## Contrast

Make sure there is **ample contrast between the font color and the background** so text is legible.

## Spacing

**Don't let text overlap.** Improve legibility by increasing line height or letter spacing.

## High Resolution

Provide **high-resolution versions of all image assets**. Images that are not @2x and @3x will appear blurry on the Retina display.

## Distortion

Always display images at their **intended aspect ratio** to avoid distortion.

## Organization

Create an **easy-to-read layout** that puts controls **close to the content** they modify.

## Alignment

**Align** text, images, and buttons to show users how information is related.

---

## Design Resources (referência)

> Get tools, UI templates, and in-depth information for designing great apps that integrate seamlessly with Apple platforms.
