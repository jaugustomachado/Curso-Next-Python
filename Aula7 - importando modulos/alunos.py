'''Escreva um programa que pergunte nomes de alunos de uma sala de aula.
O número de alunos é desconhecido, por isso o programa deve perguntar 
até que seja digitada a palavra “fim”. Depois, o programa deve sortear
um aluno para apresentar o trabalho primeiro.

Exemplo:
```
Digite um nome: Yann

Digite um nome: Camilinha

Digite um nome: Richardneydson

Digite um nome: Claudiane

Digite um nome: fim

O primeiro aluno a apresentar será: Claudiane.
```

> **Dica veja a biblioteca random**'''

import random
#input e inicialização do vetor
alunos=input('digite um nome: ')
nomes=[ ]
#repetição com condição de parada
while alunos.upper() != 'FIM':
   nomes.append(alunos)
   alunos=input('digite um nome: ')
#escolha aleatória do aluno que irá apresentar
else:
    print('o primeiro aluno a apresentar será: ', random.choice(nomes))