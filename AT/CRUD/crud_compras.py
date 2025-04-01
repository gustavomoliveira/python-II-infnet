from mysql.connector import Error
from conectar_bd import *
from validacao import validar_data_hora
from CRUD.crud_produto import atualizar_produto, incluir_produto, consultar_produto_nome

def incluir_compra(cliente):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'INSERT INTO mercado_at.compra (data_compra, id_cliente) VALUES (%s, %s);'
        cursor.execute(query, (validar_data_hora(), cliente[0]))
        conn.commit()
        print(f'\nUm novo registro de compra foi gerado automaticamente pelo sistema.')
    except Error as e:
        print(f'\nERRO: Não foi possível inserir os dados de compra {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_compra_atual():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.compra ORDER BY id_compra DESC LIMIT 1;'
        cursor.execute(query)
        compra = cursor.fetchone()
        return compra
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_compras():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.compra;'
        cursor.execute(query)
        compras = cursor.fetchall()
        return compras
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def incluir_item(quantidade, compra, produto):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'INSERT INTO mercado_at.item (quantidade, id_compra, id_produto) VALUES (%s, %s, %s);'
        cursor.execute(query, (quantidade, compra[0], produto[0]))
        conn.commit()
        print(f'\nUm novo registro de item foi gerado automaticamente pelo sistema.')
    except Error as e:
        print(f'\nERRO: Não foi possível inserir os dados de item {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_item(compra):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.item WHERE id_compra = %s;'
        cursor.execute(query, (compra[0],))
        item = cursor.fetchall()
        return item
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_qtde_items(compra):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT COUNT(id_item) FROM mercado_at.item WHERE id_compra = %s;'
        cursor.execute(query, (compra[0],))
        qtde_items = cursor.fetchone()
        return qtde_items[0]
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def organizar_produtos_bd(produtos_pedido, compra_atual):
    for produto in produtos_pedido:
        if produto[0] > 0:
            print(f'\nAtualizando produto existente: {produto[1]}')
            atualizar_produto(produto)
            incluir_item(produto[2], compra_atual, produto)
        else:
            print(f'\nCadastrando novo produto: {produto[1]}')
            incluir_produto(produto[1], produto[4], produto[3])
            produto_cadastrado = consultar_produto_nome(produto)
            incluir_item(produto[2], compra_atual, produto_cadastrado)