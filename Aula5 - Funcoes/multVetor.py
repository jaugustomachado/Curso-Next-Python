#Crie um programa que tenha uma função que receba uma lista de números
#inteiros e exiba todos os valores multiplicados por um valor inserido pelo usuário.


lista=[ ]
n_lista=int(input('quantos números você deseja inserir: '))
mult=int(input('qual é o multiplicador: '))

for n in range(n_lista):
    lista.append(int(input('informe o elemento: ')))


def funcao(vetor,x):
    vetor2=[]
    for n in vetor:
        vetor2.append(n*x)
    return print(vetor2)

funcao(lista,mult)