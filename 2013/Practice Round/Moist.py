# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434c05

from GoogleInput import GoogleInput


def main():
    T = int(input())

    for case in range(1, T + 1):
        N = int(input())
        cost = 0
        lastName = input()
        for i in range(N - 1):
            name = input()
            if name >= lastName:
                lastName = name
            else:
                cost += 1
        print('Case #{}: {}'.format(case, cost))


GoogleInput(
    'Moist - input.txt',
    'Moist - output.txt',
    main
)
