class Conteudo:
    #Classe dos Conteúdos
    def __init__(self, id_conteudo, nome):
        self.id_conteudo = id_conteudo
        self.nome = nome
        self.interacoes = []

    def adicionar_interacao(self, interacao):
        #Adiciona Interação
        self.interacoes.append(interacao)

    def calcular_total_consumo(self):
        #Tempo Total de Visualização de Conteúdo em Vídeo
        total = 0
        for interacao in self.interacoes:
            if interacao.tipo == 'view_start':
                total += interacao.tempo
        return total

    def contar_comentarios(self):
        #Conta Comentários
        return sum(1 for i in self.interacoes if i.tipo == 'comment')

    def total_interacoes(self):
        #Retorna o número total de interações
        return len(self.interacoes)

    def __str__(self):
        return f"{self.nome} (ID: {self.id_conteudo})"


class Video(Conteudo):
    #Subclasse Vídeo
    pass

class Podcast(Conteudo):
    #Subclasse Podcast
    pass

class Artigo(Conteudo):
    #Subclasse Artigo
    pass
