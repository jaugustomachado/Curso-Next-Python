#Problem1013
 
a, b, c =list(map(int,input().split()))

def maiorAB(a,b):
   return int((a+b+ abs(a - b))/2)

maior=maiorAB(a,b)
maior=maiorAB(maior,c)
print(f'{maior} eh o maior')