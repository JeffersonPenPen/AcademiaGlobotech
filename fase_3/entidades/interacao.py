class Interacao:
    #Iteraçao do Usuário com o Conteúdo
    def __init__(self, usuario, conteudo, tipo, tempo=0, comentario="", plataforma=None):
        self.usuario = usuario            #Objeto Usuario
        self.conteudo = conteudo          #Objeto Conteudo (ou subclasse)
        self.tipo = tipo.lower().strip()  #Formas de Interaçao: 'view_start', 'comment', "like" e "share"
        self.tempo = float(tempo)         #Duração em segundos
        self.comentario = comentario.strip()  #Comentários dos Usuários
        self.plataforma = plataforma      #Objeto Plataforma

    def __str__(self):
        resumo = f"{self.tipo.upper()} - Usuário {self.usuario.id_usuario} → Conteúdo {self.conteudo.nome}"
        if self.tipo == "comment":
            resumo += f"\nComentário: {self.comentario}"
        return resumo