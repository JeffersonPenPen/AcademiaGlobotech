class Plataforma:
    def __init__(self, nome_plataforma, id_plataforma=None):
    #Cria nova instância de plataforma
        if not nome_plataforma or not nome_plataforma.strip():
            raise ValueError("Nome da plataforma não pode ser vazio.")
        self.__nome_plataforma = nome_plataforma.strip()
        self.__id_plataforma = id_plataforma

    @property
    def nome_plataforma(self):
        return self.__nome_plataforma

    @nome_plataforma.setter
    #Padronização do argumento de todos os setters como "valor"
    def nome_plataforma(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Nome da plataforma não pode ser vazio.")
        self.__nome_plataforma = valor.strip()

    @property
    def id_plataforma(self):
        return self.__id_plataforma

    @id_plataforma.setter
    def id_plataforma(self, valor):
        self.__id_plataforma = valor

    def __str__(self): #Método Mágico que retorna apenas o nome da plataforma.
        return self.__nome_plataforma

    def __repr__(self): #Método Mágico que retorna Plataforma(nome='...') conforme solicitado no Projeto.
        return f"Plataforma(nome='{self.__nome_plataforma}')"

    def __eq__(self, other): #Método Mágico permite comparar duas plataformas pelo nome.
        if isinstance(other, Plataforma):
            return self.__nome_plataforma == other.__nome_plataforma
        return False

    def __hash__(self):
    #Método Mágico de hash do nome da plataforma para evitar duplicidade, para set ou dict.
        return hash(self.__nome_plataforma)
