#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:48:38 2022

@author: nicklittlefield

Solution to N-queens problem using Min-Conflicts CSP algorithm
"""

import argparse
import numpy as np
import random
import sys

def determine_diagonals(pos, size):
    y, x = pos

    upper_left = [(dy, dx) for dy, dx in zip(range(y - 1, -1, -1), range(x - 1, -1, -1))]
    lower_right = [(dy, dx) for dy, dx in zip(range(y + 1, size), range(x + 1, size))]
    upper_right = [(dy, dx) for dy, dx in zip(range(y - 1, -1, -1), range(x + 1, size))]
    lower_left = [(dy, dx) for dy, dx in zip(range(y + 1, size), range(x - 1, -1, -1))]
    
    return upper_left + upper_right + lower_left + lower_right

def initialize_board(size):
    board = np.zeros((size, size))
    queen_locs = []

    for row in range(0, size):
        init_y = np.random.randint(0, size)

        if board[row, init_y]:
            while board[row, init_y] == 1:
                init_y = np.random.randint(0, size)

        board[row, init_y] = 1
        queen_locs.append((row, init_y))
    
    return board, queen_locs



def constraint_satistified(pos, board):
    row, col = pos

    # Check columns, iterate across rows
    for y in range(len(board)):
        if row != y and board[y, col] == 1:
            return False

    # Construct possible diagonal positions to check for queens
    diags = determine_diagonals(pos, len(board))

    # Check for diagonal constraints
    for diag in diags:
        sy, sx = diag
        if sy != row and sx != col and board[sy, sx] == 1:
            return False

  
    return True

def calc_num_conflicts(pos, board):
    row, col = pos
    num_conflicts = 0

    # Check columns, iterate across rows
    for y in range(len(board)):
        num_conflicts += np.sum(row != y and board[row, col])

    # Construct possible diagonal positions to check for queens
    diags = determine_diagonals(pos, len(board))

    # Check diagonal constraints
    for diag in diags:
        sy, sx = diag
        if sy != row and sx != col and board[sy, sx] == 1:
            num_conflicts += 1
                
    return num_conflicts

def min_conflicts(size, num_steps=100000):
    board, qlocs = initialize_board(size)
    print("Initial Board:")
    display_board(board)
    for step in range(num_steps):
        conflicts = []
        
        for q in qlocs:
            if not constraint_satistified(q, board):
                conflicts.append(q)
                
        # # Find conflicts for each queen
        # for y in range(len(board)):
        #     for x in range(len(board)):
        #         if board[y, x] == 1 and not constraint_satistified((y, x), board):
        #             conflicts.append((y, x))


        # No conflicts!
        if(len(conflicts) == 0):
            return (True, board, qlocs, step)

        # Randomly choose a conflict to try and resolve
        y, x = random.choice(conflicts)
        scores = {}

        # Go through columns and check number of conflicts per column
        for c in range(len(board)):
            scores[(y, c)] = calc_num_conflicts((y, c), board)

        # Sort scores on number of conflicts
        scores = {key: value for key, value in sorted(scores.items(), key=lambda item: item[1])}
        
        # Get the column with minimum number of conflicts
        min_pos = []
        min_conflict = sys.maxsize

        for pos, conflicts in scores.items():
            if conflicts <= min_conflict:
                min_conflict = conflicts
                min_pos.append(pos)
          
        
        # Select random min position:
        my, mx = random.choice(min_pos)
        
        qlocs.append((my, mx))
        qlocs.remove((y,x))
        
        # Move the queen to column with least number of conflicts
        board[y, x] = 0
        board[my, mx] = 1

    return (False, board, qlocs, 0)


def __main__():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--nqueen', type=int,
        help="Number of queens to place on board",
        required=False)
    
    # Parse the argument
    args = parser.parse_args()

    if args.nqueen:
        nqueen = args.nqueen
    else:
        nqueen = 8

    success, board, queen_locs, steps = min_conflicts(nqueen)
    
    if success:
        print("Successfully found solution using Min-Conflict in", steps, "steps.")
        
        print("\nQueens are located at:")
        print(sorted(queen_locs))
        
        print("\nSolution:")
        display_board(board)
    else:
        print("No solution found!")

def display_board(board_solution):
    for i, row in enumerate(board_solution):
        output = "["
        for val in row:
            if val:
                output += " Q"
            else:
                output += " _"
        output += " ]"
        print(output)

if __name__ == "__main__":
    __main__()

