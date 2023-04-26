while True:
    try:
        N = int(input())
        if N == 0:
            print("vai ter copa!")
        elif N > 0 and N <= 100:
            print("vai ter duas!")
        else:
            break
    except:
        break
