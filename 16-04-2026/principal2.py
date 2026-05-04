# Exercicio: 2 janelas

# loop principal
while True:
    # dados de entrada
    # janela com valores em percentagem
    janela1 = 50 # o valor pode ir de 0% a 100%
    janela2 = 40 # o valor pode ir de 0% a 100%

    # janela > 10 significa que quero verificar
    # se a sanela não está totalmento fechada
    if janela1 > 10 and janela1 < 90:
        print("janela 1 ok")
    else:
        print("janela 1 Erro")

    # janela 2
    if janela2 > 10 and janela2 < 90:
        print("janela 2 Erro")    
    else:
        print("janela 2 Erro")                