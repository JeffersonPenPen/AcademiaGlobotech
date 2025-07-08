# Projeto Unificado - Fase 3: Análise de Engajamento de Mídias Globo com Estruturas de Dados

**Objetivo principal**: Aplicar os princípios fundamentais de Algoritmos e Estruturas de Dados na análise de dados de engajamento de mídias, utilizando as estruturas de dados adequadas para otimizar o processamento e a recuperação de informações.

**Módulo Foco**: DS-PY-003 (Introdução a Algoritmos e Estruturas de Dados)

## 1. Contexto e Dados

O projeto continua a análise de dados de engajamento de mídias da Globo, com foco agora na aplicação de estruturas de dados e algoritmos eficientes. Você terá acesso a um arquivo `interacoes_globo.csv`, que contém dados brutos sobre interações de usuários com conteúdos em diferentes plataformas da Globo.

## 2. Estruturas de Dados Fundamentais e suas Operações

### 2.1. Processamento de Dados (Fila)

Ao invés de carregar os dados brutos do CSV diretamente para uma lista, utilize uma **Fila (Queue)** para processar as interações linha por linha. Isso simula um fluxo de dados contínuo e permite um processamento sequencial.

**Implementação**: Utilize uma estrutura de dados que se comporte como uma fila (FIFO - First-In, First-Out) para armazenar temporariamente cada linha do CSV após a leitura inicial.

**Operações**:

- `enfileirar(linha_csv)`: Adiciona uma linha lida do CSV à fila.
- `desenfileirar()`: Remove e retorna a próxima linha a ser processada da fila.
- Verificar se a fila está vazia.

### 2.2. Gerenciamento de Conteúdos e Usuários (Árvore de Busca Binária)

Para gerenciar os objetos `Conteudo` e `Usuario`, utilize **Árvores de Busca Binária (Binary Search Trees - BSTs)**. Isso permitirá uma busca, inserção e remoção mais eficiente em comparação com listas lineares, especialmente à medida que o número de conteúdos e usuários cresce.

#### 2.2.1. Árvore de Conteúdos

**Chave da BST**: `_id_conteudo` (inteiro)

**Operações**:

- `inserir_conteudo(conteudo)`: Adiciona um objeto `Conteudo` à árvore, utilizando o `_id_conteudo` como chave.
- `buscar_conteudo(id_conteudo)`: Retorna o objeto `Conteudo` correspondente ao `id_conteudo` fornecido, ou `None` se não encontrado.
- `remover_conteudo(id_conteudo)`: Remove o conteúdo da árvore.
- `percurso_em_ordem()`: Retorna uma lista de todos os conteúdos na árvore em ordem crescente de `_id_conteudo`.

#### 2.2.2. Árvore de Usuários

**Chave da BST**: `_id_usuario` (inteiro)

**Operações**:

- `inserir_usuario(usuario)`: Adiciona um objeto `Usuario` à árvore, utilizando o `_id_usuario` como chave.
- `buscar_usuario(id_usuario)`: Retorna o objeto `Usuario` correspondente ao `id_usuario` fornecido, ou `None` se não encontrado.
- `remover_usuario(id_usuario)`: Remove o usuário da árvore.
- `percurso_em_ordem()`: Retorna uma lista de todos os usuários na árvore em ordem crescente de `_id_usuario`.

## 3. Algoritmos de Análise e Ordenação

### 3.1. Classificação e Análise de Eficiência

Ao implementar as operações para as estruturas de dados (fila e árvores) e os algoritmos de análise, você deve analisar a **complexidade de tempo e espaço** de cada um, utilizando as notações Big-O, Big-Theta e Big-Ômega. Para cada método implementado, documente sua complexidade (ex: O(1), O(log n), O(n), O(n log n), O(n^2)).

### 3.2. Relatórios de Engajamento (Algoritmos de Ordenação)

