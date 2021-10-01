#Problem1094
 
N=int(input())
testes=0
coelho=0
sapo=0
rato=0
while testes<N:
  X,Y=map(str,input().split())
  X=int(X)
  if 1<=X<=15:
    if Y == 'C':
      coelho=coelho+X
    if Y == 'S':
      sapo=sapo+X
    if Y == 'R':
      rato=rato+X
  testes+=1
total=coelho+sapo+rato
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {(coelho*100/total):.2f} %')
print(f'Percentual de ratos: {(rato*100/total):.2f} %')
print(f'Percentual de sapos: {(sapo*100/total):.2f} %')