from base_dados import *
from interface import *

def abrir_caixa():
    resultado = consultar_tamanho_produtos()
    if resultado == 0:
        arq_produtos = definir_arquivo('CSV/produtos.csv')
        arq_clientes = definir_arquivo('CSV/clientes.csv')

        df_produtos = criar_df(arq_produtos)
        df_clientes = criar_df(arq_clientes)

        query_produtos = """ INSERT INTO mercado_at.produto (nome, quantidade, preco)
            VALUES (%s, %s, %s) """
        importar_dados_iniciais(df_produtos, query_produtos)

        query_clientes = """ INSERT INTO mercado_at.cliente (nome)
            VALUES (%s) """
        importar_dados_iniciais(df_clientes, query_clientes)

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


