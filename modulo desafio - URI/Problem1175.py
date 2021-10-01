#Problem1175
 
N=[]
for i in range(20):
    N.append(int(input()))
N=N[::-1]
for i in range(20):
    print(f'N[{i}] = {N[i]}')