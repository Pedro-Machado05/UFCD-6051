quadro_eletrico = {
    "corte_geral": {
        "in": 32,  # corrente nominal (A)
        "tipo": "magnetotermico",
        "curva": "C",
        "poder_corte": "6kA"
    },

    "protecao": {
        "diferencial": {
            "in": 40,
            "sensibilidade": "30mA",
            "tipo": "A"
        }
    },

    "circuitos": [
        {
            "nome": "iluminacao",
            "disjuntor1": {
                "in": 10,
                "curva": "B"
            },
            "cabo": "1.5mm2"
        },
        {
            "nome": "tomadas",
            "disjuntor2": {
                "in": 16,
                "curva": "C"
            },
            "cabo": "2.5mm2"
        },
        {
            "nome": "equipamento",
            "disjuntor3": {
                "in": 20,
                "curva": "C"
            },
            "cabo": "2.5mm2"
        }
    ],

    "barramentos": {
        "fase": True,
        "neutro": True,
        "terra": True
    }
}

import minhas_funcoes

corrente_de_cada_lampadas =["potencial"] / lampadas["tensao"]
print(corrente_de_cada_lampadas)

corrente_de_todas_as_lampadas = corrente_de_cada_lampadas *lampadas["quantidade"]
print(corrente_de_todas_as_lampadas)

def calcular_corrente(potencia, tensao):
    corrente = potencia / tensao
    return corrente

corrente_de_todas_as_lampadas = corrente_de_cada_lampada * lampadas["quantidade"]
corrente_de_todas_as_lampadas

minhas_funcoes.selecionar_disjuntor