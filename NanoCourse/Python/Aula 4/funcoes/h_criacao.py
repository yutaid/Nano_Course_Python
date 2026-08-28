def velocidade_media():
    distancia = float(input("Distancia pecorrida em km: "))
    tempo = float(input("Tempo utilizado na viagem em h: "))
    vm = distancia / tempo
    print(f"A velocidade media foi de {vm}km/h")

velocidade_media()