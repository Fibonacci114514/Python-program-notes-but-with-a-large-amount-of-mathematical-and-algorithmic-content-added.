from random import *
P=eval(input('2×2转移矩阵'))
for i in range(int(len(P))):#检查矩阵是否合法
    for j in range(int(len(P))):
        if P[i][j]<0 or P[i][j]>1:
            print('输入的矩阵数字x应该为概率')
            break
    if sum(P[i])!=1:
        print('输入的矩阵行上数和不为1')
        break
s=int(input('0or1'))
n=int(input("n="))
for i in range(10):#N次蒙特卡洛模拟
    x = ''
    a=b=0
    for w in range(n):
        if random()<=P[s][0]:
            x+='a'
            s=0
            a+=1
        else:
            x+='b'
            s=1
            b+=1
    print(a/n,b/n)