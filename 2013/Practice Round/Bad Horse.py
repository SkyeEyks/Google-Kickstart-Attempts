# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434749

from GoogleInput import GoogleInput

INPUT = GoogleInput(
    "2",
    "1",
    "Dead_Bowie Fake_Thomas_Jefferson",
    "3",
    "Dead_Bowie Fake_Thomas_Jefferson",
    "Fake_Thomas_Jefferson Fury_Leika",
    "Fury_Leika Dead_Bowie"
)


def main():  # INCOMPLETE
    T = int(INPUT.get())

    for case in range(1, T+1):
        M = int(INPUT.get())
        for i in range(M):
            INPUT.get()


if __name__ == "__main__":
    main()
