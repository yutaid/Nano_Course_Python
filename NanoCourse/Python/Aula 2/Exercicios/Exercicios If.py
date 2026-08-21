faturamento_anual = float(input("Porfavor, informe seu faturamento anual: "))
assinatura = input("Por favor, informe seu tipo de assinatura: \nBasic\nSilver\nGold\nPlatinum\nDIGITE A SUA ASSINTURA:  ")
if assinatura.upper() == "BASIC":
    bonus = faturamento_anual * 0.05
elif assinatura.upper() == "SILVER":
    bonus = faturamento_anual * 0.1
elif assinatura.upper() == "GOLD":
    bonus = faturamento_anual * 0.2
elif assinatura.upper () == "PLATINUM":
    bonus = faturamento_anual * 0.3
else:
    bonus = 0
    print("O usuário não possui um bonus")
valor_total = faturamento_anual - bonus
print(f"Para um faturamento anual de R${faturamento_anual} o usuário possui um bonus de R${bonus}, portanto o valor total a ser pago é de R${valor_total}")