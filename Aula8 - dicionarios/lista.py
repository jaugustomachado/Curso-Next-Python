'''Dada a lista a seguir, crie uma segunda lista 
apenas com os itens na mesma ordem mas sem repetição.


l = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]'''

l = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
s = set()

for item in l:
  s.add(item)

print(s)