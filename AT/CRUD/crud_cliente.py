from mysql.connector import Error
from conectar_bd import *
from validacao import *

def consultar_cliente(id):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT * FROM mercado_at.cliente WHERE id_cliente = %s;'
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()
        if not cliente:
            print('\nCliente não encontrado no sistema.')
            return False
        else:
            return cliente
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

def cadastrar_novo_cliente():
    opcao = validar_escolha('\nDeseja cadastrar o cliente no sistema? ([1] - Sim / [2] - Finalizar Atendimento): ')
    if opcao == 2:
        print('\nEncerrando Atendimento ao Cliente.')
        return None

    nome_cliente = validar_nome('\nInsira o nome do cliente a ser cadastrado: ')
    print(f'\n{nome_cliente} cadastrado com sucesso no sistema.')
    return incluir_cliente(nome_cliente)