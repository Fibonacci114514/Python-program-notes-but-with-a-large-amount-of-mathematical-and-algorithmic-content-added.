def Sprint(n,step,dx):
    if step%dx==0:
        print('{:^10}'.format(n))
    else:
        print('{:^10}'.format(n),end="|")
x=0
for i in range(100,1000000):
    n=str(i)
    a=int(n[0])
    b=int(n[1])
    c=int(n[2])
    if a**3+b**3+c**3==i:
        x+=1
        Sprint(i,x,5)