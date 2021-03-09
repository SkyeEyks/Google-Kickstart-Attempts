# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434749

from GoogleInput import GoogleInput

INPUT = GoogleInput(
    "Bad Horse - input.txt",
    "Bad Horse - output.txt"
)


def main():  # INCOMPLETE
    T = int(INPUT.get())

    for case in range(1, T+1):
        M = int(INPUT.get())
        for i in range(M):
            INPUT.get()


if __name__ == "__main__":
    main()
