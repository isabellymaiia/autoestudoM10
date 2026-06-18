# Questão de Complementação — Economia da Atenção e Teste A/B

Questão estilo ENADE no formato **complementação**: um texto-base, uma frase incompleta, cinco asserções (I–V) que podem ou não completá-la e cinco alternativas.

---

## Enunciado

**TEXTO-BASE**

A atenção do usuário é um recurso escasso: cada segundo gasto num aplicativo ou site é disputado por empresas que transformam esse tempo em receita (publicidade, venda, retenção). Essa ideia, conhecida como **economia da atenção**, foi descrita já em 1971 por Herbert Simon, quando ele observou que "muita informação produz pouca atenção".

Nesse contexto, o **teste A/B** se tornou uma das principais ferramentas para decidir o que entra ou sai de um produto digital. Em vez de discutir qual versão de uma tela é melhor, a empresa mostra a versão A para metade dos usuários e a versão B para a outra metade, ao mesmo tempo, e mede qual gera mais cliques ou conversões. O método substitui o que se chama de **HiPPO** (*Highest Paid Person's Opinion* — a opinião da pessoa mais bem paga na sala) por evidência de comportamento real.

Mas a mesma ferramenta que melhora a experiência também pode ser usada para prender o usuário ao produto de forma abusiva. Em 2014, o Facebook conduziu um experimento em que manipulou, sem aviso, o conteúdo do feed de cerca de 700 mil pessoas para testar se posts mais positivos ou negativos afetavam o humor delas. O caso mostrou que rigor técnico não garante uso ético, e que a fronteira entre **otimizar a experiência** e **explorar a atenção do usuário** é uma escolha de produto, não uma consequência automática do método.

> **Termos úteis para a questão:**
> - **Teste A/B:** comparação entre duas versões (A e B) mostradas ao mesmo tempo para públicos sorteados, para identificar qual gera melhor resultado.
> - **Conversão:** quando o usuário faz a ação desejada (clicar, comprar, se cadastrar).
> - **Bounce rate (taxa de rejeição):** porcentagem de usuários que entram numa página e saem sem interagir.
> - **Busca interna:** quando o usuário usa a caixa de busca dentro do próprio site — sinal de que ele não encontrou o que queria pela navegação.
> - **Significância estatística:** medida que indica se a diferença entre A e B é real ou aconteceu por acaso. O padrão de mercado é 95% de confiança.
> - **Dado comportamental:** o que o usuário **faz** (cliques, tempo, compras).
> - **Dado atitudinal:** o que o usuário **diz** que pensa ou prefere (pesquisas, entrevistas).

**Considerando o texto-base, avalie as afirmações a seguir, que completam a frase:**

> *"A economia da atenção, aplicada à prática de testes A/B em produtos digitais, ..."*

**I.** parte do princípio de que a atenção é um recurso limitado e que, por isso, é mais confiável medir o que o usuário **faz** (dado comportamental) do que perguntar o que ele **prefere** (dado atitudinal). Isso dá ao teste A/B uma vantagem sobre decisões baseadas em opinião, mas não dispensa o uso de pesquisas qualitativas — como entrevistas — para entender **por que** o usuário se comporta daquela forma.

**II.** encontra na regra de "testar um elemento por vez" uma proteção ética contra a manipulação do usuário. Como o teste isola uma única variável de cada vez, o produto fica impedido, por desenho, de explorar simultaneamente vários gatilhos de atenção e, portanto, de manipular o comportamento do usuário.

**III.** reconhece, em sinais como **alta taxa de rejeição** numa página de categoria ou **muitas buscas internas** por termos que não existem no menu, indícios de que o usuário está gastando atenção sem encontrar o que procura. Diante desses sinais, é legítimo usar o teste A/B para validar mudanças na organização do conteúdo (por exemplo, renomear uma categoria).

**IV.** ao atingir 95% ou mais de significância estatística, resolve a questão ética levantada pelo experimento do Facebook de 2014. Isso porque, quando o sorteio dos grupos é feito de forma justa (todos os usuários têm a mesma chance de cair em A ou em B), é possível considerar que houve uma forma implícita de consentimento por parte dos participantes.

**V.** funciona em um terreno ambíguo: a mesma ferramenta que corrige problemas reais de experiência — como uma categoria mal nomeada que gera alta rejeição — pode também ser usada para prender o usuário ao produto contra o interesse dele. Por isso, decisões orientadas por dados precisam ser discutidas em conjunto entre as áreas de tecnologia, design, negócio e ética, e não tratadas como puramente técnicas.

**É correto apenas o que se afirma em:**

- **(A)** I e IV.
- **(B)** II e V.
- **(C)** I, III e V.
- **(D)** II, III e IV.
- **(E)** I, II, III, IV e V.

---

## Gabarito comentado (barema)

### Resposta correta: **(C) I, III e V**

A questão pede para o candidato separar três planos diferentes que costumam ser confundidos quando se fala em testes A/B:

1. **Plano metodológico** — o que o teste A/B permite afirmar (asserção I).
2. **Plano diagnóstico** — o que os dados de comportamento revelam sobre a experiência do usuário (asserção III).
3. **Plano ético** — os limites do que se deve otimizar, mesmo quando é tecnicamente possível (asserção V).

As asserções **II e IV** estão escritas para parecer corretas, mas cometem o mesmo tipo de erro: confundem uma **propriedade técnica do método** (isolar variáveis em II, atingir significância estatística em IV) com uma **garantia ética**. Esses dois planos são independentes — um teste pode ser tecnicamente impecável e ainda assim antiético, e foi exatamente isso que ficou claro no caso Facebook 2014.

---

### Análise de cada asserção

**I — CORRETA.**
A afirmação tem duas partes, e as duas estão certas:

- **Parte 1:** dado comportamental é mais confiável que dado atitudinal. Isso é verdade porque pesquisas mostram, repetidamente, que as pessoas dizem uma coisa e fazem outra (ex.: 90% das pessoas afirmam se preocupar com privacidade, mas aceitam todos os cookies em 1 segundo para ler uma receita). O teste A/B mede o que a pessoa faz de verdade.
- **Parte 2:** isso não dispensa pesquisa qualitativa. O teste A/B diz **qual versão ganhou**, mas não diz **por que** ganhou. Para entender o "por quê", são necessárias entrevistas, testes de usabilidade ou pesquisas com perguntas abertas.

A asserção é correta justamente por reconhecer **as duas metades**: a força do dado comportamental **e** sua insuficiência quando isolado.

**II — INCORRETA. (Distrator principal.)**
A asserção parte de uma regra real do teste A/B: mudar apenas uma coisa por vez para conseguir atribuir o efeito à mudança certa. Até aí, tudo bem. O problema é a **conclusão**: dizer que essa regra impede a manipulação do usuário.

A regra de "um elemento por vez" existe por motivo **estatístico** (saber a qual variável atribuir o efeito), não por motivo **ético**. Prova disso: o experimento do Facebook em 2014 também alterou **um único elemento** — a quantidade de posts positivos ou negativos no feed — e mesmo assim foi considerado antiético, porque os usuários não sabiam que estavam participando.

Quem marca essa asserção provavelmente está colando "boa prática técnica" em "boa prática ética", como se uma derivasse da outra. Não deriva.

**III — CORRETA.**
A asserção descreve corretamente o que se chama de "sinais de alerta" no dado de uso:

- **Alta taxa de rejeição numa categoria:** o usuário clicou, viu, e saiu — provavelmente porque o nome da categoria prometia uma coisa e a página entregou outra.
- **Muitas buscas internas por um termo que não está no menu:** o usuário está literalmente dizendo "eu queria isso, mas não achei navegando".

Esses dois sinais indicam **atrito** entre o que o usuário procura e o que a interface oferece — ou seja, atenção gasta sem retorno. A asserção também acerta ao dizer que o dado **levanta a hipótese** (algo está errado com essa categoria), mas é o **teste A/B que valida** se a mudança proposta (renomear, reorganizar) realmente resolve. Esse é o ciclo correto: dado quantitativo aponta o problema; teste A/B valida a solução.

**IV — INCORRETA. (Distrator mais perigoso.)**
A asserção usa vocabulário técnico (95% de significância, aleatorização) para concluir algo que não faz sentido: que rigor estatístico resolve um problema ético.

Significância estatística mede **uma coisa só**: a chance de que a diferença observada entre A e B tenha acontecido por acaso. Ela **não tem relação** com o consentimento do usuário, com transparência, ou com o direito de saber que está sendo testado.

A ideia de "consentimento implícito por aleatorização" é ainda mais problemática: o sorteio justo é exatamente o que **impede** o usuário de optar por não participar — ou seja, **piora** o problema ético em vez de resolvê-lo. Legalmente, leis como LGPD (Brasil) e GDPR (Europa) exigem **consentimento informado e explícito**, não "implícito por estatística".

Quem marca essa asserção tende a acreditar que, se um método é matematicamente sólido, ele também é eticamente legítimo. Não é o caso — são dois julgamentos independentes.

**V — CORRETA.**
A asserção resume bem a tensão central do tema: a mesma ferramenta serve para corrigir problemas reais (uma categoria mal nomeada que faz o usuário desistir) e para prender o usuário ao produto além do que seria saudável para ele. Por isso, decidir **até onde otimizar** não é uma escolha técnica — envolve produto, design, negócio e ética.

A conclusão da asserção (decisões orientadas por dados precisam ser discutidas em conjunto entre várias áreas, e não tratadas como puramente técnicas) é coerente com a ideia de que ferramentas neutras podem ter usos legítimos e ilegítimos, dependendo da intenção e do contexto.

---

### Análise de cada alternativa

| Alternativa | Veredito | Por que falha (ou acerta) |
|---|---|---|
| **(A) I e IV** | Incorreta | Acerta I (fundamento metodológico), mas inclui IV — confunde rigor estatístico com legitimidade ética. Quem marca (A) entende bem o lado técnico do método, mas falha em separar o que é cálculo do que é decisão moral. |
| **(B) II e V** | Incorreta | Acerta V (a tensão ética do método), mas inclui II. É uma alternativa "irônica": V reconhece que o método tem uso ambíguo, mas II pretende eliminar essa ambiguidade por desenho técnico. As duas asserções se contradizem — marcar as duas é não perceber a contradição. |
| **(C) I, III e V** | **Correta** | Forma um arco coerente: I fundamenta o método (por que medir comportamento), III aplica esse método para diagnosticar problemas reais de experiência, V reconhece que a ferramenta tem limites éticos que o método sozinho não resolve. |
| **(D) II, III e IV** | Incorreta | Acerta III, mas combina II e IV — os dois erros categoriais da questão. Tipicamente marcada por quem confunde "boas práticas técnicas" com "salvaguardas éticas". |
| **(E) I, II, III, IV e V** | Incorreta | Marcar tudo é o sintoma clássico de não distinguir os planos metodológico e ético — exatamente o erro que II e IV foram desenhados para induzir. |

---

### Critérios de avaliação (barema analítico)

Caso a questão seja aplicada em formato discursivo (com justificativa exigida), sugere-se a seguinte distribuição:

| Critério | Peso | Descrição |
|---|---|---|
| **Acerto da alternativa (C)** | 30% | Identificação correta de I + III + V como o conjunto certo. |
| **Justificativa das corretas** | 25% | Demonstrar entendimento de que: (I) dado comportamental é mais confiável que declarado, mas precisa de qualitativo para entender causas; (III) sinais de uso revelam atrito e o A/B valida correções; (V) o método tem usos legítimos e abusivos. |
| **Refutação da asserção II** | 20% | Reconhecer que "um elemento por vez" é regra **técnica** (para atribuir causa ao efeito), não **ética**. Mencionar o caso Facebook 2014 como contraexemplo (mudaram um único elemento e mesmo assim foi antiético). |
| **Refutação da asserção IV** | 20% | Distinguir significância estatística (mede acaso) de legitimidade ética (exige consentimento informado). Refutar a ideia de "consentimento implícito por sorteio". Pode citar LGPD/GDPR. |
| **Articulação ampla** | 5% | Conectar argumento com mais de uma dimensão (técnica, de experiência do usuário, de negócio e ética). |

**Notas para correção discursiva:**

- Quem acerta (C) **sem justificar** a refutação de II ou IV deve receber nota parcial — o objetivo da questão é diagnosticar a distinção entre os planos técnico e ético.
- Quem justifica corretamente a refutação de II ou IV **mesmo marcando alternativa errada** deve receber crédito parcial relevante — a distinção conceitual é o aprendizado central.
- Não é necessário que o candidato cite Herbert Simon ou use o termo "economia da atenção" em sentido técnico — o texto-base já fornece esse contexto. O que se avalia é a capacidade de **raciocinar** com ele.
