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

def validar_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            if 0 <= opcao <= 2:
                return opcao
            else:
                print('\nERRO: Opção inválida. Escolha uma das opções de atendimento.\n')
        except ValueError:
            print('\nERRO: Digite entre 0 a 2 para selecionar uma opção.\n')

def validar_nome(msg):
    while True:
        try:
            padrao = r'^[A-Za-z]{7} \d+$'
            nome = input(msg).title()
            if bool(re.fullmatch(padrao, nome)):
                return nome
            else:
                print(f'\nERRO: O nome inserido deve seguir o padrão do exemplo abaixo:')
                print(f'\n"abcdefg 1" --> 7 letras, 1 espaço, N números.')
        except ValueError:
            print('\nERRO: Digite um nome válido.')

def validar_quantidade(msg):
    while True:
        try:
            quantidade = int(input(msg))
            if quantidade > 0:
                return quantidade
            else:
                print('\nERRO: A quantidade cadastrada deve ser maior que 0.\n')
        except ValueError:
            print('\nERRO: Digite uma quantidade válida.\n')

def validar_preco(msg):
     while True:
        try:
            preco = float(input(msg))
            if preco > 0:
                return preco
            else:
                print('\nERRO: A quantidade cadastrada deve ser maior que 0.\n')
        except ValueError:
            print('\nERRO: Digite uma quantidade válida.\n')


def validar_texto_qtde(qtde, produto):
    if qtde == 1:
        print(f'\n{qtde} unidade do {produto[1]} adicionada com sucesso a lista de itens.')
    else:
        print(f'\n{qtde} unidades do {produto[1]} adicionadas com sucesso a lista de itens.')

def validar_qtde_produto(quantidade, produto):
    estoque_disponivel = produto[2] if len(produto) == 4 else produto[4]

    if quantidade > estoque_disponivel:
        print(f'\nQuantidade selecionada é maior que o estoque disponível.')
        print(f'\nQuantidade disponível em estoque: {estoque_disponivel}')
        return False, None
    else:
        validar_texto_qtde(quantidade, produto)
        return estoque_disponivel - quantidade, quantidade
        
def consultar_estoque(produto): 
    if produto[2] > 0:
        print(f'\nProduto encontrado: {produto[1]} | ID para consulta: {produto[0]} | Quantidade em estoque: {produto[2]} | Preço: R$ {produto[3]}.')
        return True
    else:
        print(f'\nO produto pesquisado, "{produto[1]}", não possui disponibilidade em estoque.')
        return False
        
def validar_data_hora():
    data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M')
    return data_hora_atual
    