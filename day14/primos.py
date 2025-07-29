numero = int(input("Dígite o numero: "))
tprimo = True

if numero <= 1:
    tprimo = False
for i in range(2, int(numero ** 2)+ 1):
    if numero % i == 0:
        tprimo = False
    break 

if tprimo:
    print(f"{numero} É um número primo")
else:
    print(f"{numero} não é um numero primo")        