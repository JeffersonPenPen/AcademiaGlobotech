class Fila:
    def __init__(self):
        #Complexidade: O(1)
        self._itens = []

    def enfileirar(self, item):
        #Adiciona ao final da fila
        #Complexidade: O(1)
        self._itens.append(item)

    def desenfileirar(self):
        #Remove e retorna o primeiro item da fila
        #Complexidade: O(n) - Todos os elementos são deslocados
        if self.esta_vazia():
            raise IndexError("Fila vazia.")
        return self._itens.pop(0)

    def esta_vazia(self):
        #Checagem de Lista Vazia
        #Complexidade: O(1)
        return len(self._itens) == 0

    def __len__(self):
        #Complexidade: O(1)
        return len(self._itens)

    def __iter__(self):
        #Itera a fila
        return iter(self._itens)

    def espiar(self):
        #Checa próximo item da fila
        #Complexidade: O(1)
        if self.esta_vazia():
            raise IndexError("Fila vazia.")
        return self._itens[0]
