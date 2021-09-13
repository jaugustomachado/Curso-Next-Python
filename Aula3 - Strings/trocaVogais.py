#Faça um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u)
# possui essa palavra. Entre com um caractere (vogal ou consoante)
# e substitua todas as vogais da palavra dada por esse caractere.

nome=input('informe texto para análise: ')
print('vogais a = ',nome.count('a'), 'vogais e= ',nome.count('e'),
 'vogais i= ',nome.count('i'), 'vogais o= ',nome.count('o'), 'vogais u=',nome.count('u'))
caractere=input('informe o caractere para troca: ')
print(nome.replace('a',caractere).replace('e',caractere).replace('i',caractere).replace('o',caractere).replace('u',caractere))