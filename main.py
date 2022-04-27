board = [
    [9, 1, 3, 0, 0, 8, 2, 7, 0],
    [6, 0, 7, 0, 0, 2, 1, 0, 9],
    [2, 0, 4, 0, 0, 7, 8, 3, 6],
    [3, 4, 0, 0, 2, 6, 0, 1, 8],
    [8, 0, 1, 0, 7, 0, 5, 0, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0],
    [0, 7, 9, 6, 8, 0, 3, 0, 0],
    [0, 0, 0, 0, 3, 4, 0, 0, 0],
    [5, 0, 8, 0, 0, 9, 0, 0, 0]
]


def solve(board):
    pos = findNextSpace(board)
    if not pos:
        return True
    for i in range(1, 10):
        if checkIfValid(board, pos, i):
            board[pos[0]][pos[1]] = i
            if solve(board):
                return True
            board[pos[0]][pos[1]] = 0
    return False

def findNextSpace(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return [i, j]
    return []


def checkIfValid(board, pos, num):
    row = pos[0]
    column = pos[1]

    #check horizontal
    if num in board[row]:
        return False

    #check vertical
    for i in range(9):
        if board[i][column] == num:
            return False

    #check box
    return checkbox(board, row, column, num)


def checkbox(board, row, column, num):
    rowbound = findLowNhigh(row)
    columnbound = findLowNhigh(column)
    for i in range(rowbound[0], rowbound[1]):
        for j in range(columnbound[0], columnbound[1]):
            if board[i][j] == num:
                return False
    return True


def findLowNhigh(index):
    if index < 3:
        return [0, 3]
    elif index < 6:
        return [3, 6]
    elif index < 9:
        return [6, 9]

solve(board)

print(board)