class No:
    #Nó da Árvore Binária de Busca com chave de comparação, valor associado e referencia filhos à esquerda e à direita.
    def __init__(self, chave, valor):
        self.chave = chave        #valor usado para ordenar na árvore
        self.valor = valor        #conteúdo associado a determinada chave
        self.esquerda = None      #filho à esquerda
        self.direita = None       #filho à direita


class ArvoreBinariaBusca:
    #Árvore Binária de Busca (BST) com inserção, busca, remoção e percurso dos elementos.
    def __init__(self):
        #Complexidade: O(1)
        self.raiz = None  #Ponto inicial

    def inserir(self, chave, valor):
        #Insere ou substitui chave, valor na árvore.
        #Complexidade: O(log n) em média, O(n) no pior caso (árvore desbalanceada)
        self.raiz = self._inserir_recursivo(self.raiz, chave, valor)

    def _inserir_recursivo(self, no, chave, valor):
        if no is None:
            return No(chave, valor)
        if chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave, valor)
        elif chave > no.chave:
            no.direita = self._inserir_recursivo(no.direita, chave, valor)
        else:
            no.valor = valor
        return no

    def buscar(self, chave):
        #Retorna chave ou None.
        #Complexidade: O(log n) em média, O(n) no pior caso
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        if no is None:
            return None
        if chave == no.chave:
            return no.valor
        elif chave < no.chave:
            return self._buscar_recursivo(no.esquerda, chave)
        else:
            return self._buscar_recursivo(no.direita, chave)

    def remover(self, chave):
        #Remove nó relacionado a determinada chave.
        #Complexidade: O(log n) em média, O(n) no pior caso
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, no, chave):
        if no is None:
            return None
        if chave < no.chave:
            no.esquerda = self._remover_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_recursivo(no.direita, chave)
        else:
            #Sem filhos
            if no.esquerda is None and no.direita is None:
                return None
            #Um filho
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            #Dois filhos, com substituição do menor da subárvore direita
            menor = self._encontrar_minimo(no.direita)
            no.chave, no.valor = menor.chave, menor.valor
            no.direita = self._remover_recursivo(no.direita, menor.chave)
        return no

    def _encontrar_minimo(self, no):
        #Nó com Menor Chave.
        #Complexidade: O(log n) em média, O(n) no pior caso
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def percurso_em_ordem(self):
        #Lista com chaves em ordem crescente
        #Complexidade: O(n)
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, lista):
        #Lista com valores determinados pela ordem esquerda|raiz|direita.
        if no is not None:
            self._em_ordem(no.esquerda, lista)
            lista.append(no.valor)
            self._em_ordem(no.direita, lista)
