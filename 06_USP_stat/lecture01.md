# IBI5086 - Aula 01

# IBI-5086 - Estatística para Biologistas Computadorizados

[toc]

## Programa

Roteiro mais ou menos cronológico

- "Caracterize a estrutura dos dados" - fundamental
- Comparação de grupos 2 ou mais
- Análise multivariada (1 mês+)

## Literatura

- Livro do Michael Love (lul)
- Pegar o Hunter & Hunter!

## Aula 01 - Beginnings

### Estatística e conhecimento científico


![](https://i.imgur.com/Xytgheu.png)

- Sobre o ciclo do conhecimento científico, desde o aprendizado até a análise dos dados e de fato contribuição do conhecimento
- Antes da pesquisa ser realizada, o plano de pesquisa ser registrado é interessante, até as análises estatísticas serão feitas especialmente se considerando os problemas que virão depois

![](https://i.imgur.com/kysW8ao.png)

- Há divergências: tamanho amostral, como as variáveis são exploradas no estado da natureza.
- A investigação deve ser convergente em hipóteses, plano amostral e experimental, e análise de dados

### Irreprodutibilidade e falta de rigor estatístico

![](https://i.imgur.com/QM2JGgg.jpg)


- Análises que não servem pra aqueles dados
- Bancos de dados irreprodutíveis
- Artigo: "Machine learning causing science crisis"

### Pesquisas em áreas factuais

- Meu estudo é observacional ou experimental?

![](https://i.imgur.com/vSxHyEs.png)


- Observacional: uma janela para natureza, passivamente tira 'fotografias' do universo, sem controle de fatores (ex: casos de Covid em um dado local, distribuição de CNV em pacientes)
- Experimental: intervenção do experimentador; padrão-ouro: **ensaios clínicos controlados e aleatorizados** (efeito do tratamento e dose na resposta de expressão gênica)
  - Efeitos de confusão: precisam ser identificados; em relação a sexo, história ancestral, severidade da doença.
  - **Blocados**: blocos de tratamento para controle de variáveis de confusão

### Coleta de dados

![](https://i.imgur.com/rdqi41a.png)


- O que há de mais interessante: estabelecer relações causais a partir de dados observacionais

### Planejamento de experimentos

![](https://i.imgur.com/6ABtvQP.png)

- Se mexer na aleatorização, avise no experimento

### Pra que planejar experimentos?

![](https://i.imgur.com/58q1lhy.png)

- Controlar o efeito das cagadas
- Reduzir o efeito das variações

![](https://i.imgur.com/4S0IZYz.png)

- Planejar para reduzir o erro de forma válida é o grande desafio

![](https://i.imgur.com/0tEoYqD.png)


### Classificação de variáveis & modelo estatístico

![](https://i.imgur.com/KgFpJKT.png)

Como modelar problemas?

![](https://i.imgur.com/zeZObj2.png)

- Correlação com o uso de oxigênio

![](https://i.imgur.com/CPSG0u2.png)


- Em M2, são adicionados os estimadores baseados na corrida ($B_2X_2$), sendo 0 em repouso e 1 se correu;
- Em M3, simultaneamente e aditivamente a variável explicativa ($y$ - pulsação) é a soma de um coeficiente linear ($B_1X_1$) que leva em conta o tratamento repouso ou corrida ($B_2X_2$). Modelo chamado de **aditivo nas variáveis preditoras**.
  - Nesse modelo é possível estimar o efeito do tratamento ($B_2$) corrigido pela pulsação inicial ($B_1$)
  - $B_2$ pode mudar muito entre M2 e M3!
  - O efeito é dito "ajustado por uma co-variável"
  - Gradativamente, mais níveis de "lentes" são adicionados, no intento de reduzir o erro e observar mais concisamente a natureza
  - Como se avaliam modelos?
- M4 é o modelo com interação dos efeitos:
  - Efeito da variável $X_1$;
  - Efeito da variável $X_2$;
  - Efeito da interação $X_1 * X_2$ 
  - Modelo "não-aditivo nas variáveis explicativas", com um fator de interação das variáveis.

![](https://i.imgur.com/jxd4VZw.png)


- Traçar as duas retas para um grupo e para outro;
- Coeficiente angular é o valor de abertura da reta (0,912)
- Coeficiente linear é onde a reta começa no eixo X (72,7 ou 19,1)

### Classificação de variáveis

![](https://i.imgur.com/vGQ9bQA.png)

- Os modelos são unificados; mas com vantagens distintas

### Princípios na prática

![](https://i.imgur.com/Z5JUUTx.png)


- O que quero extrair dos meus dados?
  - Boas estimativas dos parâmetros: são aquelas em que o modelo ajustado é apropriado para a estrutura dos dados e para o planejamento do experimento; na prática, estimativas do efeitos X sobre Y, extraindo uma "boa" predição de Y.
  - Qual é o valor de Y predito de acordo com meu modelo?
  - Pra outras finalidades, eu quero saber a variável resposta $\hat{y}$.
- Evitar erros sistemáticos:
  - Vícios de seleção (fornecedor, técnico de laboratório, desgaste de aparelho)
  - Anotar fontes de variação conhecida (peso e idade de animal; natureza do solo)
- Controlar flutuações desconhecidas?
  - Aleatorização faz o "balanceamento" do erro, gerando grupos comparáveis com características semelhantes. Se feito com probabilidade ótima, os grupos são próximos.
  - Cegamento é extremamente importante, reduz viéses de percepção. Já garante o planejamento do experimento ideal *a priori*, com resultados convergentes.
  - *A posteriori* a estatística pode corrigir o efeito de fontes desconhecidas, ajustando modelos e concentrando os erros desconhecidos para os resíduos - respostas filtradas, corrigidas.

### Como garantir análises válidas?

![](https://i.imgur.com/5RcV5FE.png)

- Como é a variável resposta?
  - Quantitativa ou qualitativa? 
  - São necessárias co-variáveis?
  - O modelo é adequado para os dados?
  - Você checou os pressupostos?
  - Você fez os diagnósticos do resíduo do modelo?

![](https://i.imgur.com/jc9rqFU.png)


- Aplicar para a vida!
- Registrar intervalos:
  - Intervalos de confiança;
  - Intervalos de compatibilidade com os dados;
  - Análises de diagnóstico;

### Para ler e entender

![](https://i.imgur.com/duy4ll5.png)


### Experimentos comparativos (motivação)

![](https://i.imgur.com/lsQgX3w.png)


- Premissas para usar testes e abordar o erro
- Como testar tais populações
- Como obter dados para realizar testes
  - Como testar em sub-populações (permutações)

A partir de agora, vamos comparar grupos, assumindo que a variável-resposta é quantitativa.

- Teste *t*
- Teste Wilcoxon (não-paramétrico)

### Comparando duas populações

![](https://i.imgur.com/YKkzoBq.png)


- ANOVA clássica: variável é quantitativa e unidimensional
  - Variável explicativa sempre é o $f(x)$, os preditores - quem influencia na variável resposta. São as variáveis independentes, aquilo que se tem.
  - Depois veremos uma variável explicativa aleatória.
  - Por enquanto, a variável será fixa (sexo, idade), um fator, uma categoria, qualitativa nominal
- MANOVA: variável-resposta multidimensional

### Raciocínio estatístico clássico

![](https://i.imgur.com/Wp6V9zl.png)


- Problemas modernos e "perca de eixo"
  - Estatística como arte;
  - N muito grande;
  - Alta dimensionalidade;

### Dataset 01 no R

- Coeficiente de variação é o desvio padrão pela média:

$$
\frac{dp}{mean}
$$

- Pode ser comparado entre diferentes unidades experimentais!
- Erro padrão é o $dp$ dividido pela $\sqrt{\hat{Y}}$ 
- Erro padrão é a acurácia experimental!



# Estudar por fora

- Tabelas de contingência
- Álgebra linear

# Siglas

- Erro padrão (SEM) da população ($\sigma_\bar{x}$)

$$
{\sigma }_{\bar {x}}\ ={\frac{\sigma}{\sqrt{n}}}
$$

