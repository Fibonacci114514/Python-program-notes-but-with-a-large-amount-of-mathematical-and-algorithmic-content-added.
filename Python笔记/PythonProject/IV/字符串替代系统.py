def Sprint(n,step,dx):
    if step+1%dx==0:
        print('{:^20}'.format(n))
    else:
        print('{:^20}'.format(n),end="|")
def re(x):
    x=list(x)
    for i in range(len(x)):
        if x[i]=='a':
            x[i]='cb'
        if x[i]=='b':
            x[i]='bac'
        if x[i]=='c':
            x[i]='bb'
    x=''.join(x)
    return x
s_1=input()
n=int(input())
for a in range(n):
    s_1=re(s_1)
    Sprint(s_1,a,10)