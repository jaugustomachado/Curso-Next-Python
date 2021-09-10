#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:

# a- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
#  e o programa não deve fazer pedir os demais valores, sendo encerrado;

#b- Se o delta calculado for negativo, a equação não possui raizes reais. 
# Informe ao usuário e encerre o programa;

#c- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
#informe-a ao usuário;

#d- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = float(input('digite o valor de a: '))

if  a == 0:
    print('programa encerrado')
    
else:
    b = float(input('digite o valor de b: '))
    c = float(input('digite o valor de c: '))
    d=(b**2)-(4*a*c)
    
    if d<0:
        print('não existem raízes reais')
    elif d == 0 :
        print('existe apenas uma raiz real:', -b/(2*a))
    else:
        print('existem duas raízes reais: ', (-b+(d**(1/2)))/(2*a) , 'e', (-b-(d**(1/2)))/(2*a)  )
