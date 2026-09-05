from turtle import *
from random import *
tracer(True)
shape('turtle')
speed(0)
n=eval(input())
for i in range(1000):
    fd(10)
    rt((180/n)*randint(-n,n))
    pencolor(random(),random(),random())
input()