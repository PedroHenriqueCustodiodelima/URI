n = int(input())
for i in range(n):
    v = input().strip()
    v1 = v.split('-')
    if all(c.isupper() for c in v1[0]) and len(v1[0]) == 3 and all(c.isdigit() for c in v1[1]) and len(v1[1]) == 4:
        dia = ""
        x = v1[1][-1]
        if x == '1' or x == '2':
            dia = "MONDAY"
        if x == '3' or x == '4':
            dia = "TUESDAY"
        if x == '5' or x == '6':
            dia = "WEDNESDAY"
        if x == '7' or x == '8':
            dia = "THURSDAY"
        if x == '9' or x == '0':
            dia = "FRIDAY"
        print(dia)
    else:
        print("FAILURE")