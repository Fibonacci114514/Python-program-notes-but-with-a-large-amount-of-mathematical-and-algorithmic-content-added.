def ifp(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
for m in range(2,1000):#区间检查
    if ifp(m) :
        print(m)
for m in range(2,1000):#孪生素数猜想
    if ifp(m) and ifp(m+2):
        print(m,m+2)
for m in range(2,1000,2):#哥德巴赫猜想
    for n in range(2,m-1):
        if ifp(n) and ifp(m-n):
            print('{:^5}+{:^5}={:^5}'.format(n,m-n,m))
            break