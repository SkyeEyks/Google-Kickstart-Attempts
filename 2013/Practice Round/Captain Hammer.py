# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434d9a

import sys
sys.path.append("..\\..")
from GoogleInput import GoogleInput


def main():  # INCOMPLETE
    T = int(input())

    for case in range(1, T+1):
        V, D = map(int, input().split(' '))


GoogleInput(
    "Captain Hammer - input.txt",
    "Captain Hammer - output.txt",
    main
)
