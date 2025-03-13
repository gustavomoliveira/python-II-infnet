from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def conectar():
    try:
        engine = create_engine('mysql+pymysql://root:@127.0.0.1/banco', echo=True) # mysql+pymysql indicação de uso dos pacotes para acessar o banco
        session = sessionmaker(bind=engine)() # acessar as atbelas do banco. segundo () é parte da sintaxe, evita que seja criado um objeto session
        print('Banco conectado.')
    except Exception as ex:
        print(ex)
    return session

def desconectar(session):
    if (session):
        session.close()