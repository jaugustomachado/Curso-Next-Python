#Faça um programa que calcule o mostre a média aritmética de N notas.

n=int(input('informe o número de notas, para cálculo da média: '))
notas = [ ]
soma=0

for i in range(n):
    notas.append(float(input('informe a nota do aluno: ')))
    soma=soma+notas[i]

print( ' a média das notas é : ', soma/n)