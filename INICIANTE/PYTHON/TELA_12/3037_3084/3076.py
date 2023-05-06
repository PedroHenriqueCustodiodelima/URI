import math
while True:
    try:
        n = int(input())
        result = math.ceil(n / 100)
        print(result)
    except EOFError:
        break
