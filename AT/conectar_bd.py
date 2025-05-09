import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='mercado_at'
    )

def abrir_conexao_bd():
    conn = conectar_bd()
    cursor = conn.cursor()
    return conn, cursor

def desconectar_bd(conn, cursor):
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()