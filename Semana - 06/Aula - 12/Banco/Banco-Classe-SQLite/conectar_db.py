import sqlite3
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
BANCO = str(DIR_CUR) + "\\banco.db"

def conectar():
    try:
        conn = sqlite3.connect(BANCO)
    except Exception as ex:
        print(ex)
    return conn

def desconectar(conn):
    if (not conn):
        conn.close()
