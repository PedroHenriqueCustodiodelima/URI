bolas = sum(map(int, input().split()))
nomes = ["Rudolph", "Dasher", "Dancer", "Prancer", "Vixen",
         "Comet", "Cupid", "Donner", "Blitzen"]
print(nomes[bolas % 9])
