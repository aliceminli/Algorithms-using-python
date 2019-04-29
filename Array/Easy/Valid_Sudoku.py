def isValidSudoku(board):

    for i in board:
        ex = set()
        for j in i:
            if j in ex:
                return False
            elif j != '.':
                ex.add(j)
    i=0
    j=0
    for i in range(9):
        ex = set()
        for j in range(9):
            if board[j][i] in ex:
                return False
            elif board[j][i] != '.':
                ex.add(board[j][i])
    # i = 0
    # j = 0
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3) if board[x][y] != '.']
            if not len(set(square)) == len(square):
                return False

    return True



if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print isValidSudoku(board)
