from GoogleInput import GoogleInput


def main():
    T = int(input())

    for case in range(1, T+1):
        N, K, P = map(int, input().split(" "))
        plates = []
        for stack in range(N):
            plates.append([*map(int, input().split(" "))])
        print(*plates, sep="\n")


INPUT = GoogleInput(
    "Plates - input.txt",
    "Plates - output.txt",
    main
)
