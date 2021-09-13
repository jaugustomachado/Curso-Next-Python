#Faça um programa para imprimir:
 #   1
 #   2   2
 #   3   3   3
 #   .....
 # #   n   n   n   n   n   n  ... n

n = int(input('informe o limite do loop: '))

for i in range(1,n+1):
    for j in range(1,i+1):
       print(i, end=" ")
    
    print()
