from conectar_db import *
from models import Conta

def incluir_conta_db(conta):
    try:
        session = conectar()
        session.add(conta)
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)        

def consultar_contas_db():
    try:
        session = conectar()
        conta = session.query(Conta).all()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return conta

def consultar_conta_db(id):
    try:
        session = conectar()
        conta = session.query(Conta).get(id)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return conta

def alterar_conta_db(conta):
    try:
        session = conectar()
        session.query(Conta).filter(Conta.id == conta.id).update({"saldo": conta.saldo}) # busca a conta que será alterada (id) e faz um update com um dicionário
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def excluir_conta_db(conta):
    try:
        session = conectar()
        session.delete(conta)
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)