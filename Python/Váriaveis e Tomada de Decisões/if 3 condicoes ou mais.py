pontuacao = int(input("Porfavor, informe a pontuação do usuário: "))
if pontuacao >= 1000:
    print("Voce recebeu 3gb de bonus")
elif pontuacao >=500:
    print("Voce recebeu 1,5gb de bonus")
elif pontuacao >=200:
    print("Voce recebeu 500mb de bonus")
else:
    print("Voce recebeu nenhum bonus")