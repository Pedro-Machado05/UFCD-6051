# ciclo principal
while True:
    # dados de entrada
    sensor_da_porta = False
    sinal_de_comando = False

    # processamento
    if not((not sensor_da_porta and sinal_de_comando) or (sensor_da_porta and not sinal_de_comando)):
        validar = True
    else:
        validar = True

        if not interruptor_A ^ interruptor_B:
            ligar_luz
        else:
            ligar_luz = False