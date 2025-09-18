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
            break
        elif op == 1:
            listarChamados()
        elif op == 2:
            abrirChamado()
        elif op == 3:
            limparTela()
            cabecalho('BUSCAR CHAMADO')
        else:
            limparTela()
            print('\nOPÇÃO INVÁLIDA! Selecione apenas dentre as disponíveis.')
    except ValueError:
        limparTela()
        print('\nERRO! Digite apenas números. ')
        