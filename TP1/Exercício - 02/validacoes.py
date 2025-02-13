import re

def validar_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            if 0 <= opcao <= 4:
                return opcao
            else:
                print('\nERRO: Opção inválida. Escolha uma das opções do Menu.')
        except ValueError:
            print('\nERRO: Digite um número entre 0 e 4 no Menu.')

def validar_nome(msg):
    while True:
        nome = input(msg).upper()
        padrao_nome = r'^F\d{1}$'
        resultado_nome = bool(re.fullmatch(padrao_nome, nome))
        if resultado_nome:
            return nome
        else:
            print(f'\nERRO: O nome digitado não segue o padrão "F#" para nomes de funcionários.')
            print(f'\nExemplos de nomes aceitos: F1, F2 ou F9, por exemplo. Sempre F seguido de um número inteiro.')

def validar_projeto(msg):
    while True:
        try:
            projeto = int(input(msg))
            if projeto in (1, 2):
                return projeto
            else:
                print(f'\nERRO: Digite [1] para o Projeto 1 e [2] para o Projeto 2.')
        except ValueError:
            print('\nERRO: Escolha uma opção válida.')

