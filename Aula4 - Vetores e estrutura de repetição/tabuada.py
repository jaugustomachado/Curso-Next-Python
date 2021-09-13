#Faça um programa que recebe um número de 1 a 10 
#do usuário e imprime a tabuada de multiplicação desse número

n=int(input('informe um número de 1 a 10: ' ))

if 0<n<11:
    for _ in range(11):
        print(n,'*',_, '=' ,n*_)