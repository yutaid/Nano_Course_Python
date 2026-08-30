#usando a função open para criar um objeto do tipo arquivo

arquivo = open("d:\\mateu\\algo\\arquivo.txt", "r", encoding="UTF-8")
print(type(arquivo))
print(" ")

#verificando o tipo do objeto arquivo

print(arquivo)

#printando o objeto arquivo

print(arquivo.read())

#printando o conteúdo do objeto arquivo



#fechando o arquivo