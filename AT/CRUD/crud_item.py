from CRUD_BD.crud_item_bd import *

def incluir_item(quantidade, compra, produto):
    sucesso = incluir_item_bd(quantidade, compra, produto)
    if sucesso:
        print(f'\nUm novo registro de item foi gerado automaticamente pelo sistema.')
    
def consultar_item(compra):
    id_compra = compra[0]
    item = consultar_item_bd(id_compra)
    if not item:
        print('\nItem não encontrado no sistema.')
        return False
    else:
        return item
    
def consultar_qtde_items(compra):
    id_compra = compra[0]
    qtde_items = consultar_qtde_items_bd(id_compra)
    if not qtde_items:
        print('\nQuantidade de itens não pôde ser verificada no sistema.')
        return False
    else:
        return qtde_items