import mysql.connector
import os
import csv

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jj008926",
    database="globo_tech"
)

cursor = con.cursor()
caminho_arquivo = "data/interacoes_globo.csv"

def carregar_interacoes_csv(caminho_arquivo):
    #Nova função criada para tratar célula de comentário com vírgula
    lista = []
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as dados_csv:
            linhas = dados_csv.readlines()
            for linha in linhas[1:]: #Ignora cabeçalho
                #rstrip() quebra as linhas e split(",", 8) separa em nove colunas
				#usando as oito primeiras vírgulas de cada linha.
                #Isso protege o conteúdo da coluna "comment_text"
                linha_colunas = linha.rstrip("\n").split(",", 7)
                
                if len(linha_colunas) == 8:
                    lista.append(linha_colunas)
                else:
                    print(f"Aviso: Linha com formato incorreto. Dados podem estar incompletos: {linha_colunas}")
                    lista.append(linha_colunas)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao carregar CSV: {e}")
    return lista
    
lista = carregar_interacoes_csv("data/interacoes_globo.csv")

lista_valores_interacao=[]
lista_valores_plataforma=[]
lista_valores_conteudo=[]
interacoes_unicas=[]

usuarios_unicos = set()
for linha in lista:
    id_usuario = linha[2]
    usuarios_unicos.add(id_usuario)

plataformas_unicas = set()
for linha in lista:
    plataforma = linha[4]
    plataformas_unicas.add(plataforma)

lista_valores_plataforma = [(p,) for p in plataformas_unicas]
lista_valores_id_usuario = [(p,) for p in usuarios_unicos]

sql_plataforma = "INSERT IGNORE INTO usuarios(id_usuario) VALUES(%s)"
cursor.executemany(sql_plataforma, lista_valores_id_usuario)
con.commit()

sql_plataforma = "INSERT IGNORE INTO plataforma(nome_plataforma) VALUES(%s)"
cursor.executemany(sql_plataforma, lista_valores_plataforma)
con.commit()

for linha in lista:
    id_conteudo = linha[0]
    nome_conteudo = linha[1]
    id_usuario = linha[2]
    timestamp_interacao = linha[3]
    plataforma = linha[4]
    tipo_interacao = linha[5]
    seconds = linha[6]
    comments = linha[7]

    print(f"Processando linha: {linha}")

    #Tratamento de Valores Vazios
    if seconds == "":
        watch_duration_seconds = None
    else:
        watch_duration_seconds = seconds

    if comments == "":
            comment_text = None
    else:
        comment_text = comments


    #Tabela Conteúdo
    valores_conteudo = (id_conteudo, nome_conteudo)
    lista_valores_conteudo.append(valores_conteudo)

    cursor.execute(
        "SELECT id_plataforma FROM globo_tech.plataforma WHERE nome_plataforma = %s", (plataforma,)
        ) 
    resultado_plataforma = cursor.fetchone()
    cursor.fetchall()
    if resultado_plataforma:
        id_plataforma = resultado_plataforma[0]
    else:
        print(f"[ERRO] Plataforma '{plataforma}' não encontrada.")
        continue

    cursor.execute(
        "SELECT id_tipo_interacao FROM globo_tech.tipo_interacao WHERE nome_tipo_interacao = %s", (tipo_interacao,)
        )
    resultado_tipo_interacao = cursor.fetchone()
    cursor.fetchall()
    if resultado_tipo_interacao:
        id_tipo_interacao = resultado_tipo_interacao[0]
    else:
        print(f"[ERRO] Tipo de Interação '{tipo_interacao}' não encontrada.")
        continue

    #Tabela Interação
    valores_interacao = (
        id_conteudo
        ,id_usuario
        ,timestamp_interacao
        ,id_plataforma
        ,id_tipo_interacao
        ,watch_duration_seconds
        ,comment_text
        )
    interacoes_unicas.append(valores_interacao)

    print(f"Número final de interações a serem inseridas: {len(interacoes_unicas)}")

lista_valores_interacao = interacoes_unicas

#Tabela Conteudo
sql_conteudo = "INSERT IGNORE INTO conteudo(id_conteudo, nome_conteudo) VALUES(%s, %s)"
cursor.executemany(sql_conteudo, lista_valores_conteudo)

#Tabela Interação
sql_interacao = """
    INSERT INTO interacao(
            id_conteudo
            ,id_usuario
            ,timestamp_interacao
            ,id_plataforma
            ,id_tipo_interacao
            ,watch_duration_seconds
            ,comment_text
            )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
cursor.executemany(sql_interacao, lista_valores_interacao)

con.commit()
cursor.close()
con.close()