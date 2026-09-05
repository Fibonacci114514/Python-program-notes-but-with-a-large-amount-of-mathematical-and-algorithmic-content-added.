def ifp(x):
    for i in range(2,x):
        if x%i==0:
            return [i,ifp(int(x/i))]
    else:
        return [x]
def fac(x):
    l=ifp(x)
    fac_list=[]
    while len(l) == 2:
        fac_list.append(l[0])
        l = l[1]
    fac_list.append(l[0])
    return fac_list
n=int(input())
f=fac(n)
w=sorted(list(set(f)))
a=['({}^{})'.format(i,f.count(i)) for i in w]
print('{}={}'.format(n,'×'.join(a)))