#ACELERACAO deltaV sobre deltaT

velocidade1 = float(input("v1 = "))
velocidade2 = float(input("v2 = "))

while    velocidade2 < velocidade1:
    print("Erro: v2 não pode ser menor doque v1")
    velocidade2 = float(input("Digite v2 novamente = "))

deltaV = velocidade2 - velocidade1
print(f"(O delta velocidade é {deltaV:.2f}")

tempo1 = float(input("t1 = "))
tempo2 = float(input("t2 = "))

while tempo2 < tempo1:
    print("Erro: t2 não pode ser menor doque t1")
    tempo2 = float(input("Digite tempo2 novamente"))

deltaT = tempo2 - tempo1
print(f"O delta T é de {deltaT:.2f} segundos")

Aceleracao = deltaV / deltaT
print(f"A aceleração é de {Aceleracao} m/s)")