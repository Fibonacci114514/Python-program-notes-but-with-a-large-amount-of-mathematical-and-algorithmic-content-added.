from turtle import *
def k(d,n):
    if n==0:
        fd(d)
    else:
        for angle in [0,60,-120,60]:
            left(angle)
            k(d/3,n-1)
if __name__ == '__main__':
    setup(1000,1000)
    pen(speed=0,pendown=False,pencolor='gray')
    a,n=400,4
    goto(-a/2,a/2/pow(3,0.5))
    pd()
    for i in range(3):
        k(a,n)
        right(120)
    ht()
    done()