while True:
    try:
        n = int(input())
    except:
        break

    m, l = map(int, input().split())
    mar = []
    leo = []
    for j in range(m):
        row = list(map(int, input().split()))
        mar.append(row)
    for j in range(l):
        row = list(map(int, input().split()))
        leo.append(row)
    cm, cl = map(int, input().split())
    a = int(input()) - 1
    cm -= 1
    cl -= 1
    if mar[cm][a] > leo[cl][a]:
        print("Marcos")
    elif mar[cm][a] < leo[cl][a]:
        print("Leonardo")
    else:
        print("Empate")
