def is_sudoku_valid(board):
    EMPTY = '.'
    CHANK_SIZE = 3

    def check_dup(nums):
        cln_row = [num for num in nums if num != EMPTY]
        # print(cln_row)
        if len(cln_row) == len(set(cln_row)):
            return True
        else:
            return False

    def check_rows(board):
        is_valid = True
        for row in board:
            if check_dup(row):
                continue
            else:
                is_valid = False
        return is_valid

    def check_cols(board):
        is_valid = True

        # i is the index for a row that iterate throw all columns
        for i in range(len(board)):
            col = []
            for row in board:
                if row[i] != EMPTY:
                    col.append(row[i])

            if check_dup(col):
                continue
            else:
                is_valid = False
                break
        return is_valid

    def check_chunks(board):
        is_valid = True
        # row_chunk is the CHUNK_SIZE of one row
        for row_chunk in range(0, len(board), CHANK_SIZE):
            # row_chunk is the CHUNK_SIZE of one col
            for col_chunk in range(0, len(board), CHANK_SIZE):
                # Build the square chunk
                chunk = []
                [chunk.extend(row[col_chunk:col_chunk + CHANK_SIZE]) for row in board[row_chunk:row_chunk + 3]]
                if not check_dup(chunk):
                    is_valid = False
        return is_valid

    if check_rows(board) and check_cols(board) and check_chunks(board):
        return True
    else:
        return False


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(is_sudoku_valid(board))
