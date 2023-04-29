cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0

n = int(input())
v = input().split()

for i in range(n):
    t = int(v[i])
    if t % 2 == 0:
        cnt2 += 1
    if t % 3 == 0:
        cnt3 += 1
    if t % 4 == 0:
        cnt4 += 1
    if t % 5 == 0:
        cnt5 += 1

print(f"{cnt2} Multiplo(s) de 2")
print(f"{cnt3} Multiplo(s) de 3")
print(f"{cnt4} Multiplo(s) de 4")
print(f"{cnt5} Multiplo(s) de 5")
