#Faça um Programa que leia 2 números e em seguida pergunte ao usuário
#qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#a. par ou ímpar;
#b. positivo ou negativo;
#c. inteiro ou decimal.

print("Informe 2 números e a opção de operação: ")

num1= float(input('informe o primeiro número:'))
num2= float(input('informe o segundo número: '))

print('0) x + y Soma de X e Y \n'
'1) x - y Subtração de X e Y \n'
'2) x * y Multiplicação de X \n'
'3) x / y Divisão de X e X \n'
'4) x // y Divisão de X e Y com resultado em inteiro \n'
'5) x % y Resto da divisão de X / Y \n'
'6) x ** y X elevado a Y \n')

list=[num1+num2, num1-num2, num1*num2, num1/num2, num1//num2, num1%num2, num1**num2]

num=int(input('Qual a operação que deseja realizar? '))
resultado=list[num]

print('O resultado é: ', resultado)

if resultado%2 ==0:
    print('O numero é par')
else:
    print('O número é ímpar')
if resultado>0:
    print('O número é postivo')
else: 
    print('O número é negativo')
if resultado%1==0:
    print('O número é inteiro')
else:
    print('O número é decimal')