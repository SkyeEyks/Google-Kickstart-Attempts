# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

import sys
sys.path.append("..\\..")
from GoogleInput import GoogleInput


def main():  # Can be made more efficient
    T = int(input())

    for case in range(1, T + 1):
        N = int(input())
        checkpoint_heights = list(map(int, input().split(" ")))
        peaks = 0
        for i in range(1, N-1):
            if checkpoint_heights[i-1] < checkpoint_heights[i] > checkpoint_heights[i+1]:
                peaks += 1
        print("Case #{}: {}".format(case, peaks))


GoogleInput(
    "Bike Tour - input.txt",
    "Bike Tour - output.txt",
    main
)
