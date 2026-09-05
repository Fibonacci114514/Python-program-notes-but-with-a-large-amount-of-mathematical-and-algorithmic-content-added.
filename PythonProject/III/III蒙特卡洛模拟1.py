def Sprint(n,step,dx):
    if step%dx==0:
        print('{:^5}'.format(n))
    else:
        print('{:^5}'.format(n),end="|")
from random import *
x=1
m=x
n=0
while x>0:
    w=random()
    if w<=0.5:
        x=x-1
        if x>m:
            m=x
    else:
        x=x+1
    n+=1
    Sprint(x,n,10)
print()
print(m,n)