# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434749

from GoogleInput import GoogleInput


def main():
    T = int(input())

    for case in range(1, T+1):
        M = int(input())
        for i in range(M):
            input()


GoogleInput(
    "Bad Horse - input.txt",
    "Bad Horse - output.txt",
    main
)
