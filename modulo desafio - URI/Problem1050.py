#Problem1050
 
x=int(input())
ddd=[61,71,11,21,32,19,27,31]
destination=['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']
if x in ddd:
  print(destination[ddd.index(x)])
else:
  print('DDD nao cadastrado')