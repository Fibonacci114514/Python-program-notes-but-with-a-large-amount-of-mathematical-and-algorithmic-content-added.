n=int(input())
l=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    l[i][0]=1
    l[i][i]=1
for i in range(2,n):
    for j in range(1,i):
        l[i][j]=l[i-1][j-1]+l[i-1][j]
for i in range(n):
    for j in range(i+1):
        print('{:^5}'.format(l[i][j]),end='|')
    print()