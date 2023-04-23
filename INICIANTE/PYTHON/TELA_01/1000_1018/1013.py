n1 = input().split()
primeiro = int(n1[0])
segundo  = int(n1[1])
terceiro = int(n1[2])
maior = primeiro
if (segundo > maior):
 maior = segundo
if (terceiro > maior):
 maior = terceiro
print(maior,"eh o maior")