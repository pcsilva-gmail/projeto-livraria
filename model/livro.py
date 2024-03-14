class Livro:
    # def __init__(self, id: int, nome: str):
    #     self.__id: int = id
    #     self.__nome: str = nome

    def __init__(self, id: int,
                       titulo: str,
                       resumo: str,
                       ano: int,
                       paginas: int,
                       isbn: str,
                       categoria_id: int,
                       editora_id: int,
                       autor_id: int):
        self.__id: int = id
        self.__titulo: str = titulo
        self.__resumo: str = resumo
        self.__ano: int = ano
        self.__paginas: int = paginas
        self.__isbn: str = isbn
        self.__categoria_id: int = categoria_id
        self.__editora_id: int = editora_id
        self.__autor_id: int = autor_id

    @property
    def id(self) -> int:
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

