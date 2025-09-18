import json
import time
import os
from time import sleep

CHAMADOS = {}

#Lógica para gerar ID's dinamicas e sequenciais
def pegarUltimoID():
    ultimoElemento = 0
    if CHAMADOS:
        for id in CHAMADOS:
            ultimoElemento = int(id)
        return ultimoElemento + 1
    else:
        return 1000

try:
    with open('baseDeDados.json', 'r', encoding='utf-8') as arquivo:
        CHAMADOS = json.load(arquivo)
except FileNotFoundError:
    CHAMADOS = {}



def salvarDados():
    with open('baseDeDados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(CHAMADOS, arquivo, ensure_ascii=False, indent=4)

def cabecalho(msg=""):
    tam = 60
    print('=' * tam)
    print(f"{msg.center(tam)}")
    print('=' * tam)

def resumo(user=""):
    chamadosAberto = 0
    chamadosEmAndamento = 0
    chamadosFechado = 0
    for chamado in CHAMADOS.values():
        if chamado['status'] == "Aberto":
            chamadosAberto += 1
        elif chamado['status'] == "Em andamento":
            chamadosEmAndamento += 1
        elif chamado['status'] == 'Fechado':
            chamadosFechado += 1
    print(f'Olá, {user}!\n')
    print('Resumo rápido:')
    print(f"  - {chamadosAberto} chamados ABERTOS.")
    print(f"  - {chamadosEmAndamento} chamados em ANDAMENTO atribuídos a você.")
    print(f'  - {chamadosFechado} chamados CONCLUÍDOS')

def menu():
    print("[1] Ver lista de Chamados\n[2] Criar novo Chamado\n[3] Buscar por um chamado Específico\n[0] Sair do Sistema\n")

def abrirChamado():
    limparTela()
    cabecalho('REGISTRAR CHAMADO')
    solicitante = str(input('Seu nome: ')).strip().upper()
    setor = str(input("Setor: ")).strip().upper()
    descricao = str(input('Detalhamento da solicitação: ')).strip().lower()

    chamadoAtual = {}
    chamadoAtual["solicitante"] = solicitante
    chamadoAtual["setor"] = setor

    #Registrando o horário
    hora = time.localtime()
    dataDoRegistro = f"{hora.tm_mday}/{hora.tm_mon}/{hora.tm_year} - {hora.tm_hour}:{hora.tm_min}"
    chamadoAtual['data'] = dataDoRegistro

    chamadoAtual['descricao'] = descricao
    #Status Inicial
    chamadoAtual['status'] = "Aberto"

    #ID do chamado
    id = pegarUltimoID()
    CHAMADOS[id] = chamadoAtual
    salvarDados()
    print(f"Chamado #{id} Criado com sucesso! ")
    sleep(0.9)

def percorrerChamados(status = ""):
    totalChamados = 0
    if status == "":
        print('-'*85)
        cabecalho('TODOS CHAMADOS')
        print(f"{'ID':<5} | {'Descrição':<40} | {'Solicitante':<15} | {'Status'}")
        print('-'*85)
        for i, c in CHAMADOS.items():
            print(f"{i:<5} | {c['descricao']:<40} | {c['solicitante']:<15} | {c['status']}")
            totalChamados += 1
        print(f"=== Total de chamados: {totalChamados} ===")
        print('-'*85)
        print(f'Digite um ID para ver detalhes | [V]oltar ao menu')
        op = str(input('SUA OPÇÃO: ')).strip().lower()
        if op == "v":
            print('Retornando ao menu anterior...')
            return
        detalhesChamado(op)
        return 
    print('-'*85)
    cabecalho(f'CHAMADOS {status.upper()}')
    print(f"{'ID':<5} | {'Descrição':<40} | {'Solicitante':<15} | {'Status'}")
    print('-'*85)
    for i, c in CHAMADOS.items():
        
        if c['status'] == status:
            print(f"{i:<5} | {c['descricao']:<40} | {c['solicitante']:<15} | {c['status']}")
            totalChamados += 1
    print(f"=== Total de chamados: {totalChamados} ===")
    print('-'*85)
    print(f'Digite um ID para ver detalhes | [V]oltar ao menu')
    op = str(input('SUA OPÇÃO: ')).strip().lower()
    if op == 'v':
        print('Retornando ao menu anterior...')
        return
    detalhesChamado(op)

def atualizarChamado(id = ""):  
    print(f'--- ATUALIZAR CHAMADO #{id} ---')
    print('O que você deseja fazer? ')
    print('[1] - Colocar Em Andamento\n[2] - FECHAR chamado\n[3] - Adicionar histórico (Observações)\n[0] - Cancelar')
    op = int(input('SUA OPÇÃO: '))
    if op == 0:
        print('Voltando ao menu anterior...')
        return
    elif op == 1:
        chamadoAtual = CHAMADOS[id]
        chamadoAtual['status'] = 'Em andamento'
        CHAMADOS[id] = chamadoAtual
        print(f'Alterado com sucesso para {chamadoAtual['status']}...')
        salvarDados()

    elif op == 2:
        chamadoAtual = CHAMADOS[id]
        chamadoAtual['status'] = 'Fechado'
        CHAMADOS[id] = chamadoAtual
        print(f'Alterado com sucesso para {chamadoAtual['status']}...')
        salvarDados()
    elif op == 3:
        chamadoAtual = CHAMADOS[id]
        chamadoAtual['obs'] = str(input('Digite as observações: ')).strip()
        CHAMADOS[id] = chamadoAtual
        print('Adicionado com sucesso...')
        salvarDados()
    else:
        print('Nenhuma opção válida! Tente novamente. ')

def detalhesChamado(id = ""):
    limparTela()
    print('-'*85)
    if id == "" or id not in CHAMADOS:
        print('XXX - Chamado NÃO encontrado... Tente outro. - XXX')
        return
    cabecalho(f"Detalhes do chamado #{id}")
    chamadoDetalhado = CHAMADOS[id]
    print(f"Descrição: {chamadoDetalhado['descricao']}")
    print(f'Solicitante: {chamadoDetalhado['solicitante']}')
    print(f"Setor: {chamadoDetalhado['setor']}")
    print('-'*85)
    print(f"Status: {chamadoDetalhado['status']}")
    print(f"Abertura: {chamadoDetalhado['data']}")
    try: 
        print('-'*85)
        print(f'--- Observações --- \n- {chamadoDetalhado['obs']}')
    except KeyError:
        pass
    print('-'*85)
    print('AÇÕES: [A]tualizar chamado | [V]oltar para a lista')
    print()
    op = str(input('SUA OPÇÃO: ')).strip().lower()
    if op == 'v':
        print('Voltando para a listagem...')
        return
    elif op == 'a':
        atualizarChamado(id)
    else:
        print('XXX - Opção inválida! Tente novamente - XXX')
        sleep(0.8)
        return    
    
def listarChamados():
    while True:
        try:
            limparTela()
            cabecalho('LISTA DE CHAMADOS')
            print('[1] - Abertos\n[2] - Em andamento\n[3] - Fechados\n[4] - Todos\n[0] - Voltar menu ')
            op = int(input('SUA OPÇÃO: '))
            if op == 0:
                print('Voltando menu...')
                break
            elif op == 1:
                limparTela()
                percorrerChamados('Aberto')
            elif op == 2:
                limparTela()
                percorrerChamados('Em andamento')
            elif op == 3:
                limparTela()
                percorrerChamados('Fechado')
            elif op == 4:
                limparTela()
                percorrerChamados("")
            else:
                limparTela()
                print('Nenhuma opção selecionada, tente novamente...')
        except ValueError:
            limparTela()
            print('\nERRO! Digite apenas números. ')

def buscarChamado():
    limparTela()
    cabecalho('BUSCAR CHAMADO')
    id = input('Digite o ID do chamado: ')
    if id in CHAMADOS:
        detalhesChamado(id)
    else:
        print('Chamado não encontrado! Tente outro ID')
        sleep(0.9)

def limparTela():
    os.system('cls')
