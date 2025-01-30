from datetime import datetime

def entrar_produto(produtos):
    id = int(input('Entrar com id do produto: '))
    produto = produtos[id - 1]
    return produto

def entrar_quantidade():
    quantidade = int(input('Entrar com a quantidade: '))
    return quantidade

def exibir_data():
    return datetime.now().strftime('%d/%m/%Y %H:%M')