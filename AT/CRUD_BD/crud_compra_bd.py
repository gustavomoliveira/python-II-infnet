from mysql.connector import Error
from conectar_bd import *
from UTIL.util import validar_data_hora

def incluir_compra_bd(cliente):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'INSERT INTO mercado_at.compra (data_compra, id_cliente) VALUES (%s, %s);'
        cursor.execute(query, (validar_data_hora(), cliente[0]))
        conn.commit()
        return True
    except Error as e:
        print(f'\nERRO: Não foi possível inserir os dados de compra {e}.')
        return False
    finally:
        desconectar_bd(conn, cursor)

def consultar_compra_atual_bd():
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT * FROM mercado_at.compra ORDER BY id_compra DESC LIMIT 1;'
        cursor.execute(query)
        compra = cursor.fetchone()
        return compra
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        desconectar_bd(conn, cursor)

def consultar_compras_bd():
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT * FROM mercado_at.compra;'
        cursor.execute(query)
        compras = cursor.fetchall()
        return compras
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        desconectar_bd(conn, cursor)