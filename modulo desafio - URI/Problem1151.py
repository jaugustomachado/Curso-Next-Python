#Problem1151
 
N=int(input())
vetor=[0,1]
if N<46:
    for i in range(N-2):
        vetor.append(vetor[i]+vetor[i+1])
    vetor_str = str(vetor)[1:-1] 
    print(''.join(vetor_str.replace(',','')))