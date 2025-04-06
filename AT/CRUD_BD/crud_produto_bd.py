from mysql.connector import Error
from conectar_bd import *

def consultar_produto_bd(id):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT * FROM mercado_at.produto WHERE id_produto = %s'
        cursor.execute(query, (id,))
        produto = cursor.fetchone()
        return produto
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        desconectar_bd(conn, cursor)

def consultar_produto_nome_bd(nome_produto):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT * FROM mercado_at.produto WHERE nome = %s'
        cursor.execute(query, (nome_produto,))
        novo_produto = cursor.fetchone()
        return novo_produto
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        desconectar_bd(conn, cursor)

def consultar_todos_produtos_bd():
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'SELECT * FROM mercado_at.produto'
        cursor.execute(query)
        produtos = cursor.fetchall()
        return produtos
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        desconectar_bd(conn, cursor)

def consultar_tamanho_produtos_bd():
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = f'SELECT COUNT(*) FROM mercado_at.produto'
        cursor.execute(query)
        resultado = cursor.fetchone()
        return resultado[0]
    except Error as e:
        print(f'Erro ao verificar existência de dados: {e}')
    finally:
        desconectar_bd(conn, cursor)

def incluir_produto_bd(nome, quantidade, preco):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'INSERT INTO mercado_at.produto (nome, quantidade, preco) VALUES (%s, %s, %s)'
        cursor.execute(query, (nome, quantidade, preco))
        conn.commit()
        return True
    except Error as e:
        print(f'\nERRO: Não foi possível inserir o produto "{nome}" no sistema: {e}.')
        return False
    finally:
        desconectar_bd(conn, cursor)

def atualizar_produto_bd(produto):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        query = 'UPDATE mercado_at.produto SET quantidade = %s WHERE id_produto = %s'
        cursor.execute(query, (produto[4], produto[0]))
        conn.commit()
        return True
    except Error as e:
        print(f'\nERRO: Não foi possível atualizar o produto selecionado: {e}.')
        return False
    finally:
        desconectar_bd(conn, cursor)