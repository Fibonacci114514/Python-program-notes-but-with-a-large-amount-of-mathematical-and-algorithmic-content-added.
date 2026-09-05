for i in range(1,10):
    for j in range(1,i+1):
        print('{:^10}'.format('{}×{}={}'.format(i,j,i*j)),end='|')
    print()