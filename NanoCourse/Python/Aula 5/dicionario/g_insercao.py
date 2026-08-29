dicionario = {}

dicionario["Skye"] = "Iniciador"
print(dicionario)

dicionario.update({"Kayo": "Iniciador"})
print(dicionario)
print(" ")

#OUTRA COISA MAS MESMA MATERIA

funcionarios = {}

while input("Quer inserir um funcionario? \nS-Sim\nN-Nao\n").upper() != "Nao".upper():
    nome = input("Nome: ")
    funcao = input("Função: ")
    #funcionarios.update({nome:funcao})
    #funcionarios[nome] = funcao
print(funcionarios)