from crud import *
from menu import *

FIM = 0
opcao = entrar_opcao()
while (opcao != FIM):
    match (opcao):
        case 1: incluir_conta()
        case 2: alterar_conta()
        case 3: excluir_conta()
        case 4: consultar_contas()
        case 5: consultar_conta()
        case _: print("Erro: opção inválida")
    opcao = entrar_opcao()
