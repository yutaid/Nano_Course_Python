quantidade_alimentos = int(input("Quantidade de alimentos: "))
total_calorias = 0
for alimento in range(1, quantidade_alimentos + 1, 1):
    caloria = int(input(f"Calorias do {alimento}: "))
    total_calorias = total_calorias + caloria
print(f"{total_calorias} é o total de calorias consumidas")
