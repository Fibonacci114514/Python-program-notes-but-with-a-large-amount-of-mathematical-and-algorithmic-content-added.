def f(x):
    return 3.8*x*(1-x)
x=float(input())
for i in range(1000):
    x=f(x)
    print(x)