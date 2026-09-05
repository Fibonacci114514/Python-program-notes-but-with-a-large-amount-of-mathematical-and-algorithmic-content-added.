s=input()
w=list(set(s))
w.sort()
for i in w:
    print('{}|{:^5}'.format(i,s.count(i)),end=' ')