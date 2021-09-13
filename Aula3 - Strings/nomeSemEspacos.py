#Leia um vetor contendo letras de uma frase inclusive os espaços em branco. 
#Retirar os espaços em branco do vetor e depois escrever o vetor resultante.

nome =input('informe a frase desejada: ')

list=[nome.replace(' ','')]
print(list)