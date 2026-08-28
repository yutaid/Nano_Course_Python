notas = []

while input("Deseja inserir uma nota? \nS - Sim\nN- Não\n").upper() != "N":
    notas.append(float(input("NOTA: ")))
media_aritmetica = sum(notas) / len(notas)
print(f"A media da turma foi de {media_aritmetica:.1f}")
