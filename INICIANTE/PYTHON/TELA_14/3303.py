while True:
    try:
        v = input()
        if v is None:
            break
        print("palavrao" if len(v) >= 10 else "palavrinha")
    except EOFError:
        break
