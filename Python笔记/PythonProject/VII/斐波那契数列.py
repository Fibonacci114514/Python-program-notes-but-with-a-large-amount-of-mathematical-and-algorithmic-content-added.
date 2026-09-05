def Sprint(n,step,dx):
    if step%dx==0:
        print('{:^20}'.format(n))
    else:
        print('{:^20}'.format(n),end="|")
def f(n):
    if n<=1:
        return n
    else:
        return f(n-1)+f(n-2)
for i in range(40):
    Sprint(f(i),i+1,4)