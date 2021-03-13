#ler a idade em dias
#converter para ano(s), mes(es), dia(s)
#1 ano = 365 dias, 1 mes = 30 dias

totaldias = int(input())

anos = totaldias//365
resto = totaldias%365

meses = resto//30
dias = resto%30

print(str(anos)+"ano(s)")
print(str(meses)+"mes(es)")
print(str(dias)+"dia(s)")

#ou
#print(anos, "ano(s)")
#print(meses, "mes(es)")
#print(dias, "dia(s)")