Ao gerar relatórios de engajamento, utilize algoritmos de ordenação para apresentar os resultados de forma classificada.

**Top Conteúdos por Métrica**: Ao identificar os top N conteúdos por uma métrica específica (ex: `tempo_total_consumo`), implemente um dos seguintes algoritmos de ordenação para classificar os conteúdos antes de selecionar os N primeiros:

- **Quick Sort**: Para ordenação geral dos conteúdos com base na métrica desejada.
- **Insertion Sort**: Pode ser útil para ordenar pequenas listas de resultados intermediários ou para demonstrar a eficiência de algoritmos de ordenação para pequenas entradas.

**Critério de Ordenação**: A ordenação deve ser baseada nos valores calculados pelas métricas dos objetos `Conteudo` (ex: `calcular_total_interacoes_engajamento`, `calcular_tempo_total_consumo`).

## 4. Estrutura do Projeto

A estrutura de módulos e pacotes da Fase 1 será mantida, com as adaptações para as novas estruturas de dados e foco em algoritmos.

```javascript
projeto_engajamento_fase_3/
|--- init.py
|--- entidades/
|    |--- init.py
|    |--- plataforma.py (Classe Plataforma) 
|    |--- conteudo.py (Classes Conteudo, Video, Podcast, Artigo) 
|    |--- interacao.py (Classe Interacao) 
|    |--- usuario.py (Classe Usuario) 
|--- estruturas_dados/
|    |--- init.py 
|    |--- fila.py (Implementação da Fila) 
|    |--- arvore_binaria_busca.py (Implementação da Árvore de Busca Binária) 
|--- analise/
|    |--- init.py 
|    |--- sistema.py (Classe SistemaAnaliseEngajamento - Adaptada) 
|--- main.py 
|--- interacoes_globo.csv 
```

## 5. Implementação Detalhada

### 5.1. Classe `SistemaAnaliseEngajamento` (Adaptações)

Esta classe será o orquestrador principal e deverá utilizar as novas estruturas de dados.

**Atributos**:

- `_fila_interacoes_brutas`: Objeto da sua classe `Fila` para carregar as linhas do CSV.
- `_arvore_conteudos`: Objeto da sua classe `ArvoreBinariaBusca` para armazenar `Conteudos`.
- `_arvore_usuarios`: Objeto da sua classe `ArvoreBinariaBusca` para armazenar `Usuarios`.
- `_plataformas_registradas`: Mantenha como um dicionário para mapear `nome_plataforma` para objetos `Plataforma`, pois a busca por nome é mais natural e eficiente para um número menor de plataformas.

**Métodos de Carga e Processamento**:

- `_carregar_interacoes_csv(self, caminho_arquivo: str)`:
  - Lê o arquivo CSV.
  - Para cada linha, `enfileirar()` a linha bruta na `_fila_interacoes_brutas`.
- `processar_interacoes_da_fila(self)`:
  - Enquanto a `_fila_interacoes_brutas` não estiver vazia, `desenfileirar()` uma linha.
  - Para cada linha desenfileirada:
    - Obtém/Cria o objeto `Plataforma` (pode continuar usando o dicionário existente).
    - Obtém/Cria o objeto `Conteudo` (utilizando `buscar_conteudo` e `inserir_conteudo` da sua `_arvore_conteudos`).
    - Obtém/Cria o objeto `Usuario` (utilizando `buscar_usuario` e `inserir_usuario` da sua `_arvore_usuarios`).
    - Tenta instanciar `Interacao`, lidando com validações.
    - Se `Interacao` válida, registra-a nos objetos `Conteudo` e `Usuario` correspondentes.

**Métodos de Análise e Relatório**:

- `gerar_relatorio_engajamento_conteudos(self, top_n: int = None)`:
  - Obtém todos os conteúdos da `_arvore_conteudos` (via percurso em ordem).
  - Calcula as métricas de engajamento para cada `Conteudo`.
  - Aplique um algoritmo de ordenação (Quick Sort ou Insertion Sort) para classificar os conteúdos com base em uma métrica de engajamento (ex: total de interações, tempo total de consumo).
  - Exibe os `top_n` conteúdos.
- `gerar_relatorio_atividade_usuarios(self, top_n: int = None)`: Similar ao de conteúdos, mas para usuários.
- `identificar_top_conteudos(self, metrica: str, n: int)`: Este método deve encapsular a lógica de ordenação e seleção dos top N.

### 5.2. Classes de Entidade (Revisão)

As classes `Plataforma`, `Conteudo` (e suas subclasses), `Interacao`, e `Usuario` podem ser mantidas conforme a especificação da Fase 1. O foco aqui é como `SistemaAnaliseEngajamento` interage com elas usando as novas estruturas de dados.

## 6. Enunciado Detalhado para os Alunos (Resumo)

- **Desenvolver Estruturas de Dados**: Implemente as classes `Fila` e `ArvoreBinariaBusca` no sub-pacote `estruturas_dados/`, garantindo que as operações básicas (inserir, buscar, remover, percursos para a árvore; enfileirar, desenfileirar para a fila) estejam funcionais e eficientes.
- **Adaptar SistemaAnaliseEngajamento**: Modifique a classe `SistemaAnaliseEngajamento` para utilizar as novas estruturas de `Fila` para o carregamento inicial do CSV e `ArvoreBinariaBusca` para o gerenciamento de `Conteudo` e `Usuarios`.
- **Implementar Algoritmos de Ordenação**: No método de geração de relatórios de top conteúdos/usuários, aplique um dos algoritmos de ordenação estudados (Quick Sort ou Insertion Sort) para classificar os resultados.
- **Análise de Complexidade**: Para cada método que você implementar ou adaptar, determine e documente sua complexidade de tempo e espaço (notação Big-O).
- **Organização e Execução**: Mantenha a estrutura de pacotes e módulos sugerida. O `main.py` deve orquestrar o carregamento dos dados, o processamento via fila e árvores, e a geração dos relatórios.

## 7. Relatórios

Gerar e apresentar:

- Ranking de conteúdos mais consumidos (Liste os conteúdos ordenados pelo maior tempo total de consumo (`watch_duration_seconds`).
- Usuários com maior tempo total de consumo (Apresente os usuários ordenados pelo somatório do tempo de consumo em todas as suas interações).
- Plataforma com maior engajamento (Ordene as plataformas pela quantidade total de interações de engajamento (`like`, `share`, `comment`)).
- Conteúdos mais comentados (Liste os conteúdos com o maior número de interações do tipo 'comment').
- Total de interações por tipo de conteúdo (Liste os conteúdos com maior quantidade de interações).
- Tempo médio de consumo para cada tipo de plataforma.
- Quantidade de comentários registrados por conteúdo.

## 8. Apresentação

Além do código, a apresentação deverá abordar:

- Demonstração do funcionamento do sistema, enfatizando o uso da fila e das árvores de busca binária.
- Discussão sobre a escolha das estruturas de dados e como elas impactam a eficiência das operações (busca, inserção, processamento).
- Análise da complexidade dos algoritmos implementados (tempo e espaço).
- Desafios enfrentados e aprendizados com a aplicação dos conceitos de Algoritmos e Estruturas de Dados.

## 9. Avaliação

A nota será composta pelos seguintes critérios:

| Critério                                  | Peso |
| ----------------------------------------- | ---- |
| Correção e funcionamento do código        | 3.0  |
| Uso correto de estruturas de dados        | 2.0  |
| Implementação de algoritmos de ordenação  | 1.0  |
| Implementação de algoritmos de busca      | 1.0  |
| Clareza e organização do código           | 1.0  |
| Documentação e justificativas             | 1.0  |
| Relatórios e interpretação dos resultados | 1.0  |
