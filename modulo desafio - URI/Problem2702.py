#Problem2702
 
C,B,P=map(int,input().split(' '))
c,b,p=map(int,input().split(' '))
res=0
if C-c <0:
  res=res+abs(C-c)
if B-b<0:
  res=res+abs(B-b)
if P-p<0:
  res=res+abs(P-p)

print(res)