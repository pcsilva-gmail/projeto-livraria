from database.conexao_factory import ConexaoFactory
from model.categoria import Categoria

class CategoriaDAO:
    def __init__(self):
        # self.__categorias: list[Categoria] = list()
        self.__conexao_factory = ConexaoFactory()


    def listar(self) -> list[Categoria]:
        # return self.__categorias
        categorias = list()
        try:
            conexao = self.__conexao_factory.get_conexao()
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome FROM categorias")
            resultados = cursor.fetchall()
            for resultado in resultados:
                cat = Categoria(resultado[0], resultado[1])
                categorias.append(cat)
                # return categorias
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        finally:
            cursor.close()
            conexao.close()

        return(categorias)

    def adicionar(self, categoria: Categoria) -> None:
        # self.__categorias.append(categoria)
        try:
            conexao = self.__conexao_factory.get_conexao()
            cursor = conexao.cursor()
            cursor.execute(f"INSERT INTO categorias (nome) values('{categoria.nome}')")
            conexao.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        finally:
            if conexao:
                cursor.close()
                conexao.close()


    def remover(self, categoria_id: int) -> bool:
        # encontrado = False
        # for c in self.__categorias:
        #     if (c.id == categoria_id):
        #         index = self.__categorias.index(c)
        #         self.__categorias.pop(index)
        #         encontrado = True
        #         break
        encontrado = False
        try:
            conexao = self.__conexao_factory.get_conexao()
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM categorias WHERE id = {categoria_id}")
            categorias_removidas = cursor.rowcount
            if (categorias_removidas == 0):
                return False
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        finally:
            cursor.close()
            conexao.close()



        return encontrado


    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        # for c in self.__categorias:
        #     if (c.id == categoria_id):
        #         cat = c
        #         break
        try:
            conexao = self.__conexao_factory.get_conexao()
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome FROM categoria WHERE id = {categoria_id}")
            resultado = cursor.fetchone()
            cat = Categoria(resultado[0], resultado[1])
            if cat is None:
                return None
            return cat 
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        finally:
            cursor.close()
            conexao.close()        
        
   
    def ultimo_id(self) -> int:
        index = len(self.__categorias) -1
        if (index == -1):
            id = 0
        else:
            id = self.__categorias[index].id
        return id
