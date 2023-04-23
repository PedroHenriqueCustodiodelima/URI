for i in range(0, 21, 2):
    for j in range(1, 4):
        k = i / 10 + j
        if i == 0 or i == 20 or (i >= 9 and i <= 11):
            print(f"I={i/10:.0f} J={k:.0f}")
        else:
            print(f"I={i/10:.1f} J={k:.1f}")
