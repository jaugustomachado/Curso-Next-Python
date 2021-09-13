#Faça uma função que receba um valor inteiro e positivo e calcule o seu fatorial.

n=int(input('informe um valor: '))
mult=1

for numero in range (n,1,-1):
    mult = mult*numero

print(mult)