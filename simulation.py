#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:48:38 2022

@author: nicklittlefield

Small simulation to determine the average number of steps it takes to solve the N-Queens problem for different values of N.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from nqueens_csp import min_conflicts

B = 10000

for i in range(4,16):
    queen_steps = []
    for b in range(B):
        success, board, queen_locs, steps = min_conflicts(i)
        queen_steps.append(steps)
    print(i, "\t", np.mean(queen_steps))
