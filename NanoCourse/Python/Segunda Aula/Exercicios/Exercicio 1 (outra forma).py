print("VERIFICADOR DE FREQUENCIAS CARDIACAS")
idade = int(input("Porfavor, informe a sua idade: "))
bpm = int(input("Porfavor, informe a sua bpm: "))

if idade <= 2:
    if bpm < 120:
        print("Batimentos Abaixo para a idade fornecida.")
    elif 120 <= bpm <= 140:
        print("Batimentos Normais para a idade fornecida.")
    else:
        print("Batimentos Acima para a idade fornecida.")

elif 8 <= idade <= 17:
    if bpm < 80:
        print("Batimentos Abaixo para a idade fornecida.")
    elif 80 <= bpm <= 100:
        print("Batimentos Normais para a idade fornecida.")
    else:
        print("Batimentos Acima para a idade fornecida.")

elif 18 <= idade <= 59:
    if bpm < 70:
        print("Batimentos Abaixo para a idade fornecida.")
    elif 70 <= bpm <= 80:
        print("Batimentos Normais para a idade fornecida.")
    else:
        print("Batimentos Acima para a idade fornecida.")

elif idade >= 60:
    if bpm < 50:
        print("Batimentos Abaixo para a idade fornecida.")
    elif 50 <= bpm <= 60:
        print("Batimentos Normais para a idade fornecida.")
    else:
        print("Batimentos Acima para a idade fornecida.")