s1=input()
s2=list(s1)
s3=''
x=int(input())
for i in s2:
    if i.islower():
        s3+=chr(ord('a')+(ord(i)+x+7)%(ord('z')-ord('a')+1))
    elif i.isupper():
        s3+=chr(ord('A')+(ord(i)+x+13)%(ord('Z')-ord('A')+1))
    elif i.isdigit():
        s3+=chr(ord('0')+(ord(i)+x+2)%(ord('9')-ord('0')+1))
    else:
        s3+=i
print(s3)