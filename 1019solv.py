#ler um valor em segundos

n = int(input())

#transformar para h:m:s

h = n//3600
r = n%3600

m = r//60
s = r%60

#imprimir

print(str(h)+":"+str(m)+":"+str(s))
