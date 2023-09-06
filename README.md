# Recursive-Sudoku-Solver
Solves a sudoku board using a recursive backtracking algorithm.

In sudoku, a board is solved when there all slots are completely filled, and each number, ranging from 1 to 9, only appears once in each row, column, and 3x3 sub square.

Input is accepted as a list of lists, with 0s representing blank squares: 

```
3 9 1   8 5 6   4 2 7 --> stored in [[3, 9, 1, 8, 5, 6, 4, 2, 7], ...]
8 0 7   2 3 4   9 1 5   
4 0 5   0 1 9   6 8 3   

7 0 4   9 6 8   1 3 2   
0 1 6   4 0 3   5 9 0   
9 3 8   5 2 1   7 6 4   

5 4 3   6 9 2   8 7 0   
6 7 2   0 8 5   3 4 0   
1 8 0   3 4 7   2 5 0  
```

This program returns whether or not a solution exists. If so, it outputs a new board with a correction solution of values for the blanks. If not, it outputs the original board. 