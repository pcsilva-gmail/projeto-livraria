class Categoria:

    def __init__(self, id: int=None, nome: str=None):
        self.__id: int = id
        self.__nome: str = nome

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

