qtdTeste = int(input())

for i in range(1, qtdTeste+1):
    v1, v2 = input().split()
    if (v1 == "tesoura" and v2 == "papel") or (v1 == "papel" and v2 == "pedra") \
    or (v1 == "pedra" and v2 == "lagarto") or (v1 == "lagarto" and v2 == "Spock") \
    or (v1 == "Spock" and v2 == "tesoura") or (v1 == "tesoura" and v2 == "lagarto") \
    or (v1 == "lagarto" and v2 == "papel") or (v1 == "papel" and v2 == "Spock") \
    or (v1 == "Spock" and v2 == "pedra") or (v1 == "pedra" and v2 == "tesoura"):
        print(f"Caso #{i}: Bazinga!")
    elif v1 == v2:
        print(f"Caso #{i}: De novo!")
    else:
        print(f"Caso #{i}: Raj trapaceou!")
