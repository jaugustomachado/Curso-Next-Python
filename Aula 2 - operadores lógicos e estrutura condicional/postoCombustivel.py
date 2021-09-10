#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#a. Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro

# b. Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro

#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente
#sabendo-se que o preço do litro da gasolina é 2.50 o preço do litro do álcool é 1,90.

combustivel = input('informe o combustível selecionado (A-álcool, G-gasolina): ').upper()
litros = float(input('Informe o numero de litros vendidos: '))

custo_alcool=1.9*litros
custo_gasolina=2.5*litros

if combustivel =='A' :
    if  litros<20:
        desconto = 0.03*litros
        print('valor a ser pago pelo cliente: R$', custo_alcool-desconto)
    else:
        desconto = 0.05*litros
        print('valor a ser pago pelo cliente: R$', custo_alcool-desconto)
elif combustivel =='G':
    if litros<20:
        desconto = 0.04*litros
        print('valor a ser pago pelo cliente:  R$' ,custo_gasolina - desconto)
    else:
        desconto = 0.06*litros
        print('valor a ser pago pelo cliente:  R$', custo_gasolina - desconto)
else:
    print('valores informados incorretamente')