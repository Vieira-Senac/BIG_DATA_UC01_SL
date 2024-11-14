# Programa Prestação em Atraso
prestacao = float(input("Informe o valor da prestação: "))
taxa = float(input("Informe a taxa mensal: "))
tempo = float(input("Informe a quantidade de meses em atraso: "))
valor_final = prestacao+(prestacao*(taxa/100)*tempo)
print(f"O valor final da prestação é R$ {valor_final:.2f}")
