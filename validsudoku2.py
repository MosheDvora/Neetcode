def valid_sudoku(board):
    hash_board = set()
    for i,row in enumerate(board):
        for j in range(len(board)):
            if row[j] != '.':
                if  (str(row[j]) + " in row " + str(i) ) in hash_board: return False
                if  (str(row[j]) + " in col " + str(i)) in hash_board: return False
                if  (str(row[j]) + " in box " + str(i/3)+str(j/3)) in hash_board: return False
                        # in hash_board: return False
                hash_board.add(str(f"{row[j]} in row {i}"))
                hash_board.add(str(f"{row[j]} in col {j}"))
                hash_board.add(str(f"{row[j]} in box {i//3, j//3}"))
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
