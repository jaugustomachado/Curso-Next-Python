#Programa que pede 2 números inteiros e um número real. Calcula e mostra:
#o produto do dobro do primeiro com metade do segundo.
#soma do triplo do primeiro com o terceiro.
#terceiro elevado ao cubo.

inteiro1 = int(input('informe o primeiro número inteiro: '))
inteiro2 = int(input('informe o segundo número inteiro: '))
real = float(input('informe o número real: '))

print('o produto do dobro do primeiro com metade do segundo é: ',inteiro1*2*0.5*inteiro2 )
print('soma do triplo do primeiro com o terceiro é: ', (inteiro1*3)+real)
print('terceiro elevado ao cubo é: ', real**3)