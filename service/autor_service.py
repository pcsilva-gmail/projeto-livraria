# from dao.categoriadao_import CategoriaDAO
# from model.categoria import Categoria
from dao.autor_dao import AutorDAO
from model.autor import Autor

class AutorService:


    def __init__(self):
        self.__autor_dao: AutorDAO = AutorDAO()


    @property
    def autor_dao(self) -> AutorDAO:
        return self.__autor_dao


    def menu(self):
        print('[Autores] Escolha uma das seguintes opções:\n'
                '1 - Listar todas os autores\n'
                '2 - Adicionar nova autor(a)\n'
                '3 - Excluir autor(a)\n'
                '4 - Ver autor(a) por Id\n'
                '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')


        if escolha == '0':
            return
        if escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida! Por favor, tente novamente!')

        self.menu()


    def listar(self):
        print('\nListando autores(as)...')

        try:
            autores = self.autor_dao.listar()
            if len(autores) == 0:
                print('Nenhum autor(a) encontrada!')


            for autor in autores:
                print(f'{autor.id} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.bio}')
        except Exception as e:
            print(f'Erro ao exibir as autores(as) ! - {e}')
            return

        input('Pressione uma tecla para continuar...')


    def adicionar(self):
        print('\nAdicionando autor(a)...')

        try:
            id = self.autor_dao.ultimo_id() + 1
         
            nome = input('Digite o nome do autor(a): ')
            email = input('Digite o email do autor(a): ')
            telefone = input('Digite o telefone do autor(a): ')
            bio = input('Digite a biografia do autor(a)')

            novo_autor = Autor(id, nome, email, telefone, bio)

            self.autor_dao.adicionar(novo_autor)
            print('Autor(a) adicionado com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir autor(a)! - {e}')
            return

        input('Pressione uma tecla para continuar...')


    def remover(self):
        print('\nRemovendo autor(a)...')

        try:
            autor_id = int(input('Digite o ID do autor(a) para excluir: '))
            if (self.__autor_dao.remover(autor_id)):
                print('Autor(a) excluído com sucesso!')
            else:
                print('Autor(a) não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir autor(a)! - {e}')
            return
       
        input('Pressione uma tecla para continuar...')


    def mostrar_por_id(self):
        print('\nAutor(a) por Id...')

        try:
            id = int(input('Digite o Id do Autor(a) para buscar: '))
            edit = self.__autor_dao.buscar_por_id(id)

            if (edit == None):
                print('Autor(a) não encontrada!')
            else:
                print(f'Id: {edit.id} | Autor(a): {edit.nome} | Email: {edit.email} | Telefone: {edit.telefone} | Bio: {edit.bio}')    
        except Exception as e:
            print(f'Erro ao exibir autor(a)! - {e}')
            return    
       
        input('Pressione uma tecla para continuar...')
