from CRUD_BD.crud_compra_bd import *

def incluir_compra(cliente):
    sucesso = incluir_compra_bd(cliente)
    if sucesso:
        print(f'\nUm novo registro de compra foi gerado automaticamente pelo sistema.')

def consultar_compra_atual():
    compra = consultar_compra_atual_bd()
    if not compra:
        print('\nCompra não encontrada no sistema.')
        return False
    else:
        return compra
    
def consultar_compras():
    compras = consultar_compras_bd()
    if not compras:
        print('\nCompras não encontrada no sistema.')
        return False
    else:
        return compras