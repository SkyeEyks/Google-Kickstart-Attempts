# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb

import sys
sys.path.append("..\\..")
from GoogleInput import GoogleInput


def main():
    def rec(idx: int, p: int):
        if p == 0:
            return 0
        elif idx == N:  # Not enough plates taken
            return -9e9
        ans = -9e9
        for i in range(min(K, p) + 1):
            ans = max(ans,  rec(idx + 1, p - i) + (addedValues[idx][i-1] if i else 0))  # Added last part because when i was 0 it took the last value in addedValues[idx] and added it to the answer
        return ans

    T = int(input())

    for case in range(1, T+1):
        N, K, P = map(int, input().split(" "))
        addedValues = []
        for stack in range(N):
            nums = [*map(int, input().split(" "))]
            addedValues.append([sum(nums[:i+1]) for i in range(K)])
        print("Case #{}: {}".format(case, rec(0, P)))


GoogleInput(
    "Plates - input.txt",
    "Plates - output.txt",
    main
)
