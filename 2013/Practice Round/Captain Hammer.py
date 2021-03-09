# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434d9a

from GoogleInput import GoogleInput

INPUT = GoogleInput(
    "3",
    "98 980",
    "98 490",
    "299 1234"
)


def main():  # INCOMPLETE
    T = int(INPUT.get())

    for case in range(1, T+1):
        V, D = map(int, INPUT.get().split(' '))


if __name__ == "__main__":
    main()
