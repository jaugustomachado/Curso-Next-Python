#Tendo como dados de entrada a altura de uma pessoa, 
# o programa calcula o peso ideal do usuário, 
# usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('informe a altura para análise: '))
peso_ideal = (72.7*altura)-58
print('o peso ideal para a altura informada é: ', peso_ideal, 'kg')