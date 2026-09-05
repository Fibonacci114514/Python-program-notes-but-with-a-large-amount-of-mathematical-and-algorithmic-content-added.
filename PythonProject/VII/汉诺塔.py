i=1
def m(n,mf,mt):
    global i
    print(i,n,mf,'->',mt)
    i+=1
def h(n,A,B,C):
        if n==1:
            m(1,A,C)
        else:
            h(n-1,A,C,B)
            m(n,A,C)
            h(n-1,B,A,C)
print(h(2,'x','y','z'))