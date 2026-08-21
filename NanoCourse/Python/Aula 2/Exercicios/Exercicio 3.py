voto1 = input("Qual premio deseja ganhar: PLAYSTATION, XBOX OU NINTENDO: ")
voto2 = input("Qual premio deseja ganhar: PLAYSTATION, XBOX OU NINTENDO: ")
voto3 = input("Qual premio deseja ganhar: PLAYSTATION, XBOX OU NINTENDO: ")
voto4 = input("Qual premio deseja ganhar: PLAYSTATION, XBOX OU NINTENDO: ")
voto5 = input("Qual premio deseja ganhar: PLAYSTATION, XBOX OU NINTENDO: ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 1 digitou um console inexiste e seu voto será cancelado.")

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 2 digitou um console inexiste e seu voto será cancelado.")

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 3 digitou um console inexiste e seu voto será cancelado.")

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 4 digitou um console inexiste e seu voto será cancelado.")

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 5 digitou um console inexiste e seu voto foi cancelado.")

print(f"Playstation: {playstation}\nXBOX: {xbox}\nNINTENDO: {nintendo}")

if playstation > xbox and playstation > nintendo:
    print("O Console escolhido foi PLAYSTATION")
elif xbox > playstation and xbox > nintendo:
    print ("O console escolhido foi XBOX")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi NINTENDO")
else:
    print("Houve um empate, porfavor entrar em contato com o suporte")

