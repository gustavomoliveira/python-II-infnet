from mysql.connector import Error
from conectar_bd import *
from validacoes import *

def consultar_cliente():
    id = validar_inteiro('\nInsira o ID do cliente para realizar a pesquisa: ')
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.cliente WHERE id_cliente = %s;'
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()

        if cliente:
            print(f'\nCliente encontrado! Nome: {cliente[1]}.')
        else:
            print('\nCliente não encontrado no sistema.')
        return cliente
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def incluir_cliente():
    nome = validar_nome_cliente('\nInsira o nome do cliente a ser cadastrado: ')
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'INSERT INTO mercado_at.cliente (nome) VALUES (%s);'
        cursor.execute(query, (nome,))
        conn.commit()
        print('\nNovo cliente inserido com sucesso!')

        query = 'SELECT * FROM mercado_at.cliente ORDER BY id_cliente DESC LIMIT 1;'
        cursor.execute(query)
        novo_cliente = cursor.fetchone()
        return novo_cliente
    except Error as e:
        print(f'\nErro na inserção dos dados: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def incluir_compra(cliente):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'INSERT INTO mercado_at.compra (data_compra, id_cliente) VALUES (%s, %s);'
        cursor.execute(query, (validar_data_hora(), cliente[0]))
        conn.commit()
        print(f'\nUm novo registro de compra foi gerado automaticamente pelo sistema.')
    except Error as e:
        print(f'\nErro na inserção dos dados de compra: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_compra():
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

def consultar_produto(id):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.produto WHERE id_produto = %s;'
        cursor.execute(query, (id,))
        produto = cursor.fetchone()

        if not produto:
            print('\nProduto não encontrado no sistema.')
            return

        return produto
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def selecionar_produto(produto):
    qtde_produto = validar_qtde_produto(produto)
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'UPDATE mercado_at.produto SET quantidade = %s WHERE id_produto = %s;'
        cursor.execute(query, (qtde_produto, produto[0]))
        conn.commit()
        validar_texto_qtde(qtde_produto, produto)
        return qtde_produto
    except Error as e:
        print(f'\nErro na seleção de quantidade do produto: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def incluir_item(qtde_produto, compra, produto):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'INSERT INTO mercado_at.item (quantidade, id_compra, id_produto) VALUES (%s, %s, %s);'
        cursor.execute(query, (qtde_produto, compra[0], produto[0]))
        conn.commit()
        print(f'\nUm novo registro de item foi gerado automaticamente pelo sistema.')
    except Error as e:
        print(f'\nErro na inserção dos dados de item: {e}.')
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
        item = cursor.fetchone()
        return item
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_qtde_items():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT COUNT(id_item) FROM mercado_at.item;'
        cursor.execute(query)
        qtde_items = cursor.fetchone
        return qtde_items
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()