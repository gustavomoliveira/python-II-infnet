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

def consultar_resumo_compra_bd(id_compra):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = '''
            SELECT p.nome, i.quantidade, p.preco, (i.quantidade * p.preco) as subtotal  
            FROM mercado_at.item i
            JOIN mercado_at.produto p ON i.id_produto = p.id_produto
            WHERE i.id_compra = %s
        '''
        cursor.execute(query, (id_compra,))
        itens = cursor.fetchall()
        return itens
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a consulta: {e}.')
        return []
    finally:
        desconectar_bd(conn, cursor)

def consultar_resumo_diario_bd():
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = '''
            SELECT cl.nome, SUM(p.preco * i.quantidade) as total
            FROM mercado_at.compra c
            JOIN mercado_at.cliente cl ON c.id_cliente = cl.id_cliente
            JOIN mercado_at.item i ON c.id_compra = i.id_compra
            JOIN mercado_at.produto p ON i.id_produto = p.id_produto
            GROUP BY cl.nome
            ORDER BY total DESC
        '''
        cursor.execute(query)
        resumo = cursor.fetchall()
        return resumo
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a consulta: {e}.')
        return []
    finally:
        desconectar_bd(conn, cursor)