from random import *
x=[]
n=int(input())
for i in range(n):
    x+=[int(randrange(0,100000+1))]
print(x)