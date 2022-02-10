def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet -->  rep with -1
    # return row, col tuple (or (NOne, None) if there is none)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty(-1)


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess, returns True if is valid, False otherwise

    # start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now with the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square, which is tricky, but we want to get where the 3x3 square starts and iterate over the
    # 3 values in the row/column
    row_start = (row // 3) * 3  # 1//3 = 0, 5 //3 = 1, ...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if we get here, these checks pass
    return True


def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # Step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: if there's nowhere left, then we're done because we only allowed valid imputs
    if row is None:
        return True

    # Step 2:
    for guess in range(1, 10):
        # step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3.1: if this is valid, then place that guess on the puzzle!
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # Step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        # Step 5: if not valid OR if oru guess does not solve the puzzle, then we need to backtrack ad try a new number
        puzzle[row][col] = -1  # reset the guess

    # Step 6: if none of the numbers that we try work then this puzzle is UNSOLVABLE!
    return False
