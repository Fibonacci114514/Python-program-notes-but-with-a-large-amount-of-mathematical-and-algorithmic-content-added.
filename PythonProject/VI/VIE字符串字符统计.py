s=input()
w=[]
s=s.lower()
for i in s:
    if i not in w:
        w.append(i)
    else:
        continue
w.sort()
for i in w:
    print(str(i)+'|'+str(s.count(i)),end=' ')