from datetime import datetime
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

def validar_disponibilidade_produto(produtos):
    while True:
        id_produto = validar_inteiro('\nInsira o ID do produto para consultar sua disponibilidade em estoque: ')
        
        produto_encontrado = False
        
        for produto in produtos:
            if id_produto == produto[0]:
                produto_encontrado = True
                estoque_disponivel = produto[2] if len(produto) == 4 else produto[4]
                
                if estoque_disponivel > 0:
                    print(f'\n{produto[1]} encontrado! Quantidade: {estoque_disponivel} | Preço: R$ {produto[3]}.')
                    return produto
                else:
                    print(f'\n{produto[1]} encontrado, porém não existe estoque disponível no momento.')
                    return None
        
        if not produto_encontrado:
            print('\nProduto não encontrado.')
            opcao = validar_escolha('\nDeseja cadastrar o produto no sistema? ([1] - Sim / [2] - Não): ')
            
            if opcao == 2:
                print('\nEncerrando o cadastro de um novo produto.')
                return None
            
            nome = validar_nome('\nInsira o nome do produto a ser cadastrado: ')
            quantidade = validar_quantidade('\nInsira a quantidade do produto a ser cadastrado: ')
            preco = validar_preco('\nInsira o preço do produto a ser cadastrado: ')
            
            novo_produto = (-1, nome, quantidade, preco)
            print(f'\nProduto "{nome}" cadastrado com sucesso! Quantidade: {quantidade} | Preço: R$ {preco:.1f}')
            return novo_produto
        
def validar_qtde_produto(quantidade, produto):
    estoque_disponivel = produto[2] if len(produto) == 4 else produto[4]

    if quantidade > estoque_disponivel:
        print(f'\nQuantidade selecionada é maior que o estoque disponível.')
        print(f'\nQuantidade disponível em estoque: {estoque_disponivel}')
        return False, None
    else:
        validar_texto_qtde(quantidade, produto)
        return estoque_disponivel - quantidade, quantidade
        
def validar_texto_qtde(qtde, produto):
    if qtde == 1:
        print(f'\n{qtde} unidade do {produto[1]} adicionada com sucesso a lista de itens.')
    else:
        print(f'\n{qtde} unidades do {produto[1]} adicionadas com sucesso a lista de itens.')
        
def validar_data_hora():
    data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M')
    return data_hora_atual
    