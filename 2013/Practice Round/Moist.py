# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434c05

from GoogleInput import GoogleInput

INPUT = GoogleInput(
    "2",
    "2",
    "Oksana Baiul",
    "Michelle Kwan",
    "3",
    "Elvis Stojko",
    "Evgeni Plushenko",
    "Kristi Yamaguchi"
)


def main():
    print('\nMoist')
    T = int(INPUT.get())

    for case in range(1, T + 1):
        N = int(INPUT.get())
        cost = 0
        lastName = INPUT.get()
        for i in range(N - 1):
            name = INPUT.get()
            if name >= lastName:
                lastName = name
            else:
                cost += 1
        print('Case #{}: {}'.format(case, cost))


if __name__ == "__main__":
    main()
