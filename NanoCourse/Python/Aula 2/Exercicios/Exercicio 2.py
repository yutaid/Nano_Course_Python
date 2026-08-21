valor_bruto = float(input("Por favor, informe o valor bruto da viagem: "))
categoria = input("Por favorm informe a categora: ECONÔMICA, EXECUTIVA OU PRIMEIRA CLASSE - ")
quantidade_viagantes = int(input("Por favor, informe a quantidade de viagantes: "))
valor_desconto = 0
if categoria.upper() == "ECONÔMICA":
    if quantidade_viagantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidade_viagantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viagantes == 4:
        valor_desconto = valor_bruto * 0.05
elif categoria.upper() == "EXECUTIVA":
    if quantidade_viagantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif quantidade_viagantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidade_viagantes == 4:
        valor_desconto = valor_bruto * 0.08
elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viagantes == 2:
        valor_desconto = valor_bruto * 0.10
    elif quantidade_viagantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidade_viagantes == 4:
        valor_desconto = valor_bruto * 0.20
else:
    print("CATEGORIA INEXISTENTE, PORTANTO NÃO HÁ DESCONTO.")
valor_liquido = valor_bruto - valor_desconto
media_viajante = valor_liquido / quantidade_viagantes
print(f"O valor da viagem é de R${valor_bruto}. Após os descontos de R${valor_liquido}, a viagem custará R${valor_desconto} cada passageiro. Cada passageiro tem um custo médio de R${media_viajante}")