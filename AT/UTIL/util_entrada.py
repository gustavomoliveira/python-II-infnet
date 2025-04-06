import re

def validar_inteiro(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor > 0:
                return valor
            else:
                print(f'\nERRO: O valor "{valor}" é inválido. Digite um número maior que zero.')
        except ValueError:
            print('\nERRO: Digite apenas números inteiros positivos.')

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
            print('\nERRO: Digite um número inteiro (1 ou 2).')

def validar_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            if 0 <= opcao <= 2:
                return opcao
            else:
                print('\nERRO: Opção inválida. Escolha uma das opções de atendimento (0 a 2).')
        except ValueError:
            print('\nERRO: Digite um número entre 0 e 2 para selecionar uma opção.')

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
                print('\nERRO: A quantidade cadastrada deve ser maior que 0.')
        except ValueError:
            print('\nERRO: Digite um número inteiro positivo.')

def validar_preco(msg):
     while True:
        try:
            preco = float(input(msg))
            if preco > 0:
                return preco
            else:
                print('\nERRO: O preço cadastrado deve ser maior que 0.')
        except ValueError:
            print('\nERRO: O preço deve ser um número.')