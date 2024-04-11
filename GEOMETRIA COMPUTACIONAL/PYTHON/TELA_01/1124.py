import math

def cabem_diagonal(l, c, r1, r2):
    if min(l, c) >= 2 * r1 + 2 * r2:
        return 1
    if min(l, c) >= 2 * max(r1, r2) and max(l, c) >= 2 * r1 + 2 * r2:
        return 1
    
    if c <= 2 * r1 or c <= 2 * r2 or l <= 2 * r1 or l <= 2 * r2:
        return 0
    if math.sqrt(l**2 + c**2) < 2 * r1 + 2 * r2:
        return 0
    if c > l:
        l, c = c, l
    
    xcr1 = r1
    xcr2 = c - r2
    ycr1 = r1
    ycr2 = l - r2
    
    if math.sqrt((xcr1 - xcr2)**2 + (ycr1 - ycr2)**2) < r1 + r2:
        return 0
    
    return 1

def main():
    while True:
        l, c, r1, r2 = map(int, input().split())
        
        if l == 0 and c == 0 and r1 == 0 and r2 == 0:
            break
        
        if cabem_diagonal(l, c, r1, r2):
            print("S")
        else:
            print("N")

if __name__ == "__main__":
    main()
