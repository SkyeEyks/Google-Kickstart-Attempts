# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434d9c/0000000000434cd0

from GoogleInput import GoogleInput

INPUT = GoogleInput(
    "3",
    "4 right",
    "2 0 2 4",
    "2 0 4 2",
    "2 2 4 8",
    "2 2 4 4",
    "10 up",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "2 0 0 0 0 0 0 0 0 0",
    "3 right",
    "2 2 2",
    "4 4 4",
    "8 8 8"
)


def main():
    T = int(INPUT.get())

    for case in range(1, T+1):
        N, DIR = map(lambda _: int(_) if _.isdigit() else _, INPUT.get().split(' '))
        board = []
        for i in range(N):
            board.append(list(map(lambda _: [int(_), 0], INPUT.get().split(" "))))
        if DIR == 'left':
            for x in range(1, N):
                for y in range(N):
                    num = board[y][x][0]
                    stop = x
                    if num:
                        for xneg in range(x)[::-1]:
                            if board[y][xneg][1]:
                                stop = xneg + 1
                                break
                            if board[y][xneg][0]:
                                if board[y][xneg][0] == num:
                                    stop = xneg
                                else:
                                    stop = xneg + 1
                                break
                            stop = xneg
                    if stop != x:
                        if board[y][stop][0]:
                            board[y][stop][1] += 1
                        board[y][stop][0] += num
                        board[y][x][0] = 0
        elif DIR == 'up':
            for y in range(1, N):
                for x in range(N):
                    num = board[y][x][0]
                    stop = y
                    if num:
                        for yneg in range(y)[::-1]:
                            if board[yneg][x][1]:
                                stop = yneg + 1
                                break
                            if board[yneg][x][0]:
                                if board[yneg][x][0] == num:
                                    stop = yneg
                                else:
                                    stop = yneg + 1
                                break
                            stop = yneg
                    if stop != y:
                        if board[stop][x][0]:
                            board[stop][x][1] += 1
                        board[stop][x][0] += num
                        board[y][x][0] = 0
        elif DIR == 'right':
            for x in range(N-1)[::-1]:
                for y in range(N):
                    num = board[y][x][0]
                    stop = x
                    if num:
                        for xneg in range(x+1, N):
                            if board[y][xneg][1]:
                                stop = xneg - 1
                                break
                            if board[y][xneg][0]:
                                if board[y][xneg][0] == num:
                                    stop = xneg
                                else:
                                    stop = xneg - 1
                                break
                            stop = xneg
                    if stop != x:
                        if board[y][stop][0]:
                            board[y][stop][1] += 1
                        board[y][stop][0] += num
                        board[y][x][0] = 0
        elif DIR == 'down':
            for y in range(N-1)[::-1]:
                for x in range(N):
                    num = board[y][x][0]
                    stop = y
                    if num:
                        for yneg in range(y+1, N):
                            if board[yneg][x][1]:
                                stop = yneg - 1
                                break
                            if board[yneg][x][0]:
                                if board[yneg][x][0] == num:
                                    stop = yneg
                                else:
                                    stop = yneg - 1
                                break
                            stop = yneg
                    if stop != y:
                        if board[stop][x][0]:
                            board[stop][x][1] += 1
                        board[stop][x][0] += num
                        board[y][x][0] = 0

        finalBoard = map(lambda _: [_[__][0] for __ in range(len(_))], board)
        print("Case #{}:\n{}".format(case, '\n'.join([' '.join(map(str, line)) for line in finalBoard])))


if __name__ == "__main__":
    main()
