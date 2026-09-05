import turtle as t
from math import *
t.pencolor('pink')
t.pensize(3)
def draw(a,n,end):
    i=0
    while i<end:
        x=a*sin(i*n)*cos(i)
        y = a * sin(i * n) * sin(i)
        t.goto(x,y)
        i+=0.01
draw(150,6,6.28)
input()
