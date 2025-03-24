from datetime import datetime
import re

def validar_inteiro(msg):
    while True:
        try:
            inteiro = int(input(msg))
            if inteiro > 0:
                return inteiro
            else:
                print(f'\nERRO: Valor inserido "{inteiro}" é inválido.')
        except ValueError:
            print('\nERRO: Digite um número inteiro maior que 0.')

def validar_escolha(msg):
    while True:
        try:
            escolha = int(input(msg))
            if escolha in (1, 2):
                return escolha
            else:
                print(f'\nERRO: Valor inserido "{escolha}" é inválido.')
                print('\nSelecione "1" para "Sim" ou "2" para "Não".')
        except ValueError:
            print('\nERRO: Digite um número inteiro.')

def validar_nome_cliente(msg):
    while True:
        try:
            padrao = r'^[A-Za-z]{7} \d+$'
            nome = input(msg).title()
            if bool(re.fullmatch(padrao, nome)):
                return nome
            else:
                print(f'\nERRO: O nome inserido deve seguir o padrão do exemplo abaixo:')
                print(f'\n"Cliente 1" --> 7 letras, 1 espaço, N números.')
        except ValueError:
            print('\nERRO: Digite um nome válido.')

def validar_qtde_produto(produto):
    while True:
        quantidade = validar_inteiro(f'\nDigite a quantidade do {produto[1]} desejada: ')
        if quantidade > produto[2]:
            print(f'\nQuantidade selecionada é maior que o estoque disponível.')
            print(f'\nQuantidade disponível em estoque: {produto[2]}')      
        else:
            return produto[2] - quantidade
        
def consultar_estoque(produto):
    if produto[2] > 0:
        print(f'\nProduto encontrado: {produto[1]} | Quantidade em estoque: {produto[2]} | Preço: R$ {produto[3]}.')
    else:
        print(f'\nO produto pesquisado, "{produto[1]}", não possui disponibilidade em estoque.')

def validar_texto_qtde(qtde_produto, produto):
    if qtde_produto == 1:
        print(f'\n{qtde_produto} unidade do {produto[1]} adicionada com sucesso.')
    else:
        print(f'\n{qtde_produto} unidades do {produto[1]} adicionadas com sucesso.')

def validar_data_hora():
    data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M')
    return data_hora_atual
    