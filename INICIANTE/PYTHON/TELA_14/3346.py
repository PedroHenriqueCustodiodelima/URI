v1 = input().split(' ')
percent1 = float(v1[0])
percent2 = float(v1[1])
percent1 = percent1 / 100 + 1
percent2 = percent2 / 100 + 1
percentAcumulado = ((percent1 * percent2) - 1) * 100
print('{0:.6f}'.format(percentAcumulado))
