a = int(input())
b = int(input())
num = 0
for i in range(a-1,b,-1):
    if i%2 == 1:
     num += i

print(num)