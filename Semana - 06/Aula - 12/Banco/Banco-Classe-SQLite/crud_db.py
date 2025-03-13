from conectar_db import *
from models import Conta

def incluir_conta_db(conta):
    comando = "insert into contas (nome, saldo) values (?, ?);"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (conta.nome, conta.saldo))
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)        

def consultar_contas_db():
    comando = "select * from contas;"
    contas = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        registros = cursor.fetchall()
        for registro in registros:
            conta = Conta(registro[0], registro[1], registro[2])
            contas.append(conta)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return contas

def consultar_conta_db(id):
    comando = "select * from contas where id = ?;"
    conta = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (id,))
        registro = cursor.fetchall()
        if (registro):
            conta = Conta(registro[0][0], registro[0][1], registro[0][2])
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return conta

def alterar_conta_db(conta):
    comando = "update contas set saldo = ? where id = ?;"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (conta.saldo, conta.id))
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)

def excluir_conta_db(id):
    comando = "delete from contas where id = ?;"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (id,))
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)