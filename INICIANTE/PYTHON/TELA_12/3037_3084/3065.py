x = 0
while True:
    n = int(input())
    if n == 0:
        break

    string = input()

    if n == 1:
        print(f"Teste {x + 1}")
        print(string)
        print()
    else:
        signal = []
        for c in string:
            if c == '+':
                signal.append(True)
            elif c == '-':
                signal.append(False)

        nums = list(map(int, string.replace('+', ' ').replace('-', ' ').split()))
        ans = nums[0]
        for i in range(n - 1):
            if signal[i]:
                ans += nums[i + 1]
            else:
                ans -= nums[i + 1]

        print(f"Teste {x + 1}")
        print(ans)
        print()

    x += 1
