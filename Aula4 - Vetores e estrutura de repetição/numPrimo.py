#Encontrar números primos é uma tarefa difícil. Faça um programa que 
# gera uma lista dos números primos existentes entre 1 e um número inteiro
# informado pelo usuário.

n=int(input('informe o limite do intervalo para pesquisa: '))
primos=[]
a = 2

while (a<=n):
    resto=0
    
    for num in range(2,a):
        if a%num ==0:
            resto+=1

    if resto == 0:
      primos.append(a)
    a+=1

print(primos)
