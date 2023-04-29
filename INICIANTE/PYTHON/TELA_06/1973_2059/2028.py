import sys

n = [[] for i in range(201)]
s = ['' for i in range(201)]

def main():
    c = 1
    for i in range(len(n)):
        l = 1
        a = (i * (i + 1) // 2) + 1
        n[i] = [0] + [k for k in range(1, i + 1) for j in range(k)]
        s[i] = ' '.join(map(str, n[i]))
    for rl in sys.stdin:
        SolveProblem(c, int(rl.strip()))
        c += 1

def SolveProblem(cn, nn):
    x = len(n[nn])
    if x < 2:
        print("Caso {}: {} numero".format(cn, x))
    else:
        print("Caso {}: {} numeros".format(cn, x))
    print(s[nn])
    print()

if __name__ == '__main__':
    main()
