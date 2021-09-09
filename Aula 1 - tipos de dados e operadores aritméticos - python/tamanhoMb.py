#Faça um programa que peça o tamanho de um arquivo para download (em MB)
#  e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('informe o tamanho do arquivo para download em MB'))
velocidade = float(input('informe a velocidade da internet em Mbps'))
tempo = float((tamanho/velocidade)/60)
print('O tempo aproximado de download em minutos é: ', "{0:.2f}". format(tempo) , 'minutos')