#Faça um Programa que peça uma data no formato dd/mm/aaaa 
#e determine se a mesma é uma data válida.

print('informe a data no formato ss/mm/aaaa: ')

dia, mes, ano = map(int, input().split('/'))

if dia>31 or dia<0 or mes >12 or mes<0 or ano<0 :
    print("data inválida")
elif mes ==2  and dia >28:
    if  dia >29:
        print("data inválida")
    else:
        if ano% 4 == 0 or (ano%100 ==0 and ano % 400 ==0):
            print('data válida')
        else:
            print('data inválida')
elif dia==31 and (mes==4 or mes==6 or mes==9 or mes==11):
    print('data inválida')
else:
    print('data válida')