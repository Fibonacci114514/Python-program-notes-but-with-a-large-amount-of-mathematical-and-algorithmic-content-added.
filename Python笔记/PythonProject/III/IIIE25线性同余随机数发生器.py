x,a,b,c,n=float(input("x=")),float(input("a=")),float(input("b=")),float(input("c=")),int(input("n="))
for i in range(n):
    x=(a*x+b)%c
    print(x)