from datetime import datetime

def validar_inteiro(msg):
    while True:
        try:
            inteiro = int(input(msg))
            if inteiro > 0:
                return inteiro
            else:
                print(f'\ERRO: Valor inserido "{inteiro}" é inválido.')
        except ValueError:
            print('\nERRO: Digite um número inteiro para o ID.')

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

def validar_data_hora():
    data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M')
    return data_hora_atual
    