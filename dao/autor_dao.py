from model.autor import Autor
from database.conexao_factory import ConexaoFactory

class AutorDAO(ConexaoFactory):
    def __init__(self):
        self.__autores: list[Autor] = list()
        # self.__conexao_factory = ConexaoFactory().get_conexao()        


    def listar(self) -> list[Autor]:
        return self.__autores


    def adicionar(self, autor: Autor) -> None:
        self.__autores.append(autor)


    def remover(self, autor_id: int) -> bool:
        encontrado = False
        for c in self.__autores:
            if (c.id == autor_id):
                index = self.__autores.index(c)
                self.__autores.pop(index)
                encontrado = True
                break
        return encontrado


    def buscar_por_id(self, autor_id) -> Autor:
        aut = None
        try:
            with super().get_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(f"SELECT id, nome, email, telefone, bio FROM autores WHERE id = {autor_id}")
                    resultado = cursor.fetchone()
                    aut = Autor(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
                    if aut is None:
                        return None
                    return aut 
        except Exception as e:
            print(f"An error occurred: {e}")
            return aut
        # finally:
        #     cursor.close()
        #     conexao.close()                

   
    def ultimo_id(self) -> int:
        index = len(self.__autores) -1
        if (index == -1):
            id = 0
        else:
            id = self.__autores[index].id
        return id
