def r1(list_1):
    m=max(list_1)
    list_1.remove(m)
    if len(list_1)>1:
        return [m,r1(list_1)]
    else:
        return [m,list_1]
def r(x,rev=False):
    l=r1(x)
    fac_list=[]
    while len(l) == 2:
        fac_list.append(l[0])
        l = l[1]
    fac_list.append(l[0])
    if not rev:
        fac_list=fac_list[::-1]
    return fac_list
print(r(eval(input())))