import requests
from config import Config
from datetime import date

headers={"access-token":Config.API_PAG_KEY}

def id_cliente_api_pagamento(nome, cpfCnpj):
    resposta=requests.post(f"{Config.API_PAG_LINK}/customers",json={'name':nome,'cpfCnpj':cpfCnpj},headers=headers,timeout=30)
    resposta.raise_for_status()
    dados=resposta.json()
    return dados["id"]

def gerar_pagamento(id_cliente,valor,tipo):
    resposta=requests.post(f"{Config.API_PAG_LINK}/payments", json={"customer":id_cliente,"billingType":tipo,"value":float(valor),"dueDate":date.today().isoformat()},headers=headers,timeout=30)
    resposta.raise_for_status()
    dados=resposta.json()
    return dados["id"]

def pegar_boleto(id_pagamento):
    pagamento=requests.get(f"{Config.API_PAG_LINK}/payments/{id_pagamento}",headers=headers,timeout=30)
    pagamento.raise_for_status()
    dados=pagamento.json()
    return dados.get("bankSlipUrl")
        
def pegar_pix(id_pagamento):
    pagamento=requests.get(f"{Config.API_PAG_LINK}/payments/{id_pagamento}/pixQrCode",headers=headers,timeout=30)
    pagamento.raise_for_status()
    qr=pagamento.json()
    
    return {
    "id_pagamento":id_pagamento,"qrCode":qr.get("encodedImage"),"chave":qr.get("payload"),"expira_em":qr.get("expirationDate")
    }

def consultar_pagamentos(pagamento):
    resultado=requests.get(f"{Config.API_PAG_LINK}/payments/{pagamento.id_pagamento}",headers=headers,timeout=30)
    resultado.raise_for_status()
    
    dados=resultado.json()
        
    return dados["status"]