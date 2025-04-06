from base_dados import *
from atendimento import *
from UTIL.util import *
from CRUD.crud_produto import consultar_tamanho_produtos, consultar_estoque_final

def abrir_caixa():
    if consultar_tamanho_produtos() == 0:
        carregar_dados_iniciais()

    total_vendas = []
    clientes_atendidos = []
    
    while True:
        opcao = menu()
        match opcao:
            case 1:
                soma_total, cliente = iniciar_atendimento()
                total_vendas.append(soma_total)
                clientes_atendidos.append(cliente)
            case 2:
                exibir_estoque(consultar_estoque_final())
            case 0:
                fechar_caixa(total_vendas, clientes_atendidos)
                break
            case _:
                print('\nERRO: Opção inválida.')
            
if __name__ == "__main__":
    abrir_caixa()


