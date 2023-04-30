while True:
    try:
        a = int(input())
        b = input().split()
        c = b.count('1')
        if c/a >= 2/3:
            print('impeachment')
        else:
            print('acusacao arquivada')
       
    except EOFError:
        break