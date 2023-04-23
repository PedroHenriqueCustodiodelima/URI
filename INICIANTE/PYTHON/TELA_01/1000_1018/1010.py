pedro = input().split()
p1 = int(pedro[0])
t1 = int(pedro[1])
c1 = float(pedro[2])
total = t1 *  c1
peça1 = input().split()
p2 = int(peça1[0])
t2 = int(peça1[1])
c2 = float(peça1[2])
total1 = t2 * c2
tudo = total + total1
print("VALOR A PAGAR: R$ {:.2f}".format(tudo))