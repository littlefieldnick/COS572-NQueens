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
    """
    Determines the diagional positions to check for conflicting queens.
    
    Params:
        - pos: position to form diagionals from
        - size: size of board (equal to N queens)
    """
    
    y, x = pos

    upper_left = [(dy, dx) for dy, dx in zip(range(y - 1, -1, -1), range(x - 1, -1, -1))]
    lower_right = [(dy, dx) for dy, dx in zip(range(y + 1, size), range(x + 1, size))]
    upper_right = [(dy, dx) for dy, dx in zip(range(y - 1, -1, -1), range(x + 1, size))]
    lower_left = [(dy, dx) for dy, dx in zip(range(y + 1, size), range(x - 1, -1, -1))]
    
    return upper_left + upper_right + lower_left + lower_right

def initialize_board(size):
    """
    Initialize a board of size N with queens placed in a random location.
    Only one queen is placed per row.
    
    Params:
        - size: Size of board
        
    Returns:
        - board: initial starting board
        - queen_locs: list of all the queen locations
    """
    
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
    """
    Checks if the constraints for a queen at a given position is satisifed.
    
    Params:
        - pos: Position to check constraints for
        - board: current board representation
    
    Returns:
        - True if all constraints are satisfied, False if not
    """
    
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
    """
    Calculates the number of constraint violations for a position.
    
    Params:
        - pos: Position to count constraints for
        - board: current board representation
    
    Returns:
        - num_conflicts: Total number of conflicts for a given position
    """
    
    
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
    """
    Runs the min conflicts algorith
    
    Params:
        - size: board size
        - num_steps: Number of steps to run the algorithm. Default: 100000
    
    Returns:
    A tuple containing (complete_solution, board, qlocs, steps) where:
        - complete_solution: is True if a solution was found, False if not
        - board: The final representation of the board
        - qlocs: The final locations of the queens
        - steps: Number of steps the min-conflicts ran for
    """
    
    # Initalize board at random and display
    board, qlocs = initialize_board(size)
    print("Initial Board:")
    display_board(board)
    
    # Run the algorithm
    for step in range(num_steps):
        conflicts = []
        
        # Find all the queens that have constraint violations
        for q in qlocs:
            if not constraint_satistified(q, board):
                conflicts.append(q)
                
        # If No conflicts, then return solution
        if(len(conflicts) == 0):
            return (True, board, qlocs, step)

        # Randomly choose a conflict to try and resolve
        y, x = random.choice(conflicts)
        scores = {}

        # Go through columns of the row the queen is in and check number of conflicts per column
        for c in range(len(board)):
            scores[(y, c)] = calc_num_conflicts((y, c), board)

        # Sort scores on number of conflicts
        scores = {key: value for key, value in sorted(scores.items(), key=lambda item: item[1])}
        
        # Get the column with minimum number of conflicts
        min_pos = []
        min_conflict = sys.maxsize

        # Generate a list of potential positions to move the queen that reduces the number of conflicts
        for pos, conflicts in scores.items():
            if conflicts <= min_conflict:
                min_conflict = conflicts
                min_pos.append(pos)
        
        # Select random min position, a random position is used to break ties
        my, mx = random.choice(min_pos)
        
        # Update the queen locations
        qlocs.append((my, mx))
        qlocs.remove((y,x))
        
        # Update queen location on board
        board[y, x] = 0
        board[my, mx] = 1

    # No solution was found return current state of board and queen locations
    return (False, board, qlocs, 0)

def display_board(board_solution):
    """
    Display a board representation
    
    Params:
        - board_solution: board to display
    """
    
    # Loop through each row
    for row in board_solution:
        output = "["
        
        # Loop through rows
        for val in columns:
            if val:
                output += " Q"
            else:
                output += " _"
        output += " ]"
        print(output)

def __main__():

    # Setup parser to get program arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--nqueen', type=int,
        help="Number of queens to place on board",
        required=False)
    
    # Parse the argument
    args = parser.parse_args()

    # Set number of queens. Default is set to 8 if no value is proved
    if args.nqueen:
        nqueen = args.nqueen
    else:
        nqueen = 8

    # Find a solution
    success, board, queen_locs, steps = min_conflicts(nqueen)
    
    # Print results
    if success:
        print("Successfully found solution using Min-Conflict in", steps, "steps.")
        
        print("\nQueens are located at:")
        print(sorted(queen_locs))
        
        print("\nSolution:")
        display_board(board)
    else:
        print("No solution found!")



if __name__ == "__main__":
    __main__()

