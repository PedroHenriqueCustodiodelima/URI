def fibonot(n):
    a = 0
    b = 1
    cnt = 0
    ans = 4
    while cnt < n:
        for i in range(a + 1, b):
            ans = i
            cnt += 1
            if cnt == n:
                break
        temp = a
        a = b
        b = temp + b
    return ans

n = int(input())
print(fibonot(n))
