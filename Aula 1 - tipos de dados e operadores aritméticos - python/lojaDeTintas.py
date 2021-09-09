#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
# cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
# Obs.: somente são vendidos um número inteiro de latas.

area = float(input('informe a área a ser pintada: '))
tinta = float(area/6)

import math
latas = math.ceil(tinta/18)
custo_latas = float(latas*80)
galoes=math.ceil(tinta/3.6)
custo_galoes=float(galoes*25)

print('a quantidade de latas a serem compradas é: ', latas, ', e o custo total é de: R$', custo_latas)
print('a quantidade de galoes a serem comprados é: ', galoes, ', e o custo total é de: R$', custo_galoes)

tinta=float(tinta*1.1)
latas=int(tinta/18)
diferenca=float((tinta/18)-latas)
galoes=math.ceil(diferenca/3.6)
custo_total=float(latas*80+galoes*25)
print('Comprando latas e galões a maneira mais rentável e com folga de 10% e menor desperdício é:\n quantidade de latas : ',
      latas, 'a quantidade de galoes : ', galoes,'\n Custo total: R$', custo_total)