# Crie um programa que receba do usuário 5 números inteiros e os exiba
# na tela na ordem contrária a que foi inserido. 
# A leitura dos números deve ser feita em uma 
# função e a exibição dos valores em ordem contrária deve ocorrer em outra função.

numeros=[]

def leitura(vetor):
    for _ in range(5):
        vetor.append(int(input('informe o número: ')))
def exibicao(vetor):
    vetor.reverse()
    print(vetor)

leitura(numeros)
exibicao(numeros)