'''Escreva um programa que implemente o jogo conhecido como pedra, 
papel, tesoura. Neste jogo, o usuário e o computador escolhem entre 
pedra, papel ou tesoura. Sabendo que pedra ganha de tesoura, 
papel ganha de pedra e tesoura ganha de papel, exiba na tela o 
ganhador: usuário ou computador. 
Para esta implementação, assuma que o número 0 representa pedra, 
1 representa papel e 2 representa tesoura. O programa deve pedir 
para o usuário entrar com sua escolha, gerar aleatoriamente a 
escolha do computador, exibir a escolha e indicar o vencedor'''

import random

#implementação de um dicionário

dic={ 0: 'pedra', 1: 'papel', 2: 'tesoura'}

#input do usuário e escolha do computador

usuario=int(input('escolha entre: 0-pedra, 1-papel, 2-tesoura: '))
computador=random.choice(range(3))

#print das escolhas de cada um

print('a escolha do usuário foi: ', dic[usuario])
print('a escolha do computador foi: ', dic[computador])

#retorno do ganhador

if usuario==computador:
    print('empate')
elif (usuario==0 and computador==1) or (usuario==1 and computador==2) or (usuario==2 and computador==0):
    print('o computador ganhou')
else:
    print('o usuario ganhou') 