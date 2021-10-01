#Aumente a lista de heróis no arquivo herois.txt. Feito isso, crie um programa que leia esse arquivo e crie dois novos arquivos:
#Um arquivo apenas com heróis da Marvel;
#Outro apenas com heróis da DC.

#Um arquivo apenas com heróis da Marvel;
#Outro apenas com heróis da DC.

#criando os vetores dc e marvel
dc=[]
marvel=[]
#criando o arquivo herois e inserindo dados
with open('herois.txt', 'w+') as usuarios:
    usuarios.write('dc,superman\n')
    usuarios.write('dc,batman\n')
    usuarios.write('dc,lanterna verde\n')
    usuarios.write('marvel,homem de ferro\n')
    usuarios.write('marvel,hulk\n')
    usuarios.write('marvel,capitão américa')
#separando os herois em listas
with open('herois.txt') as herois:
    for linha in herois:
        if 'dc' in linha.split(',')[0]:
            dc.append(linha.split(',')[1])
        else:
            marvel.append(linha.split(',')[1])
#função que cria arquivos e insere as listas
def lista_arq(nome_arq,lista):
    with open(nome_arq, 'w') as arq:
        for linha in lista:
          arq.write(linha)
#chamada de funções para criação de arquivos
lista_arq('dc.txt',dc)
lista_arq('marvel.txt',marvel)