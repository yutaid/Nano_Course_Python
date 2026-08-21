rm = input("Porfavor, insira seu RM: ")
idade = int(input("Porfavor, insira sua idade: "))
if idade < 18:
    print("SAI DAE MANÉ")
else: #ou if idade>=18
    print(f"Seu cadastro foi realizado, aluno de RM {rm}")
    print("Os destalhes serão enviados para o seu email")

print("O Programa foi finalizado")