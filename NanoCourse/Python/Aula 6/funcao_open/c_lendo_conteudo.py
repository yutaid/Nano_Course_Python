#usando a função open para criar um objeto do tipo arquivo

arquivo = open("d:\\mateu\\algo\\arquivo.txt", "r", encoding="UTF-8")

#printando o conteúdo do objeto arquivo

#print(arquivo.read())

#printando uma linha do arquivo

#print(arquivo.readline())

#printando outra linha do arquivo

#print(arquivo.readline())

#Passando o conteúdo do arquivo para uma lista

lista_linhas = arquivo.readlines()

#comprovando o tipo do objeto linhas_do_arquivo

print(type(lista_linhas))
print(lista_linhas)
print(" ")

#colocando a lista em ordem alfabética

lista_linhas.sort()
print(lista_linhas)
print(" ")

#Exibindo uma linha por vez, utilizando o loop for e o metodo readlines()

for linha in lista_linhas:
    print(linha)

