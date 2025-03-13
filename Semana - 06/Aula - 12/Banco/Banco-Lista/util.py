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

def procurar_conta(contas, id):
    '''
        Procurar conta na lista de contas
        Parâmetros:
            contas: lista de contas
            id: conta a ser procurada
        Retorna:
            Uma conta se encontrada ou [] se não encontrada
    '''
    conta_procurada = []
    for conta in contas:
        if (conta[0] == id):
            conta_procurada = conta
            break
    return conta_procurada
