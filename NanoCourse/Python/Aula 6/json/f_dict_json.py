#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo
contatos = {
    "Clark Kenté":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}


#convertendo o dicionário para uma string o formato json

conteudo_string = json.dumps(contatos, indent=4, ensure_ascii=False)

#criando um arquivo

arquivo = open("d:\\mateu\\algo\\agenda.json", "w", encoding="UTF-8")

#escrevendo o JSON dentro do arquivo

arquivo.write(conteudo_string)

#fechando arquivo

arquivo.close()