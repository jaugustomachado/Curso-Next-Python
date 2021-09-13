#escrever um programa em Python que leia
#um vetor V1 de n posições e gere um vetor V2 de tamanho n que é o vetor V1 invertido.

n= int(input('quantas posições você deseja que o vetor V1 tenha?'))
V1=[ ]

for _ in range(n):
    V1.append(str(input('informe o elemento do vetor V1: ')))

V2=V1[::-1]

print(V2)