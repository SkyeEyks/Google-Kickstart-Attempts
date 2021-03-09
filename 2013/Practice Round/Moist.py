# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434c05

from GoogleInput import GoogleInput

INPUT = GoogleInput(
    'Moist - input.txt',
    'Moist - output.txt'
)


def main():
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
    INPUT.checkOutput()
