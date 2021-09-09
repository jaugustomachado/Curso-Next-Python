#Tendo como dado de entrada a altura (h) de uma pessoa, 
#o programa calcula o peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = input('informe o sexo da pessoa (M/F): ')
sexo=sexo.upper()

if sexo == 'M' or sexo == 'F':
    h = float(input('informe a altura da pessoa: '))

    if sexo == 'M':
        peso_ideal = (72.7*h)-58
        print('o peso ideal em relação a altura do paciente é: ', peso_ideal, 'kg')
    elif sexo == 'F':
        peso_ideal = (62.1*h)-44.7
        print('o peso ideal em relação a altura do paciente é: ', peso_ideal, 'kg')
else:
    print('sexo informado incorretamente')
