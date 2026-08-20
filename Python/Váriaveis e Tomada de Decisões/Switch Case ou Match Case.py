#UMA LANCHONETE trabalha com diversos combos de lanches,conforme a tabela abaixo
#COMBO 1 - Hamburguer 12,50
#COMBO 2 - CheeseBurguer 15,00
#COMBRO 3 - X-Bacon 17,50
#Crie um programa que receba o número de um combo e exiba o nome do lanche e o preço correspondente

numero_combo = int(input("Digite o número do combo desejado: "))

match numero_combo:
    case 1:
        nome_prato = "Hamburguer"
        valor_prato = 12,50
    case 2:
        nome_prato = "CheeseBurguer"
        valor_prato = 15,00
    case 3:
        nome_prato = "X-Bacon"
        valor_prato = 17,50
    case _:
        nome_prato = None
        valor_prato = None
if nome_prato:
    print(f"O combo desejado 1é o do lanche {nome_prato} e custa R${valor_prato}")