class Plataforma:
    """
    Representa uma plataforma (ex: Globoplay, G1, etc.) onde os conteúdos são consumidos.
    Armazena todas as interações feitas nela.
    """
    def __init__(self, nome):
        self.nome = nome
        self.interacoes = []

    def adicionar_interacao(self, interacao):
        """
        Registra uma nova interação nesta plataforma.
        """
        self.interacoes.append(interacao)

    def total_interacoes(self):
        """
        Retorna o número total de interações nesta plataforma.
        """
        return len(self.interacoes)

    def tempo_medio_consumo(self):
        """
        Calcula o tempo médio de consumo (apenas interações do tipo 'view_start').
        """
        tempos = [i.tempo for i in self.interacoes if i.tipo == "view_start"]
        if not tempos:
            return 0
        return sum(tempos) / len(tempos)

    def __str__(self):
        return f"{self.nome} - {self.total_interacoes()} interações"
