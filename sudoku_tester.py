#!/usr/bin/env python
#coding:utf-8

"""
Sudoku tester file.

Usage:
    python3 sudoku_tester.py

Notes:
    * Expects 'sudokus_start.txt' and 'sudokus_finish.txt' in the same directory.
    * Do NOT submit this file — only submit sudoku.py and README.txt.
"""

import sys
import time
import statistics
from sudoku import *

def main():
    if len(sys.argv) > 1:
        print("Usage: python3 sudoku_tester.py")
        sys.exit(1)
    
    try:
        # Read puzzles and solutions
        with open("sudokus_start.txt", "r") as testfile, open("sudokus_finish.txt", "r") as solfile:
            puzzles = testfile.read().strip().split("\n")
            solutions = solfile.read().strip().split("\n")

        test_no = 1
        successes, failures, skips = [], [], []
        runtimes = []

        for puzzle_no, puzzle in enumerate(puzzles):
            if len(puzzle) < 81:
                skips.append(test_no)
                test_no += 1
                continue

            # Parse puzzle into board dictionary
            board = {ROW[r] + COL[c]: int(puzzle[9*r + c]) for r in range(9) for c in range(9)}

            # Time the solver
            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()
            runtimes.append(end_time - start_time)

            # Verify solution correctness
            solved_str = board_to_string(solved_board)
            if solved_str == solutions[puzzle_no]:
                successes.append(test_no)
            else:
                failures.append((test_no, solved_str))
            test_no += 1

        # === Summary Report ===
        print("=== Sudoku Test Results ===")
        print(f"Test case count: {test_no - 1}")
        print(f"Successes:\t {len(successes)}")
        print(f"Failures:\t {len(failures)}")
        print(f"Skipped:\t {len(skips)}")

        # === Runtime Stats ===
        if runtimes:
            print("\n=== Runtime Statistics (seconds) ===")
            print(f"Min:  {min(runtimes):.4f}")
            print(f"Max:  {max(runtimes):.4f}")
            print(f"Mean: {statistics.mean(runtimes):.4f}")
            if len(runtimes) > 1:
                print(f"Std Dev: {statistics.stdev(runtimes):.4f}")
            else:
                print("Std Dev: 0.0000")

        # === Failure Details (if any) ===
        if failures:
            print("\n=== Failed Boards ===")
            for fnum, board_str in failures:
                print(f"  Board #{fnum}: {board_str}")

    except FileNotFoundError:
        print("Error: Missing 'sudokus_start.txt' or 'sudokus_finish.txt' file.")
        sys.exit(1)

if __name__ == '__main__':
    main()
