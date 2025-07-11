from estruturas_dados.fila import Fila
from estruturas_dados.arvore_binaria_busca import ArvoreBinariaBusca
from entidades.usuario import Usuario
from entidades.conteudo import Video, Podcast, Artigo
from entidades.plataforma import Plataforma
from entidades.interacao import Interacao

def quick_sort(lista, chave):
    #Ordena a lista de objetos com base em uma chave (atributo ou método).
    #Complexidade: O(n log n) em média, O(n^2) no pior caso.
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        valor_pivo = chave(pivo)
        
        menores = [x for x in lista[1:] if chave(x) <= valor_pivo]
        maiores = [x for x in lista[1:] if chave(x) > valor_pivo]
        
        return quick_sort(maiores, chave) + [pivo] + quick_sort(menores, chave)

def converter_segundos(total_segundos):
    #Converte segundos em formato H:MM:SS para facilitar análise pelo usuário.
    if not isinstance(total_segundos, (int, float)) or total_segundos < 0:
        return "0:00:00"
    horas = int(total_segundos // 3600)
    minutos = int((total_segundos % 3600) // 60)
    segundos = int(total_segundos % 60)
    return f"{horas}:{minutos:02}:{segundos:02}"

class SistemaAnaliseEngajamento:
    #Sistema principal de analise
    def __init__(self):
        self._fila_interacoes = Fila()
        self._usuarios = ArvoreBinariaBusca()
        self._conteudos = ArvoreBinariaBusca()
        self._plataformas = {}

    def carregar_interacoes_csv(self, caminho_csv):
        #Carrega os dados do csv, seguindo a nomenclatura das colunas
        #Complexidade: O(n) - n=linhas no CSV.
        import csv

        try:
            with open(caminho_csv, newline='', encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    self._fila_interacoes.enfileirar(linha)
            print(f"[INFO] {len(self._fila_interacoes)} interações carregadas na fila.")
        except Exception as e:
            print(f"[ERRO] Falha ao carregar CSV: {e}")

    def processar_interacoes(self):
        #Processa as interaçoes nas filas, cria usuarios, conteudos e plataformas, analisa as interaçoes e envia para as entidades.
        #Complexidade: O(n * log k) - n=interações,  k=usuários/conteúdos únicos.
        if self._fila_interacoes.esta_vazia():
            print("[ERRO] Fila vazia. Use a opção de carregar dados primeiro.")
            return

        while not self._fila_interacoes.esta_vazia():
            linha = self._fila_interacoes.desenfileirar()

            try:
                id_usuario = linha.get("id_usuario", "").strip()
                tipo = linha.get("tipo_interacao", "").strip().lower()
                nome_conteudo = linha.get("nome_conteudo", "").strip()
                id_conteudo = int(linha.get("id_conteudo", 0) or 0)
                nome_plataforma = linha.get("plataforma", "").strip()
                tempo = float(linha.get("watch_duration_seconds", 0) or 0)
                comment_text = linha.get("comment_text", "")
                comentario = str(comment_text).strip() if comment_text else ""
                tipo_conteudo = linha.get("tipo_conteudo", "video").strip().lower()

                if not id_usuario or not tipo or not nome_conteudo or not nome_plataforma:
                    raise ValueError("Campos obrigatórios ausentes.")

                #Obter ou criar Plataforma
                if nome_plataforma not in self._plataformas:
                    self._plataformas[nome_plataforma] = Plataforma(nome_plataforma)
                plataforma = self._plataformas[nome_plataforma]

                #Obter ou criar Usuario
                usuario = self._usuarios.buscar(id_usuario)
                if not usuario:
                    usuario = Usuario(id_usuario)
                    self._usuarios.inserir(id_usuario, usuario)

                #Obter ou criar Conteúdo
                conteudo = self._conteudos.buscar(id_conteudo)
                if not conteudo:
                    if tipo_conteudo == "video":
                        conteudo = Video(id_conteudo, nome_conteudo)
                    elif tipo_conteudo == "podcast":
                        conteudo = Podcast(id_conteudo, nome_conteudo)
                    else:
                        conteudo = Artigo(id_conteudo, nome_conteudo)
                    self._conteudos.inserir(id_conteudo, conteudo)

                #Criar e distribuir a interação
                interacao = Interacao(usuario, conteudo, tipo, tempo, comentario, plataforma)

                usuario.adicionar_interacao(interacao)
                conteudo.adicionar_interacao(interacao)
                plataforma.adicionar_interacao(interacao)

            except Exception as e:
                print(f"[ERRO] Interação ignorada por erro de dados: {e}")

        print("[INFO] Fila processada com sucesso.")

    #->-> RELATÓRIOS <-<-

    def relatorio1_top_conteudos_por_consumo(self, top_n=10):
        print("\n->-> RELATÓRIO 1: Top Conteúdos por Tempo de Consumo <-<-\n")
        todos = self._conteudos.percurso_em_ordem()
        ordenados = quick_sort(todos, lambda c: c.calcular_total_consumo())
        for i, conteudo in enumerate(ordenados[:top_n], 1):
            tempo = conteudo.calcular_total_consumo()
            print(f"{i}. {conteudo.nome} - {tempo:.0f} segundos ou {converter_segundos(tempo)}")

    def relatorio2_usuarios_mais_engajados(self, top_n=10):
        print("\n->-> RELATÓRIO 2: Usuários com Maior Tempo de Consumo <-<-\n")
        todos = self._usuarios.percurso_em_ordem()
        ordenados = quick_sort(todos, lambda u: u.tempo_total_consumo())
        for i, usuario in enumerate(ordenados[:top_n], 1):
            print(f"{i}. {usuario.id_usuario} - {usuario.tempo_total_consumo():.0f} segundos ou {converter_segundos(usuario.tempo_total_consumo())}")

    def relatorio3_engajamento_por_plataforma(self):
        print("\n->-> RELATÓRIO 3: Engajamento por Plataforma <-<-\n")
        plataformas_lista = list(self._plataformas.values())
        ordenadas = quick_sort(plataformas_lista, lambda p: p.total_interacoes())
        for plataforma in ordenadas:
            print(f"{plataforma.nome}: {plataforma.total_interacoes()} interações")

    def relatorio4_conteudos_mais_comentados(self, top_n=10):
        print("\n->-> RELATÓRIO 4: Conteúdos Mais Comentados <-<-\n")
        todos = self._conteudos.percurso_em_ordem()
        ordenados = quick_sort(todos, lambda c: c.contar_comentarios())
        for i, conteudo in enumerate(ordenados[:top_n], 1):
            print(f"{i}. {conteudo.nome} - {conteudo.contar_comentarios()} comentários")

    def relatorio5_total_interacoes_por_tipo(self):
        print("\n->-> RELATÓRIO 5: Total de Interações por Tipo <-<-\n")
        contagem = {}
        for plataforma in self._plataformas.values():
            for i in plataforma.interacoes:
                contagem[i.tipo] = contagem.get(i.tipo, 0) + 1
        for tipo, total in contagem.items():
            print(f"{tipo}: {total} interações")

    def relatorio6_tempo_medio_por_plataforma(self):
        print("\n->-> RELATÓRIO 6: Tempo Médio de Consumo por Plataforma <-<-\n")
        for nome, plataforma in self._plataformas.items():
            media = plataforma.tempo_medio_consumo()
            print(f"{nome}: {media:.0f} segundos ou {converter_segundos(media)}")

    def relatorio7_comentarios_por_conteudo(self):
        print("\n->-> RELATÓRIO 7: Comentários por Conteúdo <-<-\n")
        todos = self._conteudos.percurso_em_ordem()
        for conteudo in todos:
            comentarios = [
                i.comentario for i in conteudo.interacoes
                if i.comentario and i.comentario.strip()
            ]
            if comentarios:
                qtd = len(comentarios)
                sufixo = "comentário" if qtd == 1 else "comentários"
                print(f"{conteudo.nome} ({qtd} {sufixo}):")
                for c in comentarios:
                    print(f"- {c}")
                print()  #Linha em branco por estética

    def relatorio8_conteudos_mais_interagidos(self, top_n=10):
        print("\n->-> RELATÓRIO 8: Conteúdos com Mais Interações <-<-\n")
        todos = self._conteudos.percurso_em_ordem()
        ordenados = quick_sort(todos, lambda c: c.total_interacoes())
        for i, conteudo in enumerate(ordenados[:top_n], 1):
            print(f"{i}. {conteudo.nome} - {conteudo.total_interacoes()} interações")

