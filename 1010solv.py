linha = input().split()
cod = int(linha[0])
num = int(linha[1])
valor = float(linha[2])

linha2 = input().split()
cod2 = int(linha2[0])
num2 = int(linha2[1])
valor2 = float(linha2[2])

valortotal = num*valor + num2*valor2

print("VALOR A PAGAR: R$",'{:.2f}'.format(valortotal))
