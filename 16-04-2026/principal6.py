# ciclo principal

while True:
    # dados de entrada
    interruptor_A = 0 # luz_acende
    interruptor_B = 1 # luz_apaga
    interruptor_C = 0 # luz_acende
    interruptor_D = 1 # luz_apaga

    # processamento
    if interruptor_A == 0 and interruptor_B == 0 and interruptor_C == 0 and interruptor_D == 0:
        luz_acende = True
    else:
        luz_acende = False