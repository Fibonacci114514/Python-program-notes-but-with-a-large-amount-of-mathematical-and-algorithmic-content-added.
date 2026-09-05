x=input()
l=len(x)
y=''
for i in range(0,len(x)):
    y=y+x[l-i-1]
print(y,x[::-1])
