from util import *

def exibir_menu():
    print("\n**** Menu ****")
    print("[1] - Incluir")
    print("[2] - Alterar")
    print("[3] - Excluir")
    print("[4] - Consultar contas")
    print("[5] - Consultar conta")
    print("[0] - Sair")

def entrar_opcao():
    while (True):
        exibir_menu()
        opcao = entrar_inteiro("Entre com a opção: ")
        if ((opcao < 0) or (opcao > 5)):
            print("Erro: opção inválida")
        else:
            break
    return opcao
