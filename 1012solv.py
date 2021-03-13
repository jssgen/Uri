#leia 3 valores: a,b, c

linha = input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

#área do triangulo
areatriangulo = (a*c)/2
print("TRIANGULO: %0.3f"%areatriangulo)

#área do circulo
pi = 3.14159
areacirculo = pi * (c**2)
print("CIRCULO: %0.3f"%areacirculo)

#área do trapezio
areatrapezio = ( (a+b)*c )/2
print ("TRAPEZIO: %0.3f"%areatrapezio)

#área do quadrado
areaquadrado = b**2
print("QUADRADO: %0.3f"%areaquadrado)

#área do retangulo
arearetangulo = a*b
print("RETANGULO: %0.3f"%arearetangulo)
