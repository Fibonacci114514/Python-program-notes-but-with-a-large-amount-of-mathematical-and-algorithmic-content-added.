d={"c":[85,89,76,88],"m":[88,92,96],"e":[98,90,95]}
for k,v in d.items():
    s=sum(v)
    l=len(v)
    print('{}:{:.1f}'.format(k,s/l))