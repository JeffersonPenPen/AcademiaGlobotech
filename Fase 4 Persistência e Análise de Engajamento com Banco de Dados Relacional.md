# **Projeto Unificado - Fase 4: Persistência e Análise de Engajamento com Banco de Dados Relacional**

**Objetivo principal**: Trabalhar com um sistema de análise de dados, mas agora usando um banco de dados relacional persistente. O projeto aplicará os conceitos de modelagem de dados, criação de esquemas com SQL (DDL), e manipulação e consulta de dados (DML e DQL) para tornar a solução mais robusta, escalável e alinhada com as práticas de mercado.

**Módulo Foco**: Banco de Dados

## **1. Contexto e Dados**

Nas fases anteriores, construímos um sistema de análise de engajamento que processava dados de um arquivo CSV e os mantinha em memória utilizando objetos e estruturas de dados como listas e dicionários. Embora funcional para um volume de dados limitado, essa abordagem não é persistente nem escalável.

Nesta fase, daremos um passo fundamental:preparar o armazenamento dos dados para um banco de dados relacional (MySQL). Isso significa que as informações sobre conteúdos, usuários, plataformas e suas interações não serão mais perdidas ao final da execução do script, e as análises serão feitas através de consultas SQL.

## **2. Modelagem e Criação do Banco de Dados (DDL)**

O primeiro passo é traduzir a estrutura de classes da Fase 2 para um esquema de banco de dados relacional.

### **2.1. Modelagem Relacional (MER e DER)**

Baseando-se nas classes Conteudo, Usuario, Plataforma e Interacao, seu grupo deverá projetar o banco de dados.

**Operações**:

- **Desenhar o Modelo Entidade-Relacionamento (MER)**: Identifique as entidades principais, seus atributos e os relacionamentos entre elas.
- **Definir Cardinalidade**: Especifique como as entidades se relacionam (1:1, 1:N, N:N). Por exemplo, um Usuario pode ter muitas Interacoes.
- **Mapear para o Modelo Lógico (DER)**: Converta o MER em um diagrama de tabelas, definindo as colunas, tipos de dados SQL (INTEGER, VARCHAR, TIMESTAMP, etc.), chaves primárias (PK) e chaves estrangeiras (FK).

### **2.2. Script de Criação do Banco (schema.sql)**

Com o modelo lógico definido, o próximo passo é escrevê-lo em SQL.

**Operações**:

- Crie um arquivo schema.sql.
- Crie o banco de dados “globo_tech”.
- Neste banco, escreva os comandos CREATE TABLE para criar cada uma das tabelas do seu modelo.
- Defina as PRIMARY KEY e FOREIGN KEY para estabelecer os relacionamentos e a integridade referencial.
- Utilize outras CONSTRAINTS importantes, como NOT NULL e UNIQUE, onde for aplicável (ex: o e-mail de um usuário pode ser único).

## **3. Carga de Dados e Análise com SQL (DML e DQL)**

Com o banco de dados estruturado, o foco se volta para a interação entre a aplicação Python e o banco.

Faça a carga dos dados no banco de dados, utilizando comandos como INSERT INTO ou COPY para inserir os dados nas tabelas correspondentes.

## **4. Relatórios**

Encontrar queries que tragam algumas das análises dos módulos anteriores, mas agora obtidos através de consultas SQL:

- Ranking de conteúdos mais consumidos (ordenados por tempo total de consumo).
- Plataforma com maior engajamento (total de interações like, share, comment).
- Conteúdos mais comentados.
