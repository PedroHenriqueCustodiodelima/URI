a=[0,0,0,0,0,0,0,0,0,0]
b= int(input())

for i in range(len(a)):
    a[i] = b
    b = b*2
    print('N[{}] = {}'.format(i,a[i]))