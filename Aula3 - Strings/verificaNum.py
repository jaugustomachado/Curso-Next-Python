#Escreva um programa que verifique se determinada entrada de usuário é um número. 
#Considere válido números inteiros e reais, positivos e negativos, como:
#10, -20, 103.0, -12.5

num=input("insira o número: ")
if num.isdigit():
    print('valor inteiro positivo válido')
elif num.find('-') == 0:
    if num.count('.')==0 and num[1:].isdigit():
        print('valor inteiro negativo válido')
    elif num.count('.')==1 and (1 <= num.find('.') < len(num)) :
        print('valor real negativo válido')
    else:
        print('valor inválido')
elif num.count('.')==1 and num.count('-')==0 and (1 <= num.find('.') < len(num)):
    print('valor real positivo')
else:
    print('valor inválido')
