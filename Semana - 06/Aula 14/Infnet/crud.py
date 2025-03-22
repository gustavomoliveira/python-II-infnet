from models import *
from conectar_db import *

def inserir_alunos():
    session = conectar()
    try:
        aluno = Aluno('Gustavo')
        aluno.endereco = Endereco('Rua do Gustavo')
        session.add(aluno)
        aluno = Aluno('Mari')
        aluno.endereco = Endereco('Rua da Mari')
        session.add(aluno)
        session.commit()
    except Exception as ex:
        print(f'Erro ao conectar: {ex}.')
    finally:
        desconectar(session)

def consultar_alunos():
    session = conectar()
    try:
        alunos = session.query(Aluno).all()
        for aluno in alunos:
            print(aluno)
    except Exception as ex:
        print(f'Erro ao conectar: {ex}.')
    finally:
        desconectar(session)