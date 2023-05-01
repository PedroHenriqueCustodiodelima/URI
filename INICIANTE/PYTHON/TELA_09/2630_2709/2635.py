import sys

for line in sys.stdin:
    n = int(line.strip())
    data = [input().strip() for _ in range(n)]
    q = int(input().strip())

    for _ in range(q):
        text = input().strip()
        ans = 0
        max_len = 0

        for word in data:
            if word.startswith(text):
                ans += 1
                max_len = max(max_len, len(word))

        if ans == 0:
            print("-1")
        else:
            print(ans, max_len)
