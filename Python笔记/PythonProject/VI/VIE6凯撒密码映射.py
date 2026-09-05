d={}
dx=int(input())
for i in range(26):
    d[chr(i+ord('a'))]=chr((i+dx)%26+ord('a'))
print(d)