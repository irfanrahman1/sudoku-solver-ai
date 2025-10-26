Number of Sudoku boards solved: 400

Runtime statistics (in seconds)
--------------------------------
Min:  0.0043
Max:  0.6494
Mean: 0.0582
Std Dev: 0.0758

Environment
-----------
Machine: MacBook Pro (14-inch, 2023)
Chip: Apple M2 Pro
Memory: 16 GB
Operating System: macOS Tahoe 26.0.1
Python version: 3.x

Algorithm Description
---------------------
This Sudoku solver uses a backtracking search algorithm enhanced with the 
Minimum Remaining Value (MRV) heuristic to choose the next unassigned cell. 
For each cell, the algorithm tests possible values consistent with Sudoku 
constraints (row, column, and 3x3 subgrid). If no valid number remains, it 
backtracks. The solver efficiently completes all provided puzzles.
