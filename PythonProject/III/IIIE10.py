i=1
s=0
while i<=100:
    print(i,end=",")
    if i%10==0:
        print()
    s+=i
    i+=1
print(s)