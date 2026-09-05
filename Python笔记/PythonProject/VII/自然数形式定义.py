def N(n):
    if n<=0:
        return ["∅"]
    else:
        return N(n-1)+[N(n-1)]
print(N(0)[-1])