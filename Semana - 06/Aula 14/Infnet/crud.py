from models import *
from conectar_db import *

def inserir_alunos():
    session = conectar()
    try:
        aluno = Aluno('Bartô')
        session.add(aluno)
        aluno = Aluno('Mari')
        aluno.endereco = Endereco('Rua da Mari')
        aluno.emails = [Email('mari@email.com')]
        session.add(aluno)
        aluno = Aluno('Gustavo')
        aluno.endereco = Endereco('Rua do Gustavo')
        aluno.emails = [Email('gustavo@email.com'), Email('gustavo@outromail.com')]
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
            if aluno.endereco:
                print(aluno.endereco)
            for email in aluno.emails:
                print(email)
            for disciplina in aluno.disciplinas:
                print(disciplina)
    except Exception as ex:
        print(f'Erro ao conectar: {ex}.')
    finally:
        desconectar(session)

def incluir_disciplinas():
    session = conectar()
    try:
       session.add(Disciplina('SQL', 40))
       session.add(Disciplina('Python', 40))
       session.add(Disciplina('PB - Fundamento de Dados', 20))
       session.commit()
    except Exception as ex:
        print(f'Erro ao conectar: {ex}.')
    finally:
        desconectar(session)

def incluir_aluno_disciplina():
    session = conectar()
    try:
        session.add(AlunoDisciplina(2, 1))
        session.add(AlunoDisciplina(3, 1))
        session.add(AlunoDisciplina(3, 2))
    except Exception as ex:
        print(f'Erro ao conectar: {ex}.')
    finally:
        desconectar(session)