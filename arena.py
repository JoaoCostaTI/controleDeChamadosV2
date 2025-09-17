CHAMADOS = {
    "1001": {
        "solicitante": "JOÃO",
        "setor": "INFORMÁTICA",
        "data": "12/9/2025 - 10:42",
        "descricao": "cabo de rede pc",
        "status": "Aberto",
        'obs': 'QUALQUER COISA AQ'
    },
    "1002": {
        "solicitante": "MARIA",
        "setor": "FINANCEIRO",
        "data": "12/9/2025 - 11:05",
        "descricao": "erro ao acessar sistema bancário",
        "status": "Aberto"
    }
}
if CHAMADOS['1002']['obs']:
    print('chegou aq')
print(CHAMADOS['1001'])