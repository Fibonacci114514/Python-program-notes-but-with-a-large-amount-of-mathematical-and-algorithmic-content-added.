def Sprint(n,step,dx):
    if step%dx==0:
        print('{:^20}'.format(n))
    else:
        print('{:^20}'.format(n),end="|")
for i in range(1,11):
    Sprint(i,i,dx=4)