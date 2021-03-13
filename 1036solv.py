#leia 3 valores de ponto flutuante

v = input().split()
a, b, c = v

a = float(a)
b = float(b)
c = float(c)

#efetue o cálculo das raizes da equaçao de bhaskara

if a == 0.0  or (b ** 2 - 4 * a * c) < 0:
    print("Impossivel calcular")

else:
    v1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    v2 = (- b - (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)

    print("R1 = {:.5f}".format(v1))
    print("R2 = {:.5f}".format(v2))
