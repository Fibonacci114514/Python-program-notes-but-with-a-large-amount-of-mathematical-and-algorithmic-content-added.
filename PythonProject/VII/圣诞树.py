from random import *
def ranstr(x):
    s = ''
    n = int(x)
    for i in range(n):
        s+=chr(int(randrange(ord('A'),ord('a')+1)))
    return s
def ranstr1(x):
    s = ''
    n = int(x)
    for i in range(n):
        s+=chr(int(randrange(ord('0'),ord('9')+1)))
    return s
print('{:^21}'.format('Φ'),end='')
for i in range(0,21,2):
    print('{:^21}'.format(str(ranstr(i-1))))
for i in range(4):
    print('{:^21}'.format(ranstr1(5)))