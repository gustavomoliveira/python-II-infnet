def entrar_inteiro(msg):
    while (True):
        try:
            num = int(input(msg))
            break
        except:
            print("Erro: valor inválido")
    return num

def entrar_id():
    while (True):
        id = entrar_inteiro("Entre com o id da conta: ")
        if (id <= 0):
            print("Erro: id inválido")
        else:
            break
    return id

def entrar_nome():
    while (True):
        nome = input("Entre com o nome: ")
        if (len(nome) < 4):
            print("Erro: nome inválido")
        else:
            break
    return nome

def entrar_saldo():
    while (True):
        saldo = float(input("Entre com o saldo: "))
        if (saldo < 0):
            print("Erro: saldo menor que zero")
        else:
            break
    return saldo

def procurar_conta_2(contas, id):
    achou = False
    for conta in contas:
        if (conta[0] == id):
            achou = True
            break
    return achou

def entrar_operacao():
    while (True):
        oper = input("[C]rédito ou [D]ébito: ").upper()
        if (oper not in ("C", "D")):
            print("Erro: operação inválida")
        else:
            break
    return oper

def entrar_valor():
    while (True):
        valor = float(input("Entre com o valor: "))
        if (valor <= 0):
            print("Erro: valor inválido")
        else:
            break
    return valor