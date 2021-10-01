'''Usuario irá infomar o valor do raio, calcule a area da circuferencia utilizando 
funções e pi do modulo math.

a. Faça o arredondamento apartir segunda casa decimal para cima.
b. Faça o arredondamento apartir terceira casa decimal para baixo.'''

import math

raio=float(input('informe o valor do raio: '))
area = (raio**2)*math.pi
print(area)
print(f' {math.ceil(area*100)/100:.2f}')
print(f' {math.trunc(area*1000)/1000:.3f}')