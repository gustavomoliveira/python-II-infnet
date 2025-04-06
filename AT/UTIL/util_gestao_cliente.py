from CRUD.crud_cliente import incluir_cliente, selecionar_cliente
from UTIL.util_entrada import validar_escolha

def cadastrar_novo_cliente():
    opcao = validar_escolha('\nDeseja cadastrar o cliente no sistema? ([1] - Sim / [2] - Finalizar Atendimento): ')
    if opcao == 2:
        print('\nEncerrando Atendimento ao Cliente.')
        return None

    cadastro_sucesso = incluir_cliente()
    return cadastro_sucesso

def processar_cliente_inexistente():
    cadastro_sucesso = cadastrar_novo_cliente()
    
    if cadastro_sucesso is None or cadastro_sucesso is False:
        return None
    
    cliente = selecionar_cliente()
    if cliente is False:
        print("\nErro ao recuperar cliente cadastrado.")
        return None
        
    return cliente