def main():
    valor = float(input())

    if valor == 0:
        print("E")
    elif valor <=  35:
        print("D")
    elif valor <= 60:
        print("C")
    elif valor <= 85:
        print("B")
    elif valor <= 100:
        print("A")


main()