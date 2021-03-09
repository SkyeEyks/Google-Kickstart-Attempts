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
    "8 8 8",
    ans=[
        "Case #1:",
        "0 0 4 4",
        "0 2 4 2",
        "0 4 4 8",
        "0 0 4 8",
        "Case #2:",
        "4 0 0 0 0 0 0 0 0 0",
        "4 0 0 0 0 0 0 0 0 0",
        "4 0 0 0 0 0 0 0 0 0",
        "4 0 0 0 0 0 0 0 0 0",
        "4 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0",
        "Case #3:",
        "0 2 4",
        "0 4 8",
        "0 8 16"
         ]
)


def main():
    """
    My method:

    I create a matrix of size N*N from the given numbers. Each value in the matrix
    is a list of 2 integers, the first being the given number and the second indicating
    whether the number was the result of a merge (1=True, 0=False). Starting 1 line away
    from the side the numbers are being pushed to I check to see if it contains a number
    that isn't 0. If it does I look for the first number in the direction it's being pushed.
    If the number found is equal to the number being pushed they merge and occupy the same position.
    If the number's aren't equal or the number found has already been merged then the number being
    pushed gets moved to 1 position before the number found. This goes on until the program has
    gone through all the values in the matrix

    """

    T = int(INPUT.get())  # number of test cases

    for case in range(1, T + 1):
        N, DIR = map(lambda _: int(_) if _.isdigit() else _,
                     INPUT.get().split(' '))  # N = length and height of matrix; DIR = direction to move numbers
        board = []

        for i in range(N):
            board.append(list(map(lambda _: [int(_), 0], INPUT.get().split(" "))))

        if DIR == 'left':
            for x in range(1, N):  # x position of matrix
                for y in range(N):  # y position of matrix
                    num = board[y][x][0]  # The value at (x, y) in the matrix
                    stop = x  # Where the value at (x, y) should be moved to
                    if num:
                        for xneg in range(x)[
                                    ::-1]:  # xneg is the x position between x and the edge of the board in the direction of DIR
                            if board[y][xneg][1]:  # if the number found has been merged, move the value to one position before (xneg, y)
                                stop = xneg + 1
                                break
                            if board[y][xneg][0]:  # if the value of (xneg, y) isn't 0
                                if board[y][xneg][0] == num:  # if the value of (xneg, y) equals (x, y)
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
            for y in range(1,
                           N):  # up starts going through values from the top, so I'm going through each x pos for each y pos
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
            for x in range(N - 1)[::-1]:
                for y in range(N):
                    num = board[y][x][0]
                    stop = x
                    if num:
                        for xneg in range(x + 1, N):
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
            for y in range(N - 1)[::-1]:
                for x in range(N):
                    num = board[y][x][0]
                    stop = y
                    if num:
                        for yneg in range(y + 1, N):
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
    INPUT.checkOutput()


if __name__ == "__main__":
    main()
