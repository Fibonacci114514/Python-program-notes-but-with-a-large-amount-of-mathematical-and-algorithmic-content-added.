def gt(t):
    t=t.lower()
    s1=set(t)
    s2=set()
    for i in s1:
        if not(i.isdigit() or i.islower()):
            s2.add(i)
    for i in s2:
        t=t.replace(i,' ')
    return t
def wb(t,n_top):
    w=t.split()
    c={}
    for i in w:
        c[i]=c.get(i,0)+1
    e={'the','and','to','of','a','be'}
    for i in e:
        if i in c:
            del c[i]
    x=list(c.items())
    x.sort(key=lambda x:x[1],reverse=True)
    return x[:n_top]
t=input()
t=gt(t)
for w,f in wb(t,20):
    print('{:<20}{:>5}'.format(w,f))
print('HALT')