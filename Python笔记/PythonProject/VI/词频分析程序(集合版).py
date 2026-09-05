t=str(input())
N_top=int(input())
t=t.lower()
s1=set(t)
s2=set()
for i in s1:
    if not (i.isdigit() or i.islower()):
        s2.add(i)
for i in s2:
    t=t.replace(i,' ')
s3=set(t.split())-{'the','and','to','of','a','be'}
l2=[[t.count(i),i] for i in s3]
l2.sort(reverse=True)
l2=l2[:N_top]
for i in l2:
    print('{:<20}{:>5}'.format(i[1],i[0]))
print('HALT')