#Crie um programa que registra 4 notas de uma pessoa na escola
#(como o boletim) em um arquivo. Em seguida, leia todos os valores para 
#imprimir o menor valor, o maior e a média.
#Dica: Se você usar listas, pode usar as funções min() e max().


with open('notas.txt', 'w') as notas:
    for _ in range(4):
        notas.write(input('insira quatro notas: ')+'\n')
with open('notas.txt') as notas:
    result=[]
    for linha in notas:
        result.append(int(linha))

    print(f'A maior nota é:{max(result)}' )
    print(f'a menot nota é:{min(result)}' )
    print(f'a media de nota é:{(sum(result))/len(result)}')