#Crie um programa que possua uma lista de nomes. Peça que o usuário 
#insira um nome que será buscado nesta lista. 
#A busca deve ser implementada em uma função que retorna os valores
#lógicos verdadeiro ou falso.

nomes=[]

for n in range(int(input('irnforme quantos nomes você quer na lista: '))):
    nomes.append(input('informe o nome:'))

def busca(palavra, lista):
    try:
        ndx = lista.index(palavra)
    except:
        ndx = -1
    if ndx>=0:
        return True
    else:
        return False

busca(input('informe o nome para busca: '), nomes)