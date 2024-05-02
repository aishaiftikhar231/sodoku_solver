import tkinter as tk

def is_valid(board, row, col, num):
    # Check if the number already exists in the row
    for x in range(9):
        if board[row][x] == num:
            return False
    
    # Check if the number already exists in the column
    for x in range(9):
        if board[x][col] == num:
            return False
    
    # Check if the number already exists in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # If no empty cell is found, puzzle is solved
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def solve_sudoku_gui():
    for i in range(9):
        for j in range(9):
            if entry_board[i][j].get():
                board[i][j] = int(entry_board[i][j].get())
            else:
                board[i][j] = 0

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entry_board[i][j].delete(0, tk.END)
                entry_board[i][j].insert(0, board[i][j])
    else:
        print("No solution exists.")

# Create GUI window
root = tk.Tk()
root.title("Sudoku Solver")

# Create entry widgets for the Sudoku board
entry_board = [[None]*9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        entry_board[i][j] = tk.Entry(root, width=3)
        entry_board[i][j].grid(row=i, column=j)

# Create solve button
solve_button = tk.Button(root, text="Solve", command=solve_sudoku_gui)
solve_button.grid(row=9, columnspan=9)

# Example Sudoku puzzle
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Insert example puzzle into entry widgets
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            entry_board[i][j].insert(0, board[i][j])

root.mainloop()
