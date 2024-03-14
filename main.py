#from service.categoria_service import CategoriaService
from  service.categoria_service import CategoriaService
from  service.editora_service   import EditoraService
from  service.autor_service     import AutorService


categoria_service = CategoriaService()
editora_service = EditoraService()
autor_service =  AutorService()


def menu_principal():
    print('[Menu Principal] Escolha uma das seguintes opções:\n'
            '1 - Categorias\n'
            '2 - Editoras\n'
            '3 - Autores\n'
            '4 - Livros\n'
            '0 - Sair do programa\n')
    escolha = input('Digite a opção: ')


    if escolha == '0':
        print('Obrigado, até logo!')
        return
    if escolha == '1':
        categoria_service.menu()
    elif escolha == '2':
        editora_service.menu()
        print('Em construção...')
    elif escolha == '3':
        # print('Em construção...')
        autor_service.menu()
    elif escolha == '4':
        print('Em construção...')
    else:
        print('Opção inválida! Por favor, tente novamente!')


    menu_principal()


if __name__ == '__main__':
    print('Bem-vindo a Livraria SHIFT - Mastering Python!')
    menu_principal()
