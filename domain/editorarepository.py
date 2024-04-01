from database.conexao_factory  import ConexaoFactory
from model.editora             import Editora
from domain.abstractrepository import AbstractRepository

class EditoraReporitory(AbstractRepository, ConexaoFactory):

    def listar(self) -> list[Editora]:
        self.__conexao_factory = super().get_conexao()        
        editoras = list()
        try:
            with self.__conexao_factory as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute("SELECT id, nome, endereco, telefone FROM editoras")
                    resultados = cursor.fetchall()
                    for resultado in resultados:
                        edit =Editora(resultado[0], resultado[1], resultado[2], resultado[3])
                        editoras.append(edit)
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        return editoras 
    
    def adicionar(self, repository) -> None:
        # This method will be implemented by the concrete repositories
        raise NotImplemented
    
    def buscar_por_id( self, id: int) -> object:
        raise NotImplemented

    # Defining an abstract method called remove that takes one argument, 'chocolate_box'

    def remover(self, id: int) -> bool:
        # This method will be implemented by the concrete repositories
        raise NotImplemented
