#Faça um Programa que peça um número correspondente a um determinado ano 
# e em seguida informe se este ano é ou não bissexto.

ano = int(input('informe o ano a ser testado: '))

if ano % 4 == 0 or (ano % 100 ==0 and ano % 400 ==0):
    print('o ano é bissexto')
else:
    print('o ano não é bissexto')