import sys
import math

while True:
    string = sys.stdin.readline().rstrip('\n')

    if not string:
        break

    sum = 0
    for i in range(len(string)-1, -1, -1):
        sum += (ord(string[i]) - ord('A') + 1) * int(math.pow(26, len(string)-1-i))

    if sum <= 16384:
        print(sum)
    else:
        print("Essa coluna nao existe Tobias!")
