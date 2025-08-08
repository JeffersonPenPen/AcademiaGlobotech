CREATE SCHEMA globo_tech;

CREATE TABLE globo_tech.usuarios (
		id_usuario SMALLINT PRIMARY KEY
        );
        
CREATE TABLE globo_tech.plataforma (
	id_plataforma TINYINT AUTO_INCREMENT PRIMARY KEY
    ,nome_plataforma VARCHAR(35)
    );

CREATE TABLE globo_tech.tipo_conteudo (
	id_tipo_conteudo TINYINT AUTO_INCREMENT PRIMARY KEY
    ,nome_tipo_conteudo VARCHAR(10)
    );

CREATE TABLE globo_tech.conteudo (
	id_conteudo TINYINT AUTO_INCREMENT PRIMARY KEY
    ,nome_conteudo VARCHAR(30) UNIQUE KEY
    ,id_tipo_conteudo TINYINT
    ,FOREIGN KEY (id_tipo_conteudo) REFERENCES globo_tech.tipo_conteudo(id_tipo_conteudo)
    );

CREATE TABLE globo_tech.tipo_interacao (
	id_tipo_interacao TINYINT AUTO_INCREMENT PRIMARY KEY
    ,nome_tipo_interacao VARCHAR(10)
    );

CREATE TABLE globo_tech.interacao (
	id_interacao SMALLINT AUTO_INCREMENT PRIMARY KEY
    ,id_conteudo TINYINT NOT NULL
    ,id_usuario SMALLINT NOT NULL
    ,timestamp_interacao DATETIME NOT NULL
    ,id_plataforma TINYINT NOT NULL
    ,id_tipo_interacao TINYINT NOT NULL
    ,watch_duration_seconds INT
    ,comment_text TEXT
    );

INSERT
	INTO globo_tech.tipo_interacao (
		nome_tipo_interacao
        )
	VALUES (
		"view_start")
        ,("like")
        ,("share")
        ,("comment"
    );
        
INSERT
	INTO globo_tech.tipo_conteudo (
		nome_tipo_conteudo
        )
	VALUES (
		"video")
        ,("podcast")
        ,("artigo"
        );

-- Executar Aplicação Python

-- QUERIES
USE globo_tech;

-- DEBUG
SELECT * FROM usuarios;
SELECT * FROM conteudo;
SELECT * FROM plataforma;
SELECT * FROM interacao;

-- RELATÓRIOS
-- 1. Ranking de conteúdos mais consumidos (ordenados por tempo total de consumo)
SELECT
    c.nome_conteudo AS Conteudo,
    SUM(i.watch_duration_seconds) AS "Consumo Total"
FROM globo_tech.interacao AS i
INNER JOIN globo_tech.conteudo AS c
ON i.id_conteudo = c.id_conteudo
GROUP BY c.nome_conteudo
ORDER BY SUM(i.watch_duration_seconds) DESC;

-- 2. Plataforma com maior engajamento (total de interações like, share, comment)
SELECT
    p.nome_plataforma AS Plataforma,
    COUNT(i.id_interacao) AS "Engajamento Total"
FROM globo_tech.interacao AS i
INNER JOIN globo_tech.plataforma AS p
ON i.id_plataforma = p.id_plataforma
INNER JOIN globo_tech.tipo_interacao AS ti
ON i.id_tipo_interacao = ti.id_tipo_interacao
WHERE ti.nome_tipo_interacao IN ("like", "share", "comment")
GROUP BY p.nome_plataforma
ORDER BY COUNT(i.id_interacao) DESC;

-- 3. Conteúdos mais comentados
SELECT
    c.nome_conteudo AS Conteudo,
    COUNT(i.comment_text) AS "Quantidade de Comentários"
FROM globo_tech.interacao AS i
INNER JOIN globo_tech.conteudo AS c
ON i.id_conteudo = c.id_conteudo
WHERE i.comment_text IS NOT NULL
GROUP BY c.nome_conteudo
ORDER BY COUNT(i.comment_text) DESC;

-- 4. Comentários por Conteúdo
SELECT
    c.nome_conteudo AS Conteudo,
    i.comment_text AS Comentario
FROM ta_na_Globo_40.interacao AS i
INNER JOIN ta_na_Globo_40.conteudo AS c
ON i.id_conteudo = c.id_conteudo
WHERE i.comment_text IS NOT NULL
ORDER BY c.nome_conteudo;

-- 5. Conteúdos Mais Interagidos
SELECT
    c.nome_conteudo AS Conteudo,
    COUNT(i.id_interacao) AS Total_de_Interacoes
FROM ta_na_Globo_40.interacao AS i
INNER JOIN ta_na_Globo_40.conteudo AS c
ON i.id_conteudo = c.id_conteudo
GROUP BY c.nome_conteudo
ORDER BY Total_de_Interacoes DESC;

-- 6. Engajamento por Plataforma
SELECT
    p.nome_plataforma AS Plataforma,
    COUNT(i.id_interacao) AS "Total de Interações"
FROM ta_na_Globo_40.interacao AS i
INNER JOIN ta_na_Globo_40.plataforma AS p
ON i.id_plataforma = p.id_plataforma
GROUP BY p.nome_plataforma
ORDER BY COUNT(i.id_interacao) DESC;

-- 7. Tempo Médio por Plataforma
SELECT p.nome_plataforma AS Plataforma,
    AVG(i.watch_duration_seconds) AS "Tempo Médio (s)"
FROM ta_na_Globo_40.interacao AS i
INNER JOIN ta_na_Globo_40.plataforma AS p
ON i.id_plataforma = p.id_plataforma
GROUP BY p.nome_plataforma
ORDER BY AVG(i.watch_duration_seconds) DESC;

-- 8. Total de Interações por Tipo
SELECT
    ti.nome_tipo_interacao AS "Tipo de Interação",
    COUNT(i.id_interacao) AS "Total"
FROM ta_na_Globo_40.interacao AS i
INNER JOIN ta_na_Globo_40.tipo_interacao AS ti
ON i.id_tipo_interacao = ti.id_tipo_interacao
GROUP BY ti.nome_tipo_interacao
ORDER BY Total DESC;

-- 9. Usuários Mais Engajados
SELECT
    i.id_usuario AS ID_Usuario,
    COUNT(i.id_interacao) AS "Total de Interações por Usuário"
FROM ta_na_Globo_40.interacao AS i
GROUP BY i.id_usuario
ORDER BY COUNT(i.id_interacao) DESC;