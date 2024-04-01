from database.conexao_factory  import ConexaoFactory
from model.editora             import Editora
from domain.editorarepository  import AbstractRepository

class EditoraDAO(AbstractRepository, ConexaoFactory):

    # def __init__(self):
        # self.__conexao_factory = super().get_conexao()

    def listar(self) -> list[Editora]:
        editoras = list()

        try:
            with super().get_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute("SELECT id, nome, endereco, telefone FROM editoras")
                    resultados = cursor.fetchall()
                    for resultado in resultados:
                        edit =Editora(resultado[0], resultado[1], resultado[2], resultado[3])
                        editoras.append(edit)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        # finally:
        #      cursor.close()
        #      conexao.close()
        return(editoras)        

    def adicionar(self, editora: Editora) -> None:

        try:
            with super().get_conexao() as conexao: #.get_conexao() as conexao:
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
        try:
            with super().get_conexao() as conexao:
                with  conexao.cursor() as cursor:
                    cursor.execute(f"DELETE FROM editoras WHERE id = {editora_id}")
                    editoras_removidas = cursor.rowcount
                    if (editoras_removidas == 0):
                        encontrado = False
                    else:
                        encontrado = True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        # finally:
        #     cursor.close()
        #     conexao.close()
        return encontrado

    def buscar_por_id(self, editora_id) -> Editora:
        edit = None
        try:
            with super().get_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(f"SELECT id, nome, endereco, telefone FROM editoras WHERE id = {editora_id}")
                    resultado = cursor.fetchone()
                    if resultado:
                        edit = Editora(resultado[0], resultado[1], resultado[2], resultado[3])
        except Exception as e:
            print(f"An error occurred: {e}")
            return edit
        return edit
   
    def ultimo_id(self) -> int:
        index = len(self.__editoras) -1
        if (index == -1):
            id = 0
        else:
            id = self.__editoras[index].id
        return id

    def __enter__():
        print('Entrou no __enter__()')

    def __exit__(self):
        print('Entrou no __exit__()')            
            


