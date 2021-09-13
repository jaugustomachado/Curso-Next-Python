#Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25, 
#imprime o nome da pessoa e a palavra “ACEITA”, caso contrario imprimir “NÃO ACEITA”.

nome=input('informe nome: ')
sexo=input('informe sexo: ').upper()
idade=int(input('informe idade: '))

if sexo=='F' and idade<25:
    print(nome)
    print('ACEITA')
else:
    print('NÃO ACEITA')