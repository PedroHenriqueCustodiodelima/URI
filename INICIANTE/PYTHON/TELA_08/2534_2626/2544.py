import math
while True:
    try:
        ninja = int(input())
    except EOFError:
        break
    
    if ninja == 1:
        print(0)
    else:
        for i in range(ninja):
            resultado = int(math.pow(2, i))
            if resultado == ninja:
                print(i)
                break
