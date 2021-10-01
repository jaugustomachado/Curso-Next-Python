'''Escreva um programa que receba o nome de uma sequência de times de 
futebol e exiba uma as partidas de um torneio com os times, de forma que:

As partidas devem ser geradas de forma aleatória.
O número de times digitados deve ser par.
O programa deve pedir nomes até que seja digitado “fim” Exemplo:
Entrada:

Digite um time: Flamengo
Digite um time: Vasco
Digite um time: Fluminense
Digite um time: Botafogo
Digite um time: Bangu 2
Digite um time: Barcelona
Digite um time: fim
Saída:

Barcelona x Botafogo
Fluminense x Vasco
Bangu 2 x Flamengo'''

import random
#input e inicialização dos vetores
time=input('digite um time: ')
times=[ ]
jogos=[]
#repetição da estrutura até a condição de parada
while time.upper() != 'FIM':
   times.append(time)
   time=input('digite um nome: ')

else:
    if len(times)%2==1:
        print('Informe uma lista com um número par de times ')
    else:
        #embaralhamento dos elementos do vetor times para o vetor jogos
        jogos=random.sample(times,len(times))
        for i in range(0,int(len(jogos)),2):
            print(jogos[i],' X ', jogos[i+1])