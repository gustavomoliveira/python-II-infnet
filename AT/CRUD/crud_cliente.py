from CRUD_BD.crud_cliente_bd import *

def consultar_cliente():
    from UTIL.util_entrada import validar_inteiro

    id_cliente = validar_inteiro('\nInsira o ID do cliente para realizar a pesquisa: ')
    cliente = consultar_cliente_bd(id_cliente)
    if not cliente:
        print('\nCliente não encontrado no sistema.')
        return False
    else:
        print(f'\n{cliente[1]} encontrado no sistema!')
        return cliente
    
def incluir_cliente():
    from UTIL.util_entrada import validar_nome

    nome_cliente = validar_nome('\nInsira o nome do cliente a ser cadastrado: ')
    sucesso = incluir_cliente_bd(nome_cliente)
    if sucesso:
        print(f'\n{nome_cliente} cadastrado com sucesso no sistema.')
        return True
    return False

def selecionar_cliente():
    novo_cliente = selecionar_cliente_bd()
    if not novo_cliente:
        print('\nCliente não encontrado no sistema')
        return False
    else:
        return novo_cliente