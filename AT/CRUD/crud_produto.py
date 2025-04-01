from mysql.connector import Error
from conectar_bd import *

def consultar_produto(id):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.produto WHERE id_produto = %s'
        cursor.execute(query, (id,))
        produto = cursor.fetchone()
        if not produto:
            print('\nProduto não encontrado no sistema.')
            return False
        else:
            return produto
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_produto_nome(produto):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.produto WHERE nome = %s'
        cursor.execute(query, (produto[1],))
        novo_produto = cursor.fetchone()
        if not produto:
            print('\nProduto não encontrado no sistema.')
            return False
        else:
            return novo_produto
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_todos_produtos():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.produto'
        cursor.execute(query)
        produtos = cursor.fetchall()
        return produtos
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_tamanho_produtos():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = f'SELECT COUNT(*) FROM mercado_at.produto'
        cursor.execute(query)
        resultado = cursor.fetchone()
        return resultado[0]
    except Error as e:
        print(f'Erro ao verificar existência de dados: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def incluir_produto(nome, quantidade, preco):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'INSERT INTO mercado_at.produto (nome, quantidade, preco) VALUES (%s, %s, %s)'
        cursor.execute(query, (nome, quantidade, preco))
        conn.commit()
        print(f'\nO novo item "{nome}" foi inserido com sucesso no sistema.')
    except Error as e:
        print(f'\nERRO: Não foi possível inserir o produto "{nome}" no sistema: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def atualizar_produto(produto):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'UPDATE mercado_at.produto SET quantidade = %s WHERE id_produto = %s'
        cursor.execute(query, (produto[4], produto[0]))
        conn.commit()
    except Error as e:
        print(f'\nERRO: Não foi possível selecionar a quantidade do produto: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_estoque_final():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.produto'
        cursor.execute(query)
        produtos = cursor.fetchall()
        estoque = [[produto[1], produto[2]] for produto in produtos]
        return estoque
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()