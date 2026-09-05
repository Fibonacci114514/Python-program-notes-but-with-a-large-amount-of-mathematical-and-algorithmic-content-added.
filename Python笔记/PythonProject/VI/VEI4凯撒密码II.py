f1={}
f2={}
f3={}
dx=int(input())
for i in range(26):
    f1[chr(i+ord('a'))]=chr((i+dx)%26+ord('a'))
for i in range(26):
    f2[chr(i+ord('A'))]=chr((i+dx)%26+ord('A'))
for i in range(10):
    f3[chr(i+ord('0'))]=chr((i+dx)%10+ord('0'))
s=input()
s1=''
for i in s:
    if i.islower():
        s1+=f1[i]
    elif i.isupper():
        s1+=f2[i]
    elif i.isdigit():
        s1+=f3[i]
    else:
        s1+=i
print(s1)