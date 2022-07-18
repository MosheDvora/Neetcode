def valid_sudoku(board):
    hash_board = set()
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            num = row[j]
            if num != '.':
                if f"{str(num)} in row {str(i)}" in hash_board:
                    return False
                if f"{str(num)} in col {str(j)}" in hash_board:
                    return False
                if f"{str(num)} in box {str(i // 3) + str(j // 3)}" in hash_board:
                    return False
                hash_board.add(str(f"{num} in row {i}"))
                hash_board.add(str(f"{num} in col {j}"))
                hash_board.add(str(f"{num} in box {i // 3, j // 3}"))
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(valid_sudoku(board))
