class Usuario:
    #Interaçoes por Usuário
    def __init__(self, id_usuario, nome=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.interacoes = []

    def adicionar_interacao(self, interacao):
        self.interacoes.append(interacao)

    def total_interacoes(self):
        return len(self.interacoes)

    def tempo_total_consumo(self):
        return sum(i.tempo for i in self.interacoes if i.tipo == "view_start")

    def __str__(self):
        return f"Usuário {self.id_usuario}" + (f" - {self.nome}" if self.nome else "")
