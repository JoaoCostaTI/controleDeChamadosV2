from funcoes import *

while True:
    try:
        cabecalho("SISTEMA DE GERENCIAMENTO DE CHAMADOS v1.0")
        resumo('João Costa', 3, 5)
        cabecalho("MENU PRINCIPAL")
        menu()
        op = int(input('Sua opção: '))
        
        if op == 0:
            print('\nSaindo do sistema...')
            break
        elif op == 1:
            cabecalho('LISTA DE CHAMADOS')
            listarChamados()
        elif op == 2:
            cabecalho('REGISTRAR CHAMADO')
            abrirChamado()
        elif op == 3:
            cabecalho('BUSCAR CHAMADO')
        else:
            print('\nOPÇÃO INVÁLIDA! Selecione apenas dentre as disponíveis.')
    except ValueError:
        print('\nERRO! Digite apenas números. ')