quantidade_transacoes = int(input("Quatidade de transacoes: "))
total_transacoes = 0
for n_transacao in  range(1, quantidade_transacoes +1, 1):
    transacao = float(input(f"O valor da transacao de numero {n_transacao}: "))
    total_transacoes = total_transacoes + transacao

media = total_transacoes / quantidade_transacoes
print(f"O valor total gasto é de {total_transacoes:.2f} reais, com um médio custo de {media:.2f} reais")
