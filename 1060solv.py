#faça um programa que leia 6 valores:

n = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

#mostrar a quantidade de valores positivos digitados:

y = 0

if n > 0:
    y = y + 1
if n2 > 0:
    y = y + 1
if n3 > 0:
    y = y + 1    
if n4 > 0:
    y = y + 1
if n5 > 0:
    y = y + 1  
if n6 > 0:
    y = y + 1  

    print('{} valores positivos'.format(y))
