import csv
from collections import defaultdict

# NOME DO ARQUIVO CSV ESPERADO NO MESMO DIRETÓRIO DO SCRIPT
NOME_ARQUIVO_CSV = "interacoes_globo.csv"

def carregar_dados_de_arquivo_csv(nome_arquivo):
    """
    Carrega os dados de um arquivo CSV para uma lista de listas.
    A primeira lista retornada é o cabeçalho, e as subsequentes são as linhas de dados.
    Retorna None se o arquivo não for encontrado ou ocorrer um erro.
    """
    dados_com_cabecalho = []
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            # Adiciona todas as linhas (incluindo o cabeçalho) à lista
            for linha in leitor_csv:
                dados_com_cabecalho.append(linha)
              
       
        if not dados_com_cabecalho:
            print(f"Aviso: O arquivo CSV '{nome_arquivo}' está vazio.")
            return None
        return dados_com_cabecalho
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado. Certifique-se de que ele está na mesma pasta do script.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV '{nome_arquivo}': {e}")
        return None

def converter_lista_para_lista_de_dicionarios(dados_em_lista_com_cabecalho):
    lista_de_dicionarios = [
        dict(zip(dados_em_lista_com_cabecalho[0], linha)) for linha in dados_em_lista_com_cabecalho[1:]
    ] # Os dicionários são criados a partir da função zip que relaciona os índices da lista 0 com os índices relacionados das demais listas [1:]
    return lista_de_dicionarios


def tratar_campos_inteiros(interacao_bruta, interacao_limpa):
    try:
        interacao_limpa["id_conteudo"] = int(interacao_bruta.get("id_conteudo", 0)) # .get recebe o valor da chave "id_conteudo" e transforma em inteiro.
    except (TypeError, ValueError):
        interacao_limpa["id_conteudo"] = 0 # Caso não seja possível transformar em inteiro, atribui valor 0.

    try:
        interacao_limpa["id_usuario"] = int(interacao_bruta.get("id_usuario", 0)) # .get recebe o valor da chave "id_usuario" e transforma em inteiro.
    except (TypeError, ValueError):
        interacao_limpa["id_usuario"] = 0 # Caso não seja possível transformar em inteiro, atribui valor 0.

    return interacao_limpa
    

def tratar_watch_duration_seconds(interacao_bruta, interacao_limpa):
    try:
        interacao_limpa["watch_duration_seconds"] = int(interacao_bruta.get("watch_duration_seconds", 0))
    except (TypeError, ValueError):
        interacao_limpa["watch_duration_seconds"] = 0
    return interacao_limpa

def seconds_to_HHmmss(seconds):
    HH = seconds // 3600
    mm = (seconds % 3600) // 60
    ss = seconds % 60
    hours_min = (f"{HH}:{mm:02d}:{ss:02d}")
    return hours_min

def tratar_campos_texto(interacao_bruta, interacao_limpa):
    try:
        interacao_limpa["nome_conteudo"] = str(interacao_bruta.get("nome_conteudo", "")).strip()
    except (TypeError, ValueError):
        interacao_limpa["nome_conteudo"] = ""

    try:
        interacao_limpa["plataforma"] = str(interacao_bruta.get("plataforma", "")).strip()
    except (TypeError, ValueError):
        interacao_limpa["plataforma"] = ""

    try:
        interacao_limpa["tipo_interacao"] = str(interacao_bruta.get("tipo_interacao", "")).strip()
    except (TypeError, ValueError):
        interacao_limpa["tipo_interacao"] = ""

    try:
        comentario = str(interacao_bruta.get("comment_text", ""))
        interacao_limpa["comment_text"] = " ".join(comentario.split())
    except (TypeError, ValueError):
        interacao_limpa["comment_text"] = ""

    return interacao_limpa


def limpar_e_transformar_dados(lista_interacoes_brutas_dict):
    """
    Limpa e transforma os dados brutos das interações (lista de dicionários).
    Converte tipos de dados, trata valores ausentes e remove espaços.
    essa função deve usar as 3 funcoes acima
    Retorna a lista de interações limpas (também como lista de dicionários).
    """
    interacoes_limpas = []
    # Espera uma lista de dicionários aqui
    for interacao_bruta in lista_interacoes_brutas_dict:
    
        interacao_limpa = {}
        interacao_limpa = tratar_campos_inteiros(interacao_bruta, interacao_limpa)
        interacao_limpa = tratar_watch_duration_seconds(interacao_bruta, interacao_limpa)
        interacao_limpa = tratar_campos_texto(interacao_bruta, interacao_limpa)
        interacoes_limpas.append(interacao_limpa) # Chama as funcões anteriores que tratam os dados e adiciona com append cada interacao_limpa à lista alteracoes_limpas, formando uma nova lista de dicionários.
            
    return interacoes_limpas

def criar_mapa_conteudos(interacoes_limpas):
    """
    Cria um dicionário que mapeia id_conteudo para nome_conteudo.
    """
    mapa = {}
    for interacao in interacoes_limpas:
        mapa[interacao["id_conteudo"]] = interacao.get("nome_conteudo", "")
    return mapa

def calcular_metricas_por_conteudo(interacoes_limpas, mapa_conteudos):
    """
    Calcula várias métricas de engajamento agrupadas por conteúdo.
    Aqui você deve varrer as interações limpas e calcular as métricas desejadas.
    Recomenda-se utilizar um loop e verificar se o conteudo ja foi incluido pelo nome ou id_conteudo
    Retorna um dicionário com as métricas calculadas.
    """
    metricas_conteudo = defaultdict(lambda: {
        'nome_conteudo': '',
        'total_interacoes_engajamento': 0, # like, share, comment, vote_bbb
        'contagem_por_tipo_interacao': defaultdict(int),
        'tempo_total_visualizacao': 0,
        'soma_watch_duration_para_media': 0,
        'contagem_watch_duration_para_media': 0,
        'media_tempo_visualizacao': 0.0,
        'comentarios': []
    })

    tipos_engajamento = {'like', 'share', 'comment', 'vote_bbb'}

    for interacao in interacoes_limpas:
        id_c = interacao["id_conteudo"]
        metricas_c = metricas_conteudo[id_c]

        if not metricas_c["nome_conteudo"]: # Preenche o nome do conteúdo uma vez
            metricas_c["nome_conteudo"] = mapa_conteudos.get(id_c, "Desconhecido")

        # Métrica 1: Total de interações de engajamento
        if interacao["tipo_interacao"] in tipos_engajamento:
            metricas_c["total_interacoes_engajamento"] += 1

        # Métrica 2: Contagem de cada tipo_interacao
        metricas_c["contagem_por_tipo_interacao"][interacao["tipo_interacao"]] += 1

        # Métrica 3: Tempo total de watch_duration_seconds
        metricas_c["tempo_total_visualizacao"] += interacao["watch_duration_seconds"]
        
        # Métrica 4: Média de watch_duration_seconds (considerar apenas watch_duration_seconds > 0)
        if interacao["watch_duration_seconds"] > 0:
            metricas_c["soma_watch_duration_para_media"] += interacao["watch_duration_seconds"]
            metricas_c["contagem_watch_duration_para_media"] += 1

        # Métrica 5: Listar todos os comentários
        if interacao["tipo_interacao"] == 'comment' and interacao["comment_text"]:
            metricas_c["comentarios"].append(interacao["comment_text"])

    # Calcular média de visualização final
    for id_c in metricas_conteudo:
        metricas_c = metricas_conteudo[id_c]
        if metricas_c["contagem_watch_duration_para_media"] > 0:
            metricas_c["media_tempo_visualizacao"] = round(
                metricas_c["soma_watch_duration_para_media"] / metricas_c["contagem_watch_duration_para_media"], 2
            )
        # Remover campos auxiliares
        if 'soma_watch_duration_para_media' in metricas_c:
            del metricas_c["soma_watch_duration_para_media"]
        if 'contagem_watch_duration_para_media' in metricas_c:
            del metricas_c["contagem_watch_duration_para_media"]
            
    return dict(metricas_conteudo) # Converter de volta para dict normal para exibição


def main():
    """
    Função principal para orquestrar a análise.
    """
    print("Iniciando Fase 1: Coleta e Estruturação Inicial de Dados de Engajamento Globo\n")

    # 1. Carregar dados do arquivo CSV para uma lista de listas
    dados_brutos_lista_de_listas = carregar_dados_de_arquivo_csv(NOME_ARQUIVO_CSV)
    
    if dados_brutos_lista_de_listas is None:
        print(f"Não foi possível carregar os dados do arquivo '{NOME_ARQUIVO_CSV}'. Encerrando.")
        return
    
    if len(dados_brutos_lista_de_listas) < 2: # Precisa de cabeçalho + pelo menos uma linha de dados
        print(f"O arquivo '{NOME_ARQUIVO_CSV}' não contém dados suficientes (cabeçalho e linhas de dados). Encerrando.")
        return

    print(f"Total de {len(dados_brutos_lista_de_listas) - 1} linhas de dados (mais cabeçalho) carregadas do CSV.\n")

    # ETAPA PARA OS ALUNOS: Converter a lista de listas para uma lista de dicionários
    # Esta etapa é crucial para que as funções subsequentes funcionem como esperado.
    interacoes_brutas_dict = converter_lista_para_lista_de_dicionarios(dados_brutos_lista_de_listas)
    
    
    # 2. Limpar e transformar dados (agora a partir da lista de dicionários)
    interacoes_limpas = limpar_e_transformar_dados(interacoes_brutas_dict)
    
    
    # 3. Criar mapa de conteúdos (id_conteudo -> nome_conteudo)
    mapa_conteudos = criar_mapa_conteudos(interacoes_limpas)
 

    # 4. Calcular métricas por conteúdo
    metricas = calcular_metricas_por_conteudo(interacoes_limpas, mapa_conteudos)

   
    # 5. Exibir resultados
    print("RESULTADOS:")
    for id_c in metricas:
        m = metricas[id_c]
        hours_min = seconds_to_HHmmss(m['tempo_total_visualizacao'])
        hours_media = seconds_to_HHmmss(int(m["media_tempo_visualizacao"]))
        total_inter = sum(m['contagem_por_tipo_interacao'].values())
        comentarios = m["comentarios"]
        print(f"ID: {id_c} - {m['nome_conteudo']}")
        print(f"Total de interações: {total_inter}")
        print("Interações por tipo:")
        for tipo, count in dict(m['contagem_por_tipo_interacao']).items():
            print(f"             {tipo}: {count}")
        print(f"Tempo total assistido: {m['tempo_total_visualizacao']} segundos ou {hours_min}")
        print(f"Média de tempo assistido: {m['media_tempo_visualizacao']} segundos ou {hours_media}")
        print(f"Quantidade de comentários: {len(m['comentarios'])}")
        for contador, i in enumerate(comentarios, 1):
            print(f"Comentário {contador}: {i}")
        print(f"\n")
    print("TOP 5 MAIS ASSISTIDOS:")
    tempos = [(id_c, m['tempo_total_visualizacao']) for id_c, m in metricas.items()]
    tempos.sort(key=lambda x: x[1], reverse=True)

    for i in range(5):
        id_c = tempos[i][0]
        print(metricas[id_c]['nome_conteudo'])

if __name__ == "__main__":
    main()
