#ler um valor com duas casas decimais (float)
#calcular e mostrar o valor com o imposto de renda

s = float(input())

if s <= 2000.00:
    imp = 0
    print("isento")

if 2000.00 < s <= 3000.00:
    vt = s - 2000.00
    imp = vt * (8/100)

if 3000.00 < s  <= 4500.00:
    imp2 = (8/100) * (1000.00)
    vt2 = s - 3000.00
    imp = vt2 * (18/100) + imp2

if s > 4500.00:
    imp2 = (8/100) * (1000.00)   
    imp3 = (18/100) * (1500.00)
    s2 = s - 4500.00
    imp = imp3 + imp2 + s2 * (28/100)

if s > 2000.00:
    print("R$ %0.2f"%imp)
