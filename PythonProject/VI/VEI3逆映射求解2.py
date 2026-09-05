a=eval(input())
b={}
if len(set(a.keys()))==len(set(a.values())):
    for k,v in a.items():
        b[v]=k
    print(b)
else:
    print("error")