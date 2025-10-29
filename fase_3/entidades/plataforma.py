class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.interacoes = []

    def adicionar_interacao(self, interacao):
        self.interacoes.append(interacao)

    def total_interacoes(self):
        return len(self.interacoes)

    def tempo_medio_consumo(self):
        tempos = [i.tempo for i in self.interacoes if i.tipo == "view_start"]
        if not tempos:
            return 0
        return sum(tempos) / len(tempos)

    def __str__(self):
        return f"{self.nome} - {self.total_interacoes()} interações"
