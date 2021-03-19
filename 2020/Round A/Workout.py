# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b

import sys
sys.path.append("..\\..")
from GoogleInput import GoogleInput


def main():  # Time limit exceeded
    def to_int(num: float) -> int:
        str_num = str(num)
        if "." in str_num:
            if str_num.split(".")[1][0] == "5":
                return int(num) + 1
        return round(num)

    T = int(input())

    for case in range(1, T+1):
        N, K = map(int, input().split())
        program = [*map(int, input().split())]
        differences = [program[i]-program[i-1] for i in range(1, N)]
        tokens = [0] * (N-1)

        for i in range(K):
            idx = max(range(N-1), key=lambda ii: differences[ii]/(tokens[ii] + 1))
            tokens[idx] += 1
        idx = max(range(N - 1), key=lambda ii: differences[ii] / (tokens[ii] + 1))
        print("Case #{}: {}".format(case, to_int(differences[idx]/(tokens[idx] + 1))))


GoogleInput(
    "Workout - input1.txt",
    "Workout - output1.txt",
    main
)

GoogleInput(
    "Workout - input2.txt",
    "Workout - output2.txt",
    main
)
