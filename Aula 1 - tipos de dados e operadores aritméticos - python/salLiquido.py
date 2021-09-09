#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
#  11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

salario_bruto = float(input('informe o salário bruto: '))
IR = 0.11*salario_bruto
INSS = 0.08*salario_bruto
sindicato = 0.05*salario_bruto
salario_liquido = salario_bruto - IR - INSS - sindicato
print('Salário Bruto : R$', salario_bruto, '\n',
         'IR (11%) : R$', IR , '\n',
         'INSS (8%) : R$', INSS, '\n',
         'Sindicato ( 5%) : R$', sindicato, '\n',
         'Salário Liquido : R$', salario_liquido)