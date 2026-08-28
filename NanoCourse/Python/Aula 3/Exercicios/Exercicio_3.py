#A sequencia de fibonacci é: 1, 1, 2, 2, 3, 5, 8, 13, 21, ... (Soma dos dois anteriores)
#Caso o usuario digite o numero 55, print Acao bem sucedida
#Caso o usuario digite algum numero que nao esteja na sequencia print A acao falhou
quantidade_elementos = int(input("Quantos elementos deseja fazer? "))
anterior1 = 1
anterior2 = 0
numero_usuario = int(input("Diga um numero inteiro: "))
for n_elementos in range(1, quantidade_elementos +1 , 1):
    valor_atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = valor_atual
    if numero_usuario == valor_atual:
        print("Acao bem sucedida")
        break
    if numero_usuario < valor_atual:
        print("Acao falhou")
        break
