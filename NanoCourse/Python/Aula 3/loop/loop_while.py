reposta = ""
tentativa = 0
while reposta != "42":
    reposta = input("Qual é a respota da vida, do universo e tudo mais: ")
    tentativa = tentativa + 1
print("Parabéns!Voce acertou a resposta!\nNão esqueça a sua toalha")
print(f"O número de tentativas foi {tentativa}")