a = int(input())
b =['']
for i in range(1,a + 1):
    b.append(int(input()))
   
for i in range(1,a + 1):
    if b[i] == 0:
        print('NULL')
       
    if b[i] > 0:
        if b[i] % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
           
    if b[i] < 0:
        if b[i] % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')