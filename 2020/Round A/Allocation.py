# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

import sys
sys.path.append("..\\..")
from GoogleInput import GoogleInput


def main():
    T = int(input())

    for case in range(1, T+1):
        N, B = map(int, input().split(' '))
        prices = sorted(map(int, input().split(' ')))
        total = [0, 0]

        while total[0] <= B and len(prices):
            total[0] += prices.pop(0)
            total[1] += 1

        if total[0] > B: total[1] -= 1

        print("Case #{}: {}".format(case, total[1]))


INPUT = GoogleInput(
    "Allocation - input.txt",
    "Allocation - output.txt",
    main
)
