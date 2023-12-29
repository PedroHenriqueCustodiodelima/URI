while True:
    try:
        line = input()
        if line is None or line == "":
            break

        values = line.split()

        a = int(values[0])
        b = int(values[1])

        c = a ^ b

        print(c)

    except EOFError:
        break
