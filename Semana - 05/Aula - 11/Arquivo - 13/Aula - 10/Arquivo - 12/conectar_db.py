from sqlalchemy import create_engine

BANCO = 'turma'

def conectar():
    try:
        engine = create_engine('mysql+pymysql://root:@127.0.0.1/' + BANCO, echo=True) # echo -> todo acesso feito no banco a tela é printada, usado pra debug
        engine.connect()
        print('Banco conectado.')
    except Exception as ex:
        print(f'Erro ao conectar o banco: {ex}.')
        exit()
    return engine

def desconectar(engine):
    if engine:
        engine.dispose()