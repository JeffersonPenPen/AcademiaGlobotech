class Fila:
    def __init__(self):
        self._itens = []

    def enfileirar(self, item):
        #Adiciona ao final da fila
        self._itens.append(item)

    def desenfileirar(self):
        #Remove e retorna o primeiro item da fila
        if self.esta_vazia():
            raise IndexError("Fila vazia.")
        return self._itens.pop(0)

    def esta_vazia(self):
        #Checagem de Lista Vazia
        return len(self._itens) == 0

    def __len__(self):
        return len(self._itens)

    def __iter__(self):
        #Itera a fila
        return iter(self._itens)

    def espiar(self):
        #Checa próximo item da fila
        if self.esta_vazia():
            raise IndexError("Fila vazia.")
        return self._itens[0]
