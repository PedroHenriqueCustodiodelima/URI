while True:
    try:
        n,d = input().split()
        n,d = int(n),int(d)
        ocorrer = False
        for i in range(d):
            entrada = input().split()
            if(ocorrer):
                continue
            else:
                data = entrada[0]
                if all(n == '1' for n in entrada[1:]):
                    ocorrer = True
                    dataFinal = data

        if(ocorrer):
            print(dataFinal)
        else:
            print("Pizza antes de FdI")
    except EOFError:
        break