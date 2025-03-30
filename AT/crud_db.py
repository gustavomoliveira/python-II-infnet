from mysql.connector import Error
from conectar_bd import *
from validacoes import *

def consultar_dados_inseridos():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = f'SELECT COUNT(*) FROM mercado_at.produto;'
        cursor.execute(query)
        resultado = cursor.fetchone()
        if resultado[0] > 0:
            return True
        else:
            return False
    except Error as e:
        print(f'Erro ao verificar existência de dados: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_cliente(id):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.cliente WHERE id_cliente = %s;'
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()
        if cliente:
            return cliente
        else:
            print('\nCliente não encontrado no sistema.')
            return False
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def incluir_cliente(nome):
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
        print(f'\nERRO: Não foi possível inserir os dados {e}.')
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

def consultar_produto(id):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.produto WHERE id_produto = %s;'
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
        query = 'SELECT * FROM mercado_at.produto WHERE nome = %s;'
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
        query = 'SELECT * FROM mercado_at.produto;'
        cursor.execute(query)
        produtos = cursor.fetchall()
        return produtos
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def incluir_produto(produto):
    nome, quantidade, preco = produto[1], produto[2], produto[3]
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'INSERT INTO mercado_at.produto (nome, quantidade, preco) VALUES (%s, %s, %s);'
        cursor.execute(query, (nome, quantidade, preco))
        conn.commit()
        print(f'\nO novo item "{nome}" foi inserido com sucesso no sistema.')
    except Error as e:
        print(f'\nERRO: Não foi possível inserir o produto "{nome}" no sistema: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_estoque_final():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.produto;'
        cursor.execute(query)
        produtos = cursor.fetchall()
        estoque = []
        for produto in produtos:
            estoque.append([produto[1], produto[2]]) 
        return estoque
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def atualizar_produto(produto):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'UPDATE mercado_at.produto SET quantidade = %s WHERE id_produto = %s;'
        cursor.execute(query, (produto[4], produto[0]))
        conn.commit()
    except Error as e:
        print(f'\nERRO: Não foi possível selecionar a quantidade do produto: {e}.')
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
        return qtde_items
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()