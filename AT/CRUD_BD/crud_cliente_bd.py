from mysql.connector import Error
from conectar_bd import *

def consultar_cliente_bd(id):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT * FROM mercado_at.cliente WHERE id_cliente = %s;'
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()
        return cliente
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        desconectar_bd(conn, cursor)

def incluir_cliente_bd(nome):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'INSERT INTO mercado_at.cliente (nome) VALUES (%s);'
        cursor.execute(query, (nome,))
        conn.commit()
        return True
    except Error as e:
        print(f'\nERRO: Não foi possível inserir os dados {e}.')
        return False
    finally:
        desconectar_bd(conn, cursor)

def selecionar_cliente_bd():
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT * FROM mercado_at.cliente ORDER BY id_cliente DESC LIMIT 1;'
        cursor.execute(query)
        novo_cliente = cursor.fetchone()
        return novo_cliente
    except Error as e:
        print(f'\nERRO: Não foi possível inserir os dados {e}.')
    finally:
        desconectar_bd(conn, cursor)