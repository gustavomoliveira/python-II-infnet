from conectar_bd import *

def importar_dados_iniciais_bd(df, query):
    conn, cursor = None, None
    try:
        conn, cursor = abrir_conexao_bd()
        df = df.iloc[:, 1:]
        dados = [tuple(valores) for valores in df.values]
        cursor.executemany(query, dados)
        conn.commit()
        print(f"\nDados importados com sucesso! ({len(dados)} registros)")
        return True
    except Exception as ex:
        print(f'\nERRO: Os dados não puderam ser inseridos: {ex}.')
        return False
    finally:
        desconectar_bd(conn, cursor)