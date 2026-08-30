#importando o módulo json
import json

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("d:\\mateu\\algo\\agenda.json", "r", encoding="UTF-8")

#colocando o conteúdo do arquivo em uma variável do tipo string em dict

dicionario = json.loads(arquivo.read())

#fechando o arquivo

arquivo.close()

#usando o método loads para converter uma string no formato json em um dicionário

print(dicionario)

#comprovando que o objeto agenda é do tipo dicionário

print(type(dicionario))