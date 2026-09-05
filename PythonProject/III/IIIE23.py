str1=str(input())
a=int(input())
str2=""
for b in str1:
    str2+=" "
for i in range(a):
    n=1
    while n<=a-1-i:
        print(str2,end="")
        n+=1
    j=1
    while j<=2*i+1:
        print(str1,end="")
        j+=1
    print()