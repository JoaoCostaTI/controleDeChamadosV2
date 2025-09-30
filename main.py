from funcoes import *

while True:
    try:
        limparTela()
        cabecalho("SISTEMA DE GERENCIAMENTO DE CHAMADOS v1.0")
        resumo('João Costa')
        cabecalho("MENU PRINCIPAL")
        menu()
        op = int(input('Sua opção: '))
        
        if op == 0:
            print('\nSaindo do sistema...')
            sleep(0.9)
            break
        elif op == 1:
            abrirChamado()
        elif op == 2:
            listarChamados() 
        elif op == 3:
            buscarChamado()
        elif op == 4:
            atividadesExtras()
        else:
            limparTela()
            print('\nOPÇÃO INVÁLIDA! Selecione apenas dentre as disponíveis.')
    except ValueError:
        limparTela()
        print('\nERRO! Digite apenas números. ')
        