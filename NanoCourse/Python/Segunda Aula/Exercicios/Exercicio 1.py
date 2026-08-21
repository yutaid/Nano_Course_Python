print("Verificador de Frequências Cardíacas.")

idade = int(input("Por favor, informe a sua idade: "))
bpm = int(input("Por favor, informe a sua bpm: "))

if idade <= 2:
    if bpm >= 120:
        if bpm <= 140:
            print("Batimentos Normais para a idade fornecida.")
        else:
            print("Batimentos Acima para a idade fornecida.")
    else:
        print("Batimentos Abaixo para a idade fornecida.")
elif idade >=8:
    if idade <=17:
        if bpm >= 80:
            if bpm <= 100:
                print("Batimentos Normais para a idade fornecida.")
            else:
                print("Batimentos Acima para idade fornecida")
        else:
            print("Batimentos Abaixo para a idade fornecida")
    if idade >= 18:
        if idade <= 59:
            if bpm >= 70:
                if bpm <=80:
                    print("Batimentos Normais para a idade fornecida")
                else:
                    print("Batimentos Acima para a idade fornecida")
            else:
                print("Batimentos Abaixo para a idade fornecida")
        else:
            if bpm >= 50:
                if bpm <= 60:
                    print("Batimentos Normais para a idade fornecida")
                else:
                    print("Batimentos Acima para a idade fornecida")
            else:
                print("Batimentos Abaixo para a idade fornecida")
else:
    print("Não foi possível verificar os batimentos cardíacos para essa idade")


