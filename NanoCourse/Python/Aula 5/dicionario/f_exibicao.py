dicionario = {
    "Jett": "Duelista",
    "Raze": "Duelista",
    "Omen": "Controlador",
    "Sova": "Iniciador",
    "Killjoy": "Sentinela"
}

#print(dicionario[yuta])

print(dicionario.get("yuta"))
print(" ")


print(dicionario.keys())
print(" ")



for chave in dicionario.keys():
    print(dicionario[chave])
print(" ")



print(len(dicionario.values()))
print(" ")



print("Duelista" in dicionario.values())
print("Pinto" in dicionario.values())
print(" ")



print(dicionario.items())
print(" ")



for item in dicionario.items():
    nome, categoria = item
    print(f"O(A) agente {nome} é um(a) {categoria}")
print(" ")



for nome, categoria in dicionario.items():
    print(f"O(A) agente {nome} é um(a) {categoria}")