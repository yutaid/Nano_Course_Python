#'r' abrir para leitura (modo padrão).
#'w' abrir para a escrita, sobrescrevendo o conteúdo.
#'x' abrir para a criação de arquivo, gerando uma falha se existir um arquivo de mesmo nome.
#'a' abrindo para escrita, anexando o novo conteúdo ao final do conteúdo já existente.
#'b' abrir em modo binário.
#'t' abrir em modo de texto (modo padrão).
#'+' abrir para atualização (escrita e leitura).


#Criando uma variável de texto

conteudo = "Há muito tempo atrás, em uma galaxia muito, muito distante, ..."

#usando a função open para criar um objeto do tipo arquivo

#arquivo = open("d:\\mateu\\algo\\arquivo_texto.txt", "w", encoding="UTF-8")

#Escrevendo o conteúdo da variável conteudo dentro do arquivo w

#arquivo.write(conteudo)

#Escrevendo o conteudo da variavel conteudo dentro do arquivo e

arquivo = open("d:\\mateu\\algo\\arquivo_texto.txt", "a", encoding="UTF-8")
arquivo.write("Teste novo")

#fechando o arquivo

arquivo.close()

#Lendo o arquivo com o texto novo

arquivo = open("d:\\mateu\\algo\\arquivo_texto.txt", "r", encoding="UTF-8")
print(arquivo.read())