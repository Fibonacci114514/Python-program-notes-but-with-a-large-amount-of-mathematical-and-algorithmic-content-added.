def f(x):
    a=[]
    for i in range(10):
        if x>1:
            a.append(f(x-1))
        else:
            a.append(i)
    return a
print(f(10))