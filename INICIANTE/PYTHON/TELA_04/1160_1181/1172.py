a=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
    a[i]=int(input())
    if a[i] <=0:
        a[i] = 1
    print('X[{}] = {}'.format(i,a[i]))