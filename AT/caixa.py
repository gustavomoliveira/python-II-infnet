from base_dados import *
from atendimento import *
from UTIL.util import *
from CRUD.crud_produto import consultar_tamanho_produtos

def abrir_caixa():
    if consultar_tamanho_produtos() == 0:
        carregar_dados_iniciais()
    
    while True:
        opcao = menu()
        match opcao:
            case 1:
                iniciar_atendimento()
            case 2:
                exibir_estoque()
            case 0:
                fechar_caixa()
                break
            case _:
                print('\nERRO: Opção inválida.')
            
if __name__ == "__main__":
    abrir_caixa()