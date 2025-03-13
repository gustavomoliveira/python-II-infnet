from util import *
from models import Conta

def consultar_contas(contas):
    for conta in contas:
        print(conta)

def consultar_conta(contas):
    id = entrar_id()
    conta = procurar_conta(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    print(conta)

def incluir_conta(contas):
    id = entrar_id()
    conta = procurar_conta(contas, id)
    if (conta):
        print("Erro: conta já existe")
        return
    nome = entrar_nome()
    saldo = entrar_saldo()
    contas.append(Conta(id, nome, saldo))

def excluir_conta(contas):
    id = entrar_id()
    conta = procurar_conta(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    contas.remove(conta)

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

def alterar_conta(contas):
    id = entrar_id()
    conta = procurar_conta(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    oper = entrar_operacao()
    valor = entrar_valor()
    if (oper == "C"):
        conta.creditar(valor)
    else:
        conta.debitar(valor)