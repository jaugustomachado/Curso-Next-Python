#Faça um programa em que troque todas as ocorrencias de uma letra L1 pela letra L2 em uma string.
# A string e as letras L1 e L2 devem ser fornecidas pelo usuario.


nome=input('informe o texto para impressão: ')
L1=input('informe a primeira letra para troca: ')
L2=input('informe a segunda letra para troca: ')

if nome.count(L1)==0:
    print('a letra selecionada não existe na string fornecida, favor digitar novamente')
else:
    print(nome.replace(L1,L2))
