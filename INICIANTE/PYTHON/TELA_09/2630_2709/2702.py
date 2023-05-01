Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

calc = 0
if Cr > Ca:
    calc += Cr - Ca
if Br > Ba:
    calc += Br - Ba
if Pr > Pa:
    calc += Pr - Pa

print(calc)
