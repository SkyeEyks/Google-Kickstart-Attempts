from GoogleInput import GoogleInput


INPUT = GoogleInput(
    "Allocation - input.txt",
    "Allocation - output.txt"
)


def main():
    T = int(INPUT.get())

    for case in range(1, T+1):
        N, B = map(int, INPUT.get().split(' '))
        prices = sorted(map(int, INPUT.get().split(' ')))
        total = [0, 0]

        while total[0] <= B and len(prices):
            total[0] += prices.pop(0)
            total[1] += 1

        if total[1]: total[1] -= 1

        print("Case #{}: {}".format(case, total[1]))


if __name__ == "__main__":
    main()
    INPUT.checkOutput()
