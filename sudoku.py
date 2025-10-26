#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def get_peers(cell):
    """Return all peers (row, column, and box neighbors) of a given cell."""
    r, c = cell[0], cell[1]
    peers = set()

    # Row and column
    for x in ROW:
        if x != r:
            peers.add(x + c)
    for y in COL:
        if y != c:
            peers.add(r + y)

    # Box
    box_row = (ord(r) - ord('A')) // 3 * 3
    box_col = (int(c) - 1) // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            peer = ROW[i] + COL[j]
            if peer != cell:
                peers.add(peer)
    return peers


def get_valid_numbers(board, cell):
    """Return list of valid numbers for a cell based on constraints."""
    if board[cell] != 0:
        return [board[cell]]
    used = set(board[p] for p in get_peers(cell) if board[p] != 0)
    return [n for n in range(1, 10) if n not in used]


def select_unassigned_var(board):
    """Select the unassigned variable with minimum remaining values (MRV)."""
    best_cell = None
    min_options = 10
    for cell, val in board.items():
        if val == 0:
            options = get_valid_numbers(board, cell)
            if len(options) < min_options:
                min_options = len(options)
                best_cell = cell
    return best_cell


def backtracking(board):
    """Solve Sudoku using backtracking with MRV and forward checking."""
    # Check if solved
    if all(v != 0 for v in board.values()):
        return board

    # Pick next variable using MRV
    cell = select_unassigned_var(board)
    if cell is None:
        return None

    # Forward check: get valid values
    options = get_valid_numbers(board, cell)
    if len(options) == 0:
        return None  # early fail if no legal moves

    for num in options:
        board[cell] = num
        result = backtracking(board)
        if result:
            return result
        board[cell] = 0  # backtrack

    return None




if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv[1]) < 81:
            print("Input string too short")
            exit()

        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)
        
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')
    else:
        print("Usage: python3 sudoku.py <input string>")
    
    print("Finishing all boards in file.")