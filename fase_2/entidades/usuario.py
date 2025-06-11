from collections import Counter

class Usuario: #Cada um dos usuários, suas interações e métricas
    def __init__(self, id_usuario):
        # Atributos privados conforme diretrizes
        self.__id_usuario = id_usuario
        self.__interacoes_realizadas = [] # Lista de objetos Interacao

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def interacoes_realizadas(self):
        return self.__interacoes_realizadas

    def registrar_interacao(self, interacao): 
    #Adiciona uma interação à lista de interações realizadas pelo usuário
        self.__interacoes_realizadas.append(interacao)

    def obter_interacoes_por_tipo(self, tipo_desejado: str) -> list: 
    #Retorna uma lista de um tipo de interação.
        return [i for i in self.__interacoes_realizadas if i.tipo_interacao == tipo_desejado]

    def obter_conteudos_unicos_consumidos(self) -> set: 
    #Retorna set de conteúdos únicos consumidos pelo usuário.
        conteudos = set()
        for interacao in self.__interacoes_realizadas:
            if interacao.conteudo_associado:
                conteudos.add(interacao.conteudo_associado)
        return conteudos

    def calcular_tempo_total_consumo_plataforma(self, plataforma) -> int: #Tempo total de consumo de um usuário em uma plataforma
        total_tempo = 0
        for interacao in self.__interacoes_realizadas:
            if interacao.plataforma_interacao == plataforma:
                if isinstance(interacao.watch_duration_seconds, int) and interacao.watch_duration_seconds > 0: #Inteiro e Positivo
                    total_tempo += interacao.watch_duration_seconds
        return total_tempo

    def plataformas_mais_frequentes(self, top_n=3) -> list:
    #3 Plataformas onde o usuário mais interage - Tupla (Plataforma, Contagem)
        plataformas = []
        for interacao in self.__interacoes_realizadas:
            if interacao.plataforma_interacao:
                plataformas.append(interacao.plataforma_interacao)
        
        contagem_plataformas = Counter(plataformas) #Counter para Frequência
        
        top_plataformas = contagem_plataformas.most_common(top_n) #Ordenar por quantidade
        return top_plataformas
    """
    Uso de collections.Counter para otimizar o código, mas segue abaixo
    lógico sem uso de biblioteca externa.
    
    def plataformas_mais_frequentes(self, top_n=3):
        contagem = {}
        for interacao in self.__interacoes_realizadas:
            plataforma_obj = interacao.plataforma_interacao
            if plataforma_obj:
                if plataforma_obj not in contagem:
                    contagem[plataforma_obj] = 0
                contagem[plataforma_obj] += 1
        top_resultados = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        return top_resultados[:top_n]
    """


    def calcular_total_interacoes_engajamento(self):
    #Total de interações de engajamento (like, share, comment) do usuário.
        total = 0
        for i in self.__interacoes_realizadas:
            if i.tipo_interacao in ["like", "share", "comment"]:
                total += 1
        return total

    def calcular_contagem_por_tipo_interacao(self):
    #Quantidade de interações por tipo para o usuário.
        contagem = {}
        for i in self.__interacoes_realizadas:
            tipo = i.tipo_interacao
            if tipo not in contagem:
                contagem[tipo] = 0
            contagem[tipo] += 1
        return contagem

    def calcular_tempo_total_consumo(self):
        total = 0
        for i in self.__interacoes_realizadas:
            if isinstance(i.watch_duration_seconds, int) and i.watch_duration_seconds > 0:
                total += i.watch_duration_seconds
        return total

    def calcular_media_tempo_consumo(self):
        duracoes = []
        for i in self.__interacoes_realizadas:
            d = i.watch_duration_seconds
            if isinstance(d, int) and d > 0:
                duracoes.append(d)
        if duracoes:
            return sum(duracoes) / len(duracoes)
        else:
            return 0

    def listar_comentarios(self):
        comentarios = []
        for i in self.__interacoes_realizadas:
            c = i.comment_text
            if c: 
                comentarios.append(c)
        return comentarios

    def __str__(self):
        return f"Usuário ID {self.__id_usuario}"

    def __repr__(self):
        return self.__str__()

