def Sprint(n,step,dx):
    if step%dx==0:
        print('{:^10}'.format(n))
    else:
        print('{:^10}'.format(n),end="|")
n=int((input()))
i=0
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=n*3+1
    i=i+1
    Sprint(n,i,5)