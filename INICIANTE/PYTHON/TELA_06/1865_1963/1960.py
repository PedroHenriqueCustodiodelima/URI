numero = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romano = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
n = int(input())
i = 0
while n > 0:
    if n >= numero[i]:
        print(romano[i], end="")
        n -= numero[i]
    else:
        i += 1
print()
