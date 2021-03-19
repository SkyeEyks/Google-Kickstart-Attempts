# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf#problem

import sys
sys.path.append("..\\..")
from GoogleInput import GoogleInput


def main():  # Can be made more efficient
    T = int(input())

    for case in range(1, T + 1):
        N, D = map(int, input().split(" "))


GoogleInput(
    "Bus Routes - input.txt",
    "Bus Routes - output.txt",
    main
)
