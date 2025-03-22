from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def conectar():
    try:
        engine = create_engine('mysql+pymysql://root:@127.0.0.1/infnet')
        session = sessionmaker(bind=engine)()
        print('Banco de Dados conectado.')
    except Exception as ex:
        print(f'Erro ao conectar no banco: {ex}.')
    return session

def desconectar(session):
    if session:
        session.close()

session = conectar()
desconectar(session)