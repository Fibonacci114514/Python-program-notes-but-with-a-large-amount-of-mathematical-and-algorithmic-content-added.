from random import *
x=''
n=int(input())
for i in range(n):
    x+=chr(int(randrange(ord('A'),ord('z')+1)))
print(x)