def velocidade_media(distancia, tempo):
    vm = distancia / tempo
    print(f"A velocidade media foi de {vm}km/h")

distancia = float(input("Distancia em km: "))
tempo = float(input("Tempo em horas: "))
velocidade_media(distancia, tempo)