from database.conexao_factory  import ConexaoFactory
from model.livro               import Livro
from domain.abstractrepository import AbstractRepository

from dao.autor_dao             import AutorDAO
from dao.categoria_dao         import CategoriaDAO
from dao.editora_dao           import EditoraDAO    

class LivroDAO(ConexaoFactory, AbstractRepository):

    def __init__(self):
        # self.__conexao_factory = super().get_conexao()
        self.__autordao: AutorDAO = AutorDAO()
        self.__categoriadao: CategoriaDAO = CategoriaDAO()
        self.__editoradao: EditoraDAO = EditoraDAO()
        self.__livros: list[Livro] = list()

    def listar(self) -> list[Livro]:
        livros = list()
        try:
            with super().get_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute('SELECT id, titulo, resumo, ano, paginas, isbn, categoria_id, editora_id, autor_id FROM livros')
                    resultados = cursor.fetchall()
                    for resultado in resultados:
                        cat = self.__categoriadao.buscar_por_id(resultado[6])
                        edt = self.__editoradao.buscar_por_id(resultado[7])
                        aut = self.__autordao.buscar_por_id(resultado[8])
                        # print(f'Resultado: {resultado[0]}, {resultado[1]}, {resultado[2]}, {resultado[3]}, {resultado[4]}, {resultado[5]}, {cat}, {edt}, {aut}')
                        livro = Livro(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], cat, edt, aut)
                        livros.append(livro)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None    
        return(livros)
    
    def adicionar(self, livro) -> None:
        # This method will be implemented by the concrete repositories
        raise NotImplemented

    def buscar_por_id( self, id: int) -> Livro:
        raise NotImplemented

    # Defining an abstract method called remove that takes one argument, 'chocolate_box'
    def remover(self, id: int) -> bool:
        # This method will be implemented by the concrete repositories
        raise NotImplemented

