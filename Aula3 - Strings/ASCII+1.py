#Faça um programa que leia uma palavra e some 1 no valor ASCII
#de cada caractere da palavra. Imprima a string resultante.

palavra = input('Digite uma palavra: ')
nova = ''
for x in palavra:    
    nova = nova + chr(ord(x[0])+1) 
print('A nova palavra : ', nova)