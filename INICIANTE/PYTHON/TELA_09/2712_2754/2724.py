def main():
    n = int(input())
    sp = False
    while n > 0:
        if sp:
            print('')
        sp = True
        t = int(input())
        che = []
        for i in range(t):
            che.append(input().strip())
        u = int(input())
        for i in range(u):
            harm = False
            s = input().strip()
            for j in range(t):
                if che[j] in s:
                    index = s.find(che[j]) + len(che[j])
                    if index < len(s) and (s[index].isalpha() and s[index].islower() or s[index].isdigit()):
                        continue
                    print('Abortar')
                    harm = True
                    break
            if not harm:
                print('Prossiga')
        n -= 1

if __name__ == '__main__':
    main()