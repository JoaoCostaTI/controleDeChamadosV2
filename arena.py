CHAMADOS = {
    "1001": {
        "solicitante": "JOÃO",
        "setor": "INFORMÁTICA",
        "data": "12/9/2025 - 10:42",
        "descricao": "cabo de rede pc",
        "status": "Aberto",
        'obs': 'Cabo de 3m solicitado ao estoque.'
    },
    "1002": {
        "solicitante": "MARIA",
        "setor": "FINANCEIRO",
        "data": "12/9/2025 - 11:05",
        "descricao": "erro ao acessar sistema bancário",
        "status": "Aberto"
    },
    "1003": {
        "solicitante": "CARLOS",
        "setor": "VENDAS",
        "data": "15/9/2025 - 09:15",
        "descricao": "instalação de impressora HP no notebook",
        "status": "Em Andamento",
        "obs": "Técnico Marcos a caminho do local."
    },
    "1004": {
        "solicitante": "ANA",
        "setor": "RECURSOS HUMANOS",
        "data": "15/9/2025 - 10:30",
        "descricao": "mouse sem fio não conecta",
        "status": "Aberto"
    },
    "1005": {
        "solicitante": "PEDRO",
        "setor": "LOGÍSTICA",
        "data": "16/9/2025 - 08:55",
        "descricao": "solicitação de acesso à pasta 'Compartilhado'",
        "status": "Em Andamento",
        "obs": "Aguardando aprovação do gestor da área."
    },
    "1006": {
        "solicitante": "SOFIA",
        "setor": "MARKETING",
        "data": "16/9/2025 - 11:21",
        "descricao": "problema com lentidão no sistema ERP",
        "status": "Aberto"
    },
    "1007": {
        "solicitante": "LUCAS",
        "setor": "VENDAS",
        "data": "16/9/2025 - 14:02",
        "descricao": "troca de toner da impressora do setor",
        "status": "Em Andamento",
        "obs": "Toner modelo XYZ-123 solicitado ao almoxarifado."
    },
    "1008": {
        "solicitante": "FERNANDA",
        "setor": "FINANCEIRO",
        "data": "17/9/2025 - 09:01",
        "descricao": "planilha do Excel corrompida",
        "status": "Aberto"
    },
    "1009": {
        "solicitante": "RAFAEL",
        "setor": "DIRETORIA",
        "data": "17/9/2025 - 10:18",
        "descricao": "ajuda com configuração de e-mail no celular",
        "status": "Em Andamento",
        "obs": "Agendado atendimento remoto para as 15:00."
    },
    "1010": {
        "solicitante": "JULIANA",
        "setor": "PRODUÇÃO",
        "data": "17/9/2025 - 11:45",
        "descricao": "computador reiniciando sozinho",
        "status": "Aberto"
    },
    "1011": {
        "solicitante": "TIAGO",
        "setor": "INFORMÁTICA",
        "data": "17/9/2025 - 15:10",
        "descricao": "monitor secundário não dá vídeo",
        "status": "Aberto"
    },
    "1012": {
        "solicitante": "CAMILA",
        "setor": "RECURSOS HUMANOS",
        "data": "17/9/2025 - 16:05",
        "descricao": "criação de novo usuário de rede para estagiário",
        "status": "Em Andamento",
        "obs": "Aguardando dados completos do novo colaborador."
    }
}
chamadosAbertos = 0
chamadosEmAndamento = 0
for chamado in CHAMADOS.values():
    if chamado['status'] == "Aberto":
        chamadosAbertos += 1
    if chamado["status"] == "Em Andamento":
        chamadosEmAndamento += 1
print(chamadosEmAndamento)
print(chamadosAbertos)