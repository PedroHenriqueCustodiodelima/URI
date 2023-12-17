while True:
    t = input().lower()
    if t == "*":
        break

    ok = all(word[0] == t[0] for word in t.split())
    
    print("Y" if ok else "N")