#Faça um programa para imprimir:
 #   1
 #   1   2
 #   1   2   3
 #   .....
 #   1   2   3   ...  n

n=int(input('informe um valor: '))

for i in range(1,n+1):
     for j in range(1,i+1):
       print(j, end=" ")
     
     print()