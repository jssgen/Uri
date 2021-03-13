ler um valor qualquer

v = float(input())

#imprimir em qual dos intervalos o valor se encontra

if 0 <= v and v <= 25:
    print("Intervalo [0,25]")
if 25 < v and v <= 50:
    print("Intervalo (25,50]")
if 50 < v and v <= 75:
    print("Intervalo (25,50]")
if 75 < v and v <= 100:
    print("Intervalo (75,100]")
if v > 100 or v < 0:
    print("Fora de intervalo")
