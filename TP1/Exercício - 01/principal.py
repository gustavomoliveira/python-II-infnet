from utilitario import *
from crud import *

def iniciar_programa():
    produtos = {}
    while True:
        opcao = menu()
        match opcao:
            case 1:
                produtos = inserir_produto(produtos)
            case 2:
                consultar_produto(produtos)
            case 3:
                produtos = alterar_produto(produtos)
            case 4:
                excluir_produto(produtos)
            case 0:
                exibir_produtos(produtos)
                break
            case _:
                print('\nERRO: Opção inválida.')

if __name__ == '__main__':   
    iniciar_programa()






    

