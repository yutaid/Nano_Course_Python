#Durante o aniversário de uma loja, ela está presenteando seus clientes da seguinte forma:
#Toda compra acima de 1000 reais, receberá um desconto de 10%
#Clientes selecionados receberam o cupom FESTA, que também gera 10% de desconto na hora da compra,não importando o valor.
#Os descontos não são cumulativos.
#Escreva um scrypt em python que receba um cupom e o valor de uma compra do usuário e informe o valor da compra.

valor_compra = float(input("Informe o valor da compra realizado: "))

#float porque tem casas decimais (ou seja centavos

cupom = input("Digite um cupom válido: ")

if valor_compra >= 1000 or cupom == "FESTA":
    novo_valor = valor_compra - (valor_compra * 10 / 100)
    print("Cupom Válido")
else:
    novo_valor = valor_compra
    print("Cupom Inválido")

print (f"O valor de sua conta será de {novo_valor} reais")