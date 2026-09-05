a=eval(input())
b={}
if len(set(a.keys()))==len(set(a.values())):
    for i in a.keys():
        b[a[i]]=i
    print(b)
else:
    print("error")