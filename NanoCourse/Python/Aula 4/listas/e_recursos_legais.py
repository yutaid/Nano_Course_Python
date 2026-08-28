#valores fora de ordem

valores = (1, 4.5, 8, 6, 7, 4, 5, 3, 11, 19, 3.5, 1, 8, 19)

#exibicao da lista

print(f"A lista está desse jeito: {valores}")

#contagem de elementos 1

contagem = valores.count(1)
print(f"Há {contagem} elementos de número 1")

#Invertendo a lista

valores = list(valores)
valores.reverse()
print(f"A lista invertida ficou de: {valores}")

#Ordenando a lista, ordem crescente

valores.sort()
print(valores)

#Ordenando a lista, ordem descrescente

valores.sort(reverse=True)
print(valores)

#Tamanho da lista

quantidade = len(valores)
print(f"quantidade de elementos nessa lista é {quantidade}")

#Soma dos valores

soma = sum(valores)
print(f"A soma dos valores é {int(soma)}")
