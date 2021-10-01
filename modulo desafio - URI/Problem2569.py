#Problem2569
 
a,op,b=map(str,input().split(' '))
b=int(b.replace('7','0'))
a=int(a.replace('7','0'))

def virus(a,b):
  c=a+b
  c=str(c).replace('7','0')
  c=int(c)
  return print(c)

def virus2(a,b):
  c=a*b
  c=str(c).replace('7','0')
  c=int(c)
  return print(c)

if op=='+':
    virus(a,b)
else:
    virus2(a,b)