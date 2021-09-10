#Construa uma pequena chave dicotômica para identificar uma determinada planta 
# como membro de um dos principais grupos: Bryophyta, Pteridophyta, Gymnospermae ou Angiospermae.
# A identificação se dá com base na presença (1) ou ausência (0) de três caracteres:
# vascularização, sementes e flores. Utilize a tabela abaixo como referência.

#  Grupo	     Vascularização	  Sementes  	Flores

#Bryophyta	          0	             0	          0
#Pteridophyta	      1              0            0
#Gymnospermae	      1              1            0
#Angiospermae	      1              1            1

print('informe os dados solicitados abaixo para descobrir o grupo a que pertence a espécie: ')

vasc = int(input('a espécie tem vascularização 1- sim , 0 - não: '))
sem = int(input('a espécie tem sementes 1- sim , 0 - não: '))
flor = int(input('a espécie tem flores 1- sim , 0 - não: '))

if vasc == 0 and sem==0 and flor==0:
    print('a espécie é: Bryophyta')
elif vasc ==1 and sem ==0 and flor==0:
    print('a espécie é: Pteridophyta')
elif vasc == 1 and sem ==1 and flor == 0:
    print('a espécie é: Gymnospermae')
elif vasc == 1 and sem ==1 and flor == 1:
    print('a espécie é: Angiospermae')
else:
    print('algum valor foi informado incorretamente')
