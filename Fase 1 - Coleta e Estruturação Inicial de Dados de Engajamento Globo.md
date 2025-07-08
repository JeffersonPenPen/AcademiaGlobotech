## Projeto Formação em Tecnologia Rede Globo

## Módulo DS-PY-19: Lógica de Programação em Python

### Fase 1: Coleta e Estruturação Inicial de Dados de Engajamento Globo

___

## 1\. Introdução e Contextualização

Bem-vindos à Fase 1 do projeto unificado **"Análise de Engajamento de Mídias Globo"**! Ao longo dos próximos módulos, construiremos progressivamente um sistema capaz de simular a coleta, o armazenamento, o processamento e a análise de dados de engajamento do público com os conteúdos veiculados nas diversas plataformas da Globo. Nosso objetivo final é identificar padrões de consumo, destacar os conteúdos mais populares e traçar perfis de audiência.

Nesta primeira fase, nosso foco será na **leitura simulada, limpeza e análise inicial de dados de engajamento**. Utilizaremos os fundamentos da lógica de programação em Python que aprendemos neste módulo para manipular e preparar os dados para análises futuras. Para facilitar o início, forneceremos um arquivo base com dados simulados.

Este trabalho será desenvolvido em grupos, fomentando a colaboração e a troca de conhecimentos.

## 2\. Objetivos de Aprendizagem Específicos da Fase 1

Ao final desta fase, vocês deverão ser capazes de:

- Aplicar conceitos de manipulação de strings para processar dados textuais (nomes de conteúdo, comentários, etc.).
- Utilizar listas e dicionários de forma eficiente para armazenar e organizar os dados de interação coletados.
- Empregar estruturas de controle (condicionais `if/else` e laços `for/while`) para iterar e processar os conjuntos de dados.
- Desenvolver funções para modularizar o código, tornando-o mais organizado, legível e reutilizável.
- Implementar rotinas básicas de limpeza e transformação de dados a partir de dados já carregados em memória (ex: tratamento de valores ausentes, conversão de tipos).
- Calcular métricas descritivas simples a partir dos dados estruturados (ex: contagens, somas, médias).
- Praticar o tratamento básico de exceções (`try-except`) para tornar os scripts mais robustos a erros de processamento.

## 3\. Descrição Detalhada das Tarefas (Passo a Passo Sugerido)

A seguir, apresentamos um roteiro com as principais tarefas a serem desenvolvidas.

### 3.1. Entendimento dos Dados Iniciais

Será fornecido um arquivo de dados inicial chamado `interacoes_globo.csv`. Este arquivo contém dados simulados de interações de usuários com conteúdos da Globo.

**Estrutura dos Dados no arquivo `interacoes_globo.csv`:**

| Coluna                   | Tipo de Dado | Descrição / Exemplo                                                                                                                                                                                                                                                   |
| ------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id_conteudo`            | `int`        | Identificador único do conteúdo.                                                                                                                                                                                                                                      |
| `nome_conteudo`          | `string`     | Nome descritivo do conteúdo. Ex: 'Jornal Nacional - Edição de 20/10/2024', 'Capítulo 15 - Novela Renascer', 'Podcast Papo de Segunda - Tema Y', 'Compacto - Jogo do Brasileirão Série A: Flamengo vs Palmeiras', 'Receita de Bolo de Cenoura Cobertura de Chocolate'. |
| `id_usuario`             | `int`        | Identificador único do usuário.                                                                                                                                                                                                                                       |
| `timestamp_interacao`    | `string`     | Data e hora da interação no formato 'YYYY-MM-DD HH:MM:SS'.                                                                                                                                                                                                            |
| `plataforma`             | `string`     | Plataforma de origem da interação. Ex: 'Globoplay', 'G1', 'GE Globo', 'Premiere', 'Sportv Play', 'Receitas Gshow', 'App Cartola', 'TV Globo', 'Canal Brasil', 'Multishow', 'Viva', 'GNT Play'.                                                                        |
| `tipo_interacao`         | `string`     | Tipo de ação principal do usuário. Ex: 'view\_start' (início de visualização), 'like', 'share', 'comment'.                                                                                                                                                            |
| `watch_duration_seconds` | `int`        | Duração que o usuário assistiu ao conteúdo de vídeo em segundos. Pode ser nulo/vazio se `tipo_interacao` não for de consumo de vídeo ou se o conteúdo não for vídeo.                                                                                                  |
| `comment_text`           | `string`     | Texto do comentário, se o `tipo_interacao` for 'comment'. Pode ser nulo/vazio.                                                                                                                                                                                        |

**Ações Iniciais:**

1. Analisem a estrutura do arquivo `interacoes_globo.csv` fornecido.
2. **Opcional, mas recomendado para testes:** Os grupos podem, se desejarem, incrementar este arquivo com mais linhas de dados simulados. Ao fazer isso, mantenham o formato CSV e utilizem exemplos de plataformas, nomes de conteúdo e tipos de interação relevantes ao universo Globo. Isso ajudará a testar os scripts em cenários mais complexos e variados.
3. _Observação:_ O código para a leitura básica do arquivo CSV e carregamento inicial dos dados em uma estrutura Python (como uma lista de listas ou lista de dicionários) poderá ser disponibilizado pelo professor para que vocês possam focar na lógica de processamento.

### 3.2. Validação e Limpeza dos Dados

Após o carregamento inicial dos dados para a memória (por exemplo, em uma lista de dicionários, onde cada dicionário representa uma linha do CSV), desenvolvam funções em Python para realizar as seguintes tarefas de validação e limpeza:

- **Tratamento de `watch_duration_seconds`:**
  - Identificar valores ausentes ou vazios nesta coluna.
  - Se o `tipo_interacao` indicar consumo de vídeo (ex: 'view\_start' ou um tipo específico que denote visualização), converta valores ausentes/vazios de `watch_duration_seconds` para `0`.
  - Para `tipo_interacao` que claramente não envolvem duração de visualização (ex: 'like', 'share', 'comment'), o campo `watch_duration_seconds` deve ser tratado consistentemente. Decidam se ele será mantido como `None`, `0`, ou um valor que indique "não aplicável". Justifiquem a escolha.
  - Converter a coluna `watch_duration_seconds` para um tipo numérico adequado.
- **Limpeza de Campos de Texto:**
  - Remover espaços em branco desnecessários no início e no fim de campos de texto como `plataforma` e `tipo_interacao`.
- **Tratamento de Exceções:**
  - Implementar tratamento básico de exceções (blocos `try-except`) durante as conversões de tipo e outras operações de limpeza para evitar que o script pare abruptamente em caso de dados inesperados (ex: `ValueError` ao tentar converter um texto não numérico para `int`, `TypeError` ao operar com tipos incompatíveis).

### 3.3. Estruturação dos Dados

Após a limpeza, os dados processados devem ser armazenados em estruturas de dados Python que facilitem as consultas e cálculos de métricas. Algumas sugestões (vocês podem escolher uma delas ou propor uma alternativa, justificando a escolha):

- **Opção 1: Lista de Dicionários Otimizada:**
  - Manter uma lista principal, onde cada item é um dicionário representando uma interação. Cada dicionário deve ter as chaves correspondentes às colunas do CSV, mas com os dados já limpos e com os tipos corretos
- **Opção 2: Dicionário Agrupado por Conteúdo:**
  - Criar um dicionário principal onde as chaves são os `id_conteudo`.
  - Os valores associados a cada `id_conteudo` seriam outros dicionários contendo:
    - `nome_conteudo` (string)
    - Uma lista de todas as interações (`timestamp_interacao`, `id_usuario`, `plataforma`, `tipo_interacao`, `watch_duration_seconds`, `comment_text`) para aquele conteúdo, também como dicionários.

**Importante:** No relatório da Fase 1, os grupos deverão justificar a escolha da estrutura de dados principal utilizada para armazenar os dados processados, explicando por que ela foi considerada adequada para as tarefas desta fase.

### 3.4. Cálculo de Métricas Simples

Com os dados limpos e estruturados, desenvolvam funções que operem sobre essa estrutura para calcular as seguintes métricas de engajamento:

1. **Total de Interações por Conteúdo:**
   - Para cada `id_conteudo` (e seu respectivo `nome_conteudo`), calcular o número total de interações dos tipos 'like', 'share', 'comment'.
2. **Contagem por Tipo de Interação para Cada Conteúdo:**
   - Para cada `id_conteudo` (e `nome_conteudo`), contar quantas vezes cada `tipo_interacao` ocorreu (ex: Conteúdo X teve 50 'likes', 10 'shares', 5 'comments').
3. **Tempo Total de Visualização por Conteúdo:**
   - Para cada `id_conteudo` (e `nome_conteudo`), calcular a soma total de `watch_duration_seconds`.
4. **Média de Tempo de Visualização por Conteúdo:**
   - Para cada `id_conteudo` (e `nome_conteudo`), calcular a média de `watch_duration_seconds`. **Atenção:** Considerar apenas as interações onde `watch_duration_seconds` for maior que 0 para este cálculo.
5. **Listagem de Comentários por Conteúdo:**
   - Criar uma função que, dado um `id_conteudo`, retorne (ou imprima de forma organizada) todos os `comment_text` associados a ele.
6. **Listagem dos top-5 conteúdos com mais visualizações:**
   - Criar uma função que retorne (ou imprima de forma organizada) os top-5 conteúdos com mais visualizações.

### 3.5. Organização do Código

- O código Python deve ser bem organizado em funções lógicas e coesas. O arquivo base fornecido já traz sugestões de funções que ajudarão na solução. Por exemplo, vocês podem ter funções como:
  - `carregar_dados_csv(caminho_arquivo)`
  - `calcular_metricas_por_conteudo(dados_estruturados)`
  - `listar_comentarios_de_conteudo(id_conteudo_alvo, dados_estruturados)`
- Vocês podem usar quantas funções quiserem! Usem e abusem desse recurso para organizar melhor o código de vocês
- Utilizem comentários concisos para explicar as partes mais importantes do código, a lógica das funções e as decisões de implementação.
- Crie um script principal (ex: `main.py` ou `analise_fase1.py`) que orquestre a execução das diferentes etapas: carregamento, limpeza, estruturação e cálculo/exibição das métricas.

## 4\. Entregáveis Obrigatórios

Ao final desta fase, cada grupo deverá entregar:

1. **Scripts Python (`.py`):**
   - Um ou mais arquivos Python contendo todo o código desenvolvido para a leitura (se não fornecida), limpeza, estruturação e cálculo das métricas.
   - O código deve estar devidamente comentado.
2. **Arquivos de Dados (Opcional):**
   - Caso o grupo tenha incrementado o arquivo `interacoes_globo.csv` original com mais dados simulados, incluir esta versão modificada do arquivo.

## 5\. Especificações da Apresentação (para os grupos)

Haverá uma sessão de apresentação dos trabalhos.

- **Duração:** 10-15 minutos por grupo.
- **Formato:** Demonstração ao vivo do funcionamento do script, seguida de uma breve explicação oral.
- **Conteúdo da Apresentação:**
  1. **Demonstração da Execução:** Executar o script principal, mostrando o processamento dos dados (pode ser focado na etapa após a leitura inicial, se esta for fornecida) e a saída das métricas calculadas.
  2. **Explicação do Código:** Apresentar a estrutura geral do código, destacar as principais funções desenvolvidas e explicar como os dados são limpos e estruturados em memória (listas, dicionários).
  3. **Apresentação das Métricas:** Mostrar as métricas que foram calculadas e explicar brevemente como cada uma foi obtida a partir dos dados.
  4. **Desafios e Aprendizados:** Discutir brevemente os principais desafios enfrentados pelo grupo durante o desenvolvimento e os principais aprendizados da fase.
- **Participação:** Todos os membros do grupo devem participar ativamente da apresentação.

## 6\. Observação Adicional Importante

Lembrem-se que o **foco principal desta Fase 1 é a aplicação da lógica de programação e o uso de estruturas de dados fundamentais do Python (listas, dicionários, strings), juntamente com funções, estruturas de controle (laços e condicionais) e tratamento básico de exceções.**

**Nesta fase, NÃO é esperado (nem permitido, a menos que explicitamente instruído de outra forma) o uso de bibliotecas externas avançadas de análise de dados, como Pandas ou NumPy.** O objetivo é solidificar os conceitos básicos de programação em Python puro.

Certifiquem-se de que os exemplos de nomes de conteúdo, plataformas e tipos de interação que vocês utilizarem (especialmente se incrementarem os dados) sejam relevantes e façam sentido dentro do universo de produtos e serviços da Globo.

Boa sorte e bom trabalho!



## FEEDBACK

### Nota <mark>90</mark>

- Código está bastante direto
- Funções funcionam muito bem e estão bem organizadas
- Gostei dos prints estão muito bem organizados
