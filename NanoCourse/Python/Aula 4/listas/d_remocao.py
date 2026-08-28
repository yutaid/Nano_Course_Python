duelistas = ["jett", "raze", "waylay", "neon", "iso", "omen", "reyna", "yoru"]

#REMOCAO DO ULTIMO VALOR

duelistas.pop(-1)
print(duelistas)

#REMOCAO DE UM VALOR EM POSICAO ESPECIFICA

duelistas.pop(1)
print(duelistas)

#REMOCAO DE UM VALOR ESPECIFICO

print(duelistas)
while True:
    alvo = input("Insira um nome de agente que não é duelista: ")
    if alvo == "omen":
        print("Este agente realmente não é um duelista")
        duelistas.remove("omen")
        break
    elif alvo in duelistas:
        print("Este agente é um duelista.Tente novamente!")
    else:
        print("Este não se categoriza como um dos citados na lista")
print(duelistas)

#APAGAR A LISTA TODA

duelistas.clear()
print(duelistas)

