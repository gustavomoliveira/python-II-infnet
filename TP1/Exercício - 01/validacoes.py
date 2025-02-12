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

def validar_chave(msg):
    while True:
        try:
            chave = int(input(msg))
            return chave
        except ValueError:
            print('\nERRO: Digite um número inteiro para o campo Chave.')

def validar_quantidade(msg):
    while True:
        try:
            quantidade = int(input(msg))
            if quantidade >= 0:
                return quantidade
            else:
                print('\nERRO: A quantidade não pode ser menor do que 0.')
        except ValueError:
            print('\nERRO: Digite o valor referente a operação.')

def validar_preco(msg):
    while True:
        try:
            preco = float(input(msg))
            if preco >= 0:
                return preco
            else:
                print('\nERRO: O preço não pode ser menor do que 0.')
        except ValueError:
            print('\nERRO: Digite o valor referente a operação.')
