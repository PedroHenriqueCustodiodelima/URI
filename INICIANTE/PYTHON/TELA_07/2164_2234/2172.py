while True:
    mult, quan = map(int, input().split())
    if mult == 0 and quan == 0:
        break
    print(mult * quan)
