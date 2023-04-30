while True:
    try:
        line = input()
    except EOFError:
        break
    
    if line == "":
        continue
    
    n, a_min, a_max = map(int, line.split())
    count = 0
    
    for i in range(n):
        x = int(input())
        if a_min <= x <= a_max:
            count += 1
    
    print(count)
