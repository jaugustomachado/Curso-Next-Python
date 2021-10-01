'''Faça um programa que crie uma pasta no diretorio atual do 
notebook e crie dentro dele um arquivo chamado, lista_de_chamada.txt, 
na qual devera ter 5 nomes informados pelo usuario.'''

import os

pasta = '/content/nova_pasta'

if os.path.isdir(pasta): # vemos se este diretorio ja existe
    print ('Ja existe uma pasta com esse nome!')
else:
    os.mkdir(pasta) # aqui criamos a pasta caso nao exista
    print ('Pasta criada com sucesso!')

with open('/content/nova_pasta/lista_de_chamada.txt', 'w+') as lista:
    lista.write(input('Informe o primeiro nome: ')+'\n')
    lista.write(input('Informe o segundo nome: ')+'\n')
    lista.write(input('Informe o terceiro nome: ')+'\n')
    lista.write(input('Informe o quarto nome: ')+'\n')
    lista.write(input('Informe o quinto nome: ')+'\n')