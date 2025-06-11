from entidades.plataforma import Plataforma #Importa classes de plataforma.py

class Conteudo: #Classe Base para diversos Conteúdos. Super Classe de Video, Podcast e Artigo
    def __init__(self, id_conteudo, nome_conteudo):
        self._id_conteudo = id_conteudo
        self._nome_conteudo = nome_conteudo
        self._interacoes = [] #Lista para armazenar as interações associadas a este conteúdo
        

    @property
    def id_conteudo(self):
        return self._id_conteudo
        

    @property
    def nome_conteudo(self):
        return self._nome_conteudo
        

    def adicionar_interacao(self, interacao): #Adiciona interação a lista do Conteúdo
        self._interacoes.append(interacao)
        

    def calcular_total_interacoes_engajamento(self):
    #Calcula o total de Interações de Engajamento (Like, Share e Comment)
        total = 0
        for i in self._interacoes:
            if i.tipo_interacao in ["like", "share", "comment"]:
                total += 1
        return total
        

    def calcular_contagem_por_tipo_interacao(self): #Calcula o total de interações por tipo 
        contagem = {}
        for i in self._interacoes:
            tipo = i.tipo_interacao
            if tipo not in contagem:
                contagem[tipo] = 0
            contagem[tipo] += 1
        return contagem
        

    def calcular_tempo_total_consumo(self): #Calcula o tempo total de consumo do conteúdo.
        total = 0
        for i in self._interacoes:
            if isinstance(i.watch_duration_seconds, int) and i.watch_duration_seconds > 0:
                total += i.watch_duration_seconds #Watch_duration_seconds: Inteiro e Positivo
        return total
        

    def calcular_media_tempo_consumo(self): #Calcula o tempo médio de consumo do conteúdo.
        duracoes = []
        for i in self._interacoes:
            d = i.watch_duration_seconds
            if isinstance(d, int) and d > 0:
                duracoes.append(d)
        if len(duracoes) > 0:
            return sum(duracoes) / len(duracoes)
        else:
            return 0
    #Padronização desde Projeto 1: int e floats vazia retorna zero, strings vazias retorna none.
    

    def listar_comentarios(self): #Lista todos os comentários associados ao conteúdo.
        comentarios = []
        for i in self._interacoes:
            c = i.comment_text
            if c is None or c.strip() != "": # Adiciona apenas se o comentário não for vazio
                comentarios.append(c)
        return comentarios

    def __str__(self):
        return "Conteúdo ID " + str(self._id_conteudo) + ": " + self._nome_conteudo

    def __repr__(self):
        return self.__str__()
        
        

class Video(Conteudo): #Tipo de conteúdo analisado pelos dados do csv
    def __init__(self, id_conteudo, nome_conteudo, duracao_total_video_seg):
        super().__init__(id_conteudo, nome_conteudo)
        self.__duracao_total_video_seg = duracao_total_video_seg

    @property
    def duracao_total_video_seg(self):
        return self.__duracao_total_video_seg

    def calcular_percentual_medio_assistido(self): #Método Exclusivo
        if self.__duracao_total_video_seg == 0:
            return 0
        media = self.calcular_media_tempo_consumo()
        return (media / self.__duracao_total_video_seg) * 100
        

class Podcast(Conteudo): #Sem dados para análise
    def __init__(self, id_conteudo, nome_conteudo, duracao_total_episodio_seg=0):
        super().__init__(id_conteudo, nome_conteudo)
        self.__duracao_total_episodio_seg = duracao_total_episodio_seg

    @property
    def duracao_total_episodio_seg(self):
        return self.__duracao_total_episodio_seg
        

class Artigo(Conteudo): #Sem dados para análise
    def __init__(self, id_conteudo, nome_conteudo, tempo_leitura_estimado_seg=0):
        super().__init__(id_conteudo, nome_conteudo)
        self.__tempo_leitura_estimado_seg = tempo_leitura_estimado_seg

    @property
    def tempo_leitura_estimado_seg(self):
        return self.__tempo_leitura_estimado_seg

"""
As classes Podcast e Artigo são solicitadas nas diretrizes do projeto,
mas não é solicitado nenhum relatório sobre eles já que a origem dos
dados (interacoes_globo.csv) não apresenta nenhuma informação sobre
consumo de podcasts e/ou artigos. Portanto, as classes foram
modeladas para serem escalonadas numa futura refatoração do projeto
Fase_2.py, assim como está sendo feito do Fase_1.py para o Fase_2.py
"""