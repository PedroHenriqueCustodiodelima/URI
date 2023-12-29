n = int(input())
total = 0.0
kg = 0

for i in range(n):
    num = 0

    preco = float(input())
    total += preco

    frutas = input()
    num = frutas.count(' ') + 1

    kg += num
    print(f"day {i + 1}: {num} kg")

print(f"{kg / n:.2f} kg by day")
print(f"R$ {total / n:.2f} by day")
