vetor = []
for i in range(20):
    x = int(input())
    vetor.append(x)

for i in range(20 // 2):
    temp = vetor[i]
    vetor[i] = vetor[19 - i]
    vetor[19 - i] = temp

for i in range(20):
    print("N[{}] = {}".format(i, vetor[i]))
