inimigos = [(10, 5), (30, 3), (1, 50)]

while len(inimigos) > 0:
    x = int(input("Informe um valor para o eixo X: "))
    y = int(input("Informe um valor para o eixo Y: "))

    if (x,y) in inimigos:
        print("Voce acertou um inimigo")
        inimigos.remove((x,y))
    else:
        print("Voce errou")

    print(f"Agora restam {len(inimigos)} no mapa")
