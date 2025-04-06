from mysql.connector import Error
from conectar_bd import *

def incluir_item_bd(quantidade, compra, produto):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'INSERT INTO mercado_at.item (quantidade, id_compra, id_produto) VALUES (%s, %s, %s);'
        cursor.execute(query, (quantidade, compra[0], produto[0]))
        conn.commit()
        return True
    except Error as e:
        print(f'\nERRO: Não foi possível inserir os dados de item {e}.')
        return False
    finally:
        desconectar_bd(conn, cursor)

def consultar_item_bd(id_compra):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT * FROM mercado_at.item WHERE id_compra = %s;'
        cursor.execute(query, (id_compra,))
        item = cursor.fetchall()
        return item
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        desconectar_bd(conn, cursor)

def consultar_qtde_items_bd(id_compra):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT COUNT(id_item) FROM mercado_at.item WHERE id_compra = %s;'
        cursor.execute(query, (id_compra,))
        qtde_items = cursor.fetchone()
        return qtde_items[0]
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        desconectar_bd(conn, cursor)