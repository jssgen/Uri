#calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 km/l

#ler o tempo gasto na viagem (horas)

t = int(input())

#ler a velocidade média (km)

v = int(input())

#calcular quantos litros seriam necessários

dist = v * t
litros = dist/12

print('{:.3f}'.format(litros))
