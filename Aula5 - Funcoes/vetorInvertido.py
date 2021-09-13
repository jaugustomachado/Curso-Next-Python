#Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba 
#todos os seus valores em ordem invertida. Obs.: Sem usar invert ou o fatiador com passo -1.

numeros=[]

def leitura(vetor):
    for _ in range(5):
        vetor.append(int(input('informe o número: ')))

def exibicao(vetor):
    idx=len(vetor)-1
    vetornovo = []
    
    while idx>=0:
        vetornovo.append(numeros[idx])
        idx=idx-1
    
    return print(vetornovo)

leitura(numeros)
exibicao(numeros)