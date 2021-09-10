#Faça um Programa que peça uma data no formato dd/mm/aaaa 
# e determine se a mesma é uma data válida.
#OBS: use o módulo datetime

from datetime import datetime

date_s = input('informe a data no formato ss/mm/aaaa: ')

try:
    datetime.strptime(date_s,'%d%m%Y')
    print('data válida')
except ValueError:
    print('data inválida')