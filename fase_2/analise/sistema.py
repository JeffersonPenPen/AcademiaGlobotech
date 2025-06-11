import csv #Bilioteca interna para tratar csv
from entidades.usuario import Usuario #Recebe Classes e Funções de usuario.py
from entidades.plataforma import Plataforma #Recebe Classes e Funções de plataforma.py
from entidades.conteudo import Video, Podcast, Artigo #Recebe Classes e Funções de conteudo.py
from entidades.interacao import Interacao #Recebe Classes e Funções de interacao.py

"""
Como a Fase 2 é uma reformulação do código da Fase 1,
foi mantido a formatação dos outputs sempre que possível,
além de algumas outras padronizações.
"""

class SistemaAnaliseEngajamento:
#Classe que recebe os dados das entidades, organiza e analisa os dados
    VERSAO_ANALISE = "2.0"

    def __init__(self):
        # Atributos privados
        self.__plataformas_registradas = {}
        self.__conteudos_registrados = {}
        self.__usuarios_registrados = {}
        self.__proximo_id_plataforma = 1 # Contador para gerar IDs para plataformas

    def cadastrar_plataforma(self, nome_plataforma):
        #Cadastra uma nova plataforma se ela ainda não estiver registrada.
        if nome_plataforma not in self.__plataformas_registradas:
            nova = Plataforma(nome_plataforma, self.__proximo_id_plataforma)
            self.__plataformas_registradas[nome_plataforma] = nova
            self.__proximo_id_plataforma += 1
        return self.__plataformas_registradas[nome_plataforma]

    def obter_plataforma(self, nome_plataforma):
        #Carrega uma plataforma existente ou a cadastra se não existir.
        return self.__plataformas_registradas.get(nome_plataforma, self.cadastrar_plataforma(nome_plataforma))

    def listar_plataformas(self):
        #Retorna plataformas registradas.
        return list(self.__plataformas_registradas.values())

    def _carregar_interacoes_csv(self, caminho_arquivo):
    #Carrega os dados do csv como dicionários.
        lista = []
        try:
            with open(caminho_arquivo, mode='r', encoding='utf-8') as csvfile:
                leitor = csv.DictReader(csvfile)
                for linha in leitor:
                    lista.append(linha)
        except FileNotFoundError:
            print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
            return [] #Evita interrupção do código, retornando lista vazia.
        except Exception as e:
            print(f"Erro ao carregar CSV: {e}")
            return [] #Evita interrupção do código, retornando lista vazia.
        return lista

    
    def processar_interacoes_do_csv(self, caminho_arquivo):
    #Classe que processa os dicionários oriundos dos dados do csv
        linhas = self._carregar_interacoes_csv(caminho_arquivo)
        if not linhas:
            print("Nenhuma linha para processar ou erro ao carregar o CSV.")
            return

        for linha in linhas: 
            try:
                # Extrair dados da linha do CSV
                id_usuario = int(linha['id_usuario'])
                id_conteudo = int(linha['id_conteudo'])
                nome_conteudo = linha['nome_conteudo']
                timestamp = linha['timestamp_interacao']
                tipo = linha['tipo_interacao']

                valor_duracao = linha['watch_duration_seconds']
                
                #Caso 'watch_duration_seconds' seja vazio ou não numérico
                if not str(valor_duracao).strip().isdigit(): #Se o valor do csv sem espaços não for inteiro e positivo
                    duracao = 0
                else:
                    duracao = int(valor_duracao)
                    if duracao < 0:
                        duracao = 0

                
                comentario = linha['comment_text']
                nome_plataforma = linha['plataforma']

                # Carrega ou cadastra a plataforma
                plataforma = self.obter_plataforma(nome_plataforma)

                tipo_conteudo = None #Placeholder para futura coluna no csv com tipo de conteúdo
                
                # Carrega ou cadastra o conteúdo consumido.
                if id_conteudo not in self.__conteudos_registrados:
                    if tipo_conteudo == "podcast":
                        conteudo = Podcast(id_conteudo, nome_conteudo, 0)
                    elif tipo_conteudo == "artigo":
                        conteudo = Artigo(id_conteudo, nome_conteudo, 0)
                    else:
                        conteudo = Video(id_conteudo, nome_conteudo, 0)

                    self.__conteudos_registrados[id_conteudo] = conteudo
                else:
                    conteudo = self.__conteudos_registrados[id_conteudo]

                # Carrega ou cadastra o usuário
                if id_usuario not in self.__usuarios_registrados:
                    usuario = Usuario(id_usuario)
                    self.__usuarios_registrados[id_usuario] = usuario
                else:
                    usuario = self.__usuarios_registrados[id_usuario]

                # Cadastra Interacao e relaciona ao Conteudo e Usuario
                interacao = Interacao(id_usuario, timestamp, tipo, duracao, comentario, conteudo, plataforma)
                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao) # Chamada para o novo método registrar_interacao
                
            except ValueError as ve:
                print(f"Erro de valor ao processar linha: {linha} - {ve}")
            except KeyError as ke:
                print(f"Erro: Coluna '{ke}' não encontrada no CSV na linha: {linha}")
            except Exception as e:
                print(f"Erro inesperado ao processar interação na linha {linha}: {e}")
        

    def gerar_relatorio_engajamento_conteudos(self, top_n=None):
    #Relatório de Engajamento por Conteúdo ou com maior quantidade de interações
        if not self.__conteudos_registrados:
            print("Nenhum conteúdo registrado para gerar relatório.")
            return

        print("\n-> -> RESULTADOS DE ENGAJAMENTO DE CONTEÚDOS <- <-\n")
        
        conteudos_para_relatorio = list(self.__conteudos_registrados.values())
        if top_n:
            # Ordena Conteúdo por total de Interações
            conteudos_para_relatorio = sorted(conteudos_para_relatorio, 
                                            key=lambda c: c.calcular_total_interacoes_engajamento(), 
                                            reverse=True)
            conteudos_para_relatorio = conteudos_para_relatorio[:top_n]


        for conteudo in conteudos_para_relatorio:
            print(f"ID: {conteudo.id_conteudo} - {conteudo.nome_conteudo}")
            print(f"Total de interações: {conteudo.calcular_total_interacoes_engajamento()}")
            
            contagem_tipos = conteudo.calcular_contagem_por_tipo_interacao()
            if contagem_tipos:
                print("Interações por tipo:")
                for tipo, qtd in contagem_tipos.items():
                    print(f"             {tipo}: {qtd}") #Identação Artificial estética, seguindo formatação da Fase 1

            tempo_total = conteudo.calcular_tempo_total_consumo()
            if tempo_total > 0:
                tempo_medio = conteudo.calcular_media_tempo_consumo()
                print(f"Tempo total assistido: {tempo_total} segundos ou {self.converter_segundos(tempo_total)}")
                print(f"Média de tempo assistido: {tempo_medio:.2f} segundos")
                """
                Tempo mostrado também no formato HH:MM:SS para facilitar ao usuário,
                seguindo o que foi feito na Fase 1
                """

            comentarios = conteudo.listar_comentarios()
            if comentarios:
                print(f"Quantidade de comentários: {len(comentarios)}")
                for idx, c in enumerate(comentarios):
                    print(f"Comentário {idx+1}: {c}")

            print("\n\n") 

    
    def gerar_relatorio_atividade_usuarios(self):
    #Relatório com todas as atividades de cada usuário
        if not self.__usuarios_registrados:
            print("Nenhum usuário registrado para gerar relatório.")
            return

        print("\n-> -> RESULTADOS DE ATIVIDADE DE USUÁRIOS <- <-\n")
        for usuario in self.__usuarios_registrados.values():

            print(f"Usuário (ID): {usuario.id_usuario}")
            
            #Número de Interações (total de interações, não apenas engajamento)
            #Agora acessando a property interacoes_realizadas
            print(f"Número de Interações: {len(usuario.interacoes_realizadas)}") 
            
            #Contagem por tipo de interação
            contagem = usuario.calcular_contagem_por_tipo_interacao()
            if contagem:
                print("Contagem por tipo de interação:")
                for tipo, qtd in contagem.items():
                    print(f"             {tipo}: {qtd}") 

            #Tempo total e médio de consumo (apenas se houver consumo)
            total_consumo = usuario.calcular_tempo_total_consumo()
            if total_consumo > 0: 
                media_consumo = usuario.calcular_media_tempo_consumo()
                print(f"Tempo total assistido: {total_consumo} segundos ou {self.converter_segundos(total_consumo)}") 
                print(f"Média de tempo assistido: {media_consumo:.2f} segundos") 

            
            #Comentários (apenas se houver comentários, com quantidade e numeração)
            comentarios = usuario.listar_comentarios()
            if comentarios:
                print(f"Quantidade de comentários: {len(comentarios)}") 
                for idx, c in enumerate(comentarios):
                    print(f"Comentário {idx+1}: {c}") 

            
            conteudos_unicos = usuario.obter_conteudos_unicos_consumidos()
            #Para adiconar chaves únicas ao dicionário de conteúdos consumidos por usuário
            if conteudos_unicos:
                print(f"Conteúdos únicos consumidos: {len(conteudos_unicos)}")

            
            plataformas_frequentes = usuario.plataformas_mais_frequentes(top_n=3)
            if plataformas_frequentes:
                print("Top 3 Plataformas Mais Frequentes:")
                for plat, cont in plataformas_frequentes:
                    print(f"             {plat.nome_plataforma}: {cont} interação(ões)")

            print("\n\n") 

    def gerar_relatorio_top_conteudos_consumidos(self, n=0):
    #Top 5 Conteudo mais consumidos
        if not self.__conteudos_registrados:
            print("Nenhum conteúdo registrado.") #Se não houver conteúdos registrados
            return

        ordenados = sorted(self.__conteudos_registrados.values(), key=lambda c: c.calcular_tempo_total_consumo(), reverse=True)
        #Função com lambda que ordena os conteúdos pelo tempo de consumo
        
        if n <= 0:
            top = ordenados  #Mostra todos os conteúdos.
        else:
            top = ordenados[:n]  #Mostra os top N indicados no main.

        print("\n-> -> TOP CONTEÚDOS POR TEMPO TOTAL CONSUMIDO <- <-\n")
        for idx, c in enumerate(top): #Enumera os Top N conteúdos por consumo
            tempo_total = c.calcular_tempo_total_consumo() #Super Classe em conteudo.py
            print(f"{idx+1}o. {c.nome_conteudo} ({self.converter_segundos(tempo_total)} consumidos)")
    
    
    def converter_segundos(self, total_segundos):
    #Função para Converter total de segundos do csv no formato HH:MM:SS
        if not isinstance(total_segundos, (int, float)) or total_segundos < 0:
            return "0:00:00" #Entradas inválidas

        horas = int(total_segundos // 3600)
        minutos = int((total_segundos % 3600) // 60)
        segundos = int(total_segundos % 60)

        return f"{horas}:{minutos:02}:{segundos:02}"