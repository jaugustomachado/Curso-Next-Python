#Faça um programa que recebe do usuário 10 valores de números inteiros,
#armazena em um vetor e apos percorre-lo exibe qual é o maior valor e a sua posição.

vetor=[]

for _ in range(10):
    vetor.append(int(input('informe o elemento do vetor: ')))

print('o maior valor do vetor é: ', max(vetor), 'e sua pocição é: ', vetor.index(max(vetor)))