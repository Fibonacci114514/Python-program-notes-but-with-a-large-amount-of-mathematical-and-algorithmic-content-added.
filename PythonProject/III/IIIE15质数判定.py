x=int(input())
for n in range(2,x+1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=",")