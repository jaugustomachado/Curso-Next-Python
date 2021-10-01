#Problem1038
 
dict={1:4.00, 2:4.50 , 3:5.00 , 4:2.00 , 5:1.50}
X, Y=map(int,(input().split()))
print(f'Total: R$ {(dict[X]*Y):.2f}')
