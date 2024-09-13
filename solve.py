from sudoku import *

# input sudoku puzzle
arr = input("Enter Sudoku Puzzle: ")

arr = arr.split()

# convert to matrix
if(len(arr) != 81):
    print("Enter Valid Sudoku Puzzle")
else:
    grid = []
    for i in range(9):
        grid.append([int(x) for x in arr[i*9 : i*9 + 9]])

# if success print the grid
if(solve_sudoku(grid)):
    print_grid(grid)
else:
    print ("No solution exists")