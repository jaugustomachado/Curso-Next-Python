#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
# o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
# regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a 
# variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além 
# do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

peso_peixes = float(input('informe o peso de peixes pescado: '))

if peso_peixes > 50:
    excesso = peso_peixes-50
    multa = 4*excesso
    print('o excesso de peixe em kg foi:', excesso,'kg')
    print('a multa ser paga em reais é: R$ ', multa)
else:
    print('a quantidade pescada é inferior ao limite, não havendo multa')