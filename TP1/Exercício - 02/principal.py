from crud import *
from utilitario import *
    
def iniciar_programa():
    projeto_1 = {'F1', 'F2', 'F3', 'F4'}
    projeto_2 = {'F1', 'F5', 'F3', 'F6'}
    while True:
        opcao = menu_principal()
        match opcao:
            case 1:
                inserir_funcionario(projeto_1, projeto_2)
            case 2:
                verificar_duplicatas(projeto_1, projeto_2)
            case 3:
                executar_submenu(projeto_1, projeto_2)
            case 4:
                excluir_funcionario(projeto_1, projeto_2)
            case 0:
                print('\nPrograma encerrado.\n')
                break
            case _:
                print('\nERRO: Opção inválida.')

if __name__ == '__main__':           
    iniciar_programa()
