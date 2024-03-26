from database.conexao_factory import ConexaoFactory
from model.editora import Editora

class EditoraDAO:
    def __init__(self):
        # self.__editoras: list[Editora] = list()
        self.__conexao_factory = ConexaoFactory()        


    def listar(self) -> list[Editora]:
        return self.__editoras


    def adicionar(self, editora: Editora) -> None:

        try:
            with self.__conexao_factory.get_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(
                                "INSERT INTO editoras (nome, endereco, telefone) VALUES (%(nome)s, %(endereco)s, %(telefone)s)",
                                ({'nome': editora.nome, 'endereco': editora.endereco, 'telefone': editora.telefone}))            
                    conexao.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            return

    def remover(self, editora_id: int) -> bool:
        encontrado = False
        for c in self.__editoras:
            if (c.id == editora_id):
                index = self.__editoras.index(c)
                self.__editoras.pop(index)
                encontrado = True
                break
        return encontrado


    def buscar_por_id(self, editora_id) -> Editora:
        cat = None
        for c in self.__editoras:
            if (c.id == editora_id):
                cat = c
                break
        return cat
   
    def ultimo_id(self) -> int:
        index = len(self.__editoras) -1
        if (index == -1):
            id = 0
        else:
            id = self.__editoras[index].id
        return id
