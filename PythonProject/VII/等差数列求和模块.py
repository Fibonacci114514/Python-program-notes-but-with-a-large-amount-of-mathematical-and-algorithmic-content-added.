def s(n_start,n_end):
    x=0
    for i in range(n_start,n_end+1):
        x+=i
    return x
print(s(0,100))