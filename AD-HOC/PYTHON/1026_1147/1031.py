def josephus(n, k):
    retorno = 0

    for i in range(1, n):
        retorno = (retorno + k) % i

    return retorno


def main():
    true_value = 1
    false_value = 0

    while true_value == 1:
        qts_regioes = int(input())

        if qts_regioes == 0:
            break

        pulo = 1
        while true_value == 1:
            if josephus(qts_regioes, pulo) != 11:
                pulo += 1
            else:
                break

        print(pulo)


if __name__ == "__main__":
    main()
