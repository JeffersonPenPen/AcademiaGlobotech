from datetime import datetime #Biblioteca utilizada conforme projeto Fase_1
from entidades.plataforma import Plataforma
from entidades.conteudo import Conteudo

class Interacao: #Uma interação de um usuário um conteúdo em uma plataforma.
    TIPOS_INTERACAO_VALIDOS = {"view_start", "like", "share", "comment", "vote_bbb"}
    __proximo_id = 1 # Contador para gerar IDs únicos para interações

    def __init__(self, id_usuario, timestamp, tipo_interacao, watch_duration_seconds=0, comment_text="", conteudo_associado=None, plataforma_interacao=None):
        #Padronização desde Projeto 1: int e floats vazia retorna zero, strings vazias retorna none.
        self.__interacao_id = Interacao.__proximo_id
        Interacao.__proximo_id += 1

        self.__id_usuario = int(id_usuario)

        try:
            self.__timestamp_interacao = datetime.fromisoformat(timestamp)
        except ValueError:
            self.__timestamp_interacao = datetime.min 
        
        self.__tipo_interacao = tipo_interacao if tipo_interacao in self.TIPOS_INTERACAO_VALIDOS else "view_start"
        #Se inválido, usa "view_start" como interação minima.

        try:
            self.__watch_duration_seconds = int(watch_duration_seconds)
            if self.__watch_duration_seconds < 0:
                self.__watch_duration_seconds = 0
        except (ValueError, TypeError): 
            self.__watch_duration_seconds = 0 #Duração inválida

        self.__comment_text = comment_text.strip() if comment_text else ""
        self.__conteudo_associado = conteudo_associado
        self.__plataforma_interacao = plataforma_interacao

    @property
    def interacao_id(self):
        return self.__interacao_id

    @property
    def conteudo_associado(self):
        return self.__conteudo_associado

    @property
    def plataforma_interacao(self):
        return self.__plataforma_interacao

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def timestamp_interacao(self):
        # Retorna o objeto datetime
        return self.__timestamp_interacao

    @property
    def tipo_interacao(self):
        return self.__tipo_interacao

    @property
    def watch_duration_seconds(self):
        return self.__watch_duration_seconds

    @property
    def comment_text(self):
        return self.__comment_text

    def __str__(self): #Método mágico que define como será apresentado ao usuário
        return f"Interação {self.__interacao_id}: {self.__tipo_interacao} por usuário {self.__id_usuario} em {self.conteudo_associado.nome_conteudo}"

    def __repr__(self): #Método Mágico de representação interna
        return (f"Interacao(id={self.__interacao_id}, usuario={self.__id_usuario}, tipo='{self.__tipo_interacao}', "
                f"duracao={self.__watch_duration_seconds}, comentario='{self.__comment_text}')")