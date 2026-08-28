#LISTA ORIGINAL
duelistas = ["jett", "raze", "waylay", "neon", "iso", "reyna"]
print(f"A lisa original contém os elementos:\n {duelistas}")
#APRENDENDO A COLOCAR ALGO NOVO NA LISTA
duelistas.append("yoru")
print(duelistas)
#APRENDENDO A COLOCAR COM INPUT E NÃO DIRETAMENTE NO CODIGO
duelistas.append(input("Digite um duelista faltante: "))
print(duelistas)
#APRENDENDO A COLOCAR EM ALGUM LUGAR ESPECIFICO DA LISTA
duelistas.insert(1, input("Digite um duelista faltante: "))
print(duelistas)


