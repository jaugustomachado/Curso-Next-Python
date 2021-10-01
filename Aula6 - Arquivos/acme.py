'''A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco
no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede
precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, com o nome dos
usuários e seus respectivos consumos em Bytes chamado "usuarios.txt":
```
      alexandre       456123789
      anderson        1245698456
      antonio         123456456
      carlos          91257581
      cesar           987458
      rosemary        789456125
```
Neste arquivo, o nome do usuário possui 15 caracteres. 
A partir deste arquivo, você deve criar um programa que gere um relatório, 
chamado "relatório.txt", no seguinte formato:
```
    ACME Inc.       Uso do espaço em disco pelos usuários

    Nr.  Usuário        Espaço utilizado     % do uso

    1    alexandre       434,99 MB             16,85%
    2    anderson       1187,99 MB             46,02%
    3    antonio         117,73 MB              4,56%
    4    carlos           87,03 MB              3,37%
    5    cesar             0,94 MB              0,04%
    6    rosemary        752,88 MB             29,16%

    Espaço total ocupado: 2581,57 MB
    Espaço médio ocupado: 430,26 MB
```
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, 
caso sejam necessários, de forma a agilizar a execução do programa. 
A conversão da espaço ocupado em disco, de bytes para megabytes deverá 
ser feita através de uma função separada, que será chamada pelo programa principal. 
O cálculo do percentual de uso também deverá ser feito através de uma função, 
que será chamada pelo programa principal.'''

#criando o arquivo usuários.txt
with open('usuarios.txt', 'w+') as usuarios:
    usuarios.write('alexandre       456123789\n')
    usuarios.write('anderson        1245698456\n')
    usuarios.write('antonio         123456456\n')
    usuarios.write('carlos          91257581\n')
    usuarios.write('cesar           987458\n')
    usuarios.write('rosemary        789456125')
#inicializando os vetores que serão usados
dados=[ ]
nomes=[ ]
megab=[ ]
porc=[ ]
soma=[]
media=[]

#criando as funções solicitadas

def converter(usuarios,nomes, dados, megab):
    with open('usuarios.txt') as usuarios:
        for linha in usuarios:
            nomes.append(linha.split(linha[16])[0])
            dados.append(int(linha.split()[1]))
        for n in range(len(dados)):
            megab.append(float("{0:.2f}".format(dados[n]/1048576)))
def espaco_disco(vetor,porc,soma,media):
    soma.append(sum(vetor))
    media.append("{0:.2f}".format(sum(vetor)/(len(vetor))))
    for i in range(len(vetor)):
        porc.append(float("{0:.2f}".format(100*(vetor[i]/(sum(vetor))))))

#gerando o arquivo de saída

converter('usuarios.txt', nomes, dados, megab)
espaco_disco(megab,porc,soma,media)
with open('relatorio.txt', 'w+') as relatorio:
    relatorio.write('ACME Inc.       Uso do espaço em disco pelos usuários\n\n')
    relatorio.write('Nr.  Usuário        Espaço utilizado     % do uso\n\n')
    for i in range(6):
        relatorio.write(f'{i+1}    {nomes[i]}{megab[i]} MB             {porc[i]}%\n')  
    relatorio.write(f'\nEspaço total ocupado: {soma[0]} MB\n')
    relatorio.write(f'Espaço médio ocupado: {media[0]} MB')