# N-Queens

## Overview: N-Queen Problem
The N-Queen problem attempts to placing N chess queens on an N×N chessboard so that no two queens threaten each other. A solution thus requires no two queens share the same column, row, or diagonal.

## Solution
One way to solve the N-Queens problem is by treating it as a constraint satisfaction problem. In a constraint satisfaction problem, there are three components:
- <img src="https://render.githubusercontent.com/render/math?math=X"> a set of variables <img src="https://render.githubusercontent.com/render/math?math=\{X_1, X_2, \cdots, X_n\}">
- <img src="https://render.githubusercontent.com/render/math?math=D"> a set of domains <img src="https://render.githubusercontent.com/render/math?math=\{D_1, D_2, \cdots, D_n\}">
- <img src="https://render.githubusercontent.com/render/math?math=C"> a set of constraints that specify allowable combination of values <img src="https://render.githubusercontent.com/render/math?math=\{C_1, C_2, \cdots, C_n\}">

A domain <img src="https://render.githubusercontent.com/render/math?math=D_i"> is a set of allowable values for <img src="https://render.githubusercontent.com/render/math?math=X_i">. Each constraint consists of a paired value <img src="https://render.githubusercontent.com/render/math?math=(scope, rel)"> where scope is the set of variables particpating in a constraint and rel is a relationship indicating all the values the constraints can take. CSPs will attempt to assign values to the variables in a way that doesn't violate any of the constraints. A solution that doesn't violate any constraints is considered complete. 

In the N-Queens problem:
- <img src="https://render.githubusercontent.com/render/math?math=\{X_1, X_2, \cdots, X_n\}"> correspond to the individual queens
- <img src="https://render.githubusercontent.com/render/math?math=\{D_1, D_2, \cdots, D_n\}"> corresponds to values it can take which is a position in the row of the board (ranging from 1 to N)
- <img src="https://render.githubusercontent.com/render/math?math=\{C_1, C_2, \cdots, C_n\}">: 
1.) No two queens share a column 
2.) No two queens share a row
3.) No two queens share a diagonal

To solve the CSP problem the min-conflicts algorithm can be used. The algorithm starts with a possible solution to the N-Queens problem. If all the constraints are satisfied then the current representation of the CSP is the final solution. If not, then we loop for a max number of steps in an attempt to resolve the conflicts. We do this by randomly choosing a variable that has conflicts. We find a new position that has the minimum number of conflicts and move the queen to that spot, and repeat until a solution is found or we have iterated the max number of steps. 

## Example Output: 8-Queens

```
Initial Board:
[ _ Q _ _ _ _ _ _ ]
[ _ _ _ _ Q _ _ _ ]
[ _ Q _ _ _ _ _ _ ]
[ _ _ _ _ _ Q _ _ ]
[ _ _ _ _ _ Q _ _ ]
[ _ _ _ Q _ _ _ _ ]
[ _ Q _ _ _ _ _ _ ]
[ _ Q _ _ _ _ _ _ ]
Successfully found solution using Min-Conflict in 25 steps.

Queens are located at:
[(0, 2), (1, 4), (2, 7), (3, 3), (4, 0), (5, 6), (6, 1), (7, 5)]

Solution:
[ _ _ Q _ _ _ _ _ ]
[ _ _ _ _ Q _ _ _ ]
[ _ _ _ _ _ _ _ Q ]
[ _ _ _ Q _ _ _ _ ]
[ Q _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ Q _ ]
[ _ Q _ _ _ _ _ _ ]
[ _ _ _ _ _ Q _ _ ]
```

```
Initial Board:
[ _ _ Q _ _ _ _ _ ]
[ Q _ _ _ _ _ _ _ ]
[ _ _ _ _ _ Q _ _ ]
[ _ _ _ _ _ _ Q _ ]
[ _ _ _ _ _ _ _ Q ]
[ _ _ Q _ _ _ _ _ ]
[ _ _ _ _ _ _ Q _ ]
[ _ _ _ _ _ _ _ Q ]
Successfully found solution using Min-Conflict in 49 steps.

Queens are located at:
[(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)]

Solution:
[ _ _ Q _ _ _ _ _ ]
[ _ _ _ _ _ Q _ _ ]
[ _ _ _ Q _ _ _ _ ]
[ Q _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ Q ]
[ _ _ _ _ Q _ _ _ ]
[ _ _ _ _ _ _ Q _ ]
[ _ Q _ _ _ _ _ _ ]
```

## Example: 14-Queens
```
Initial Board:
[ _ _ _ _ _ _ _ _ _ _ _ Q _ _ ]
[ _ _ _ _ _ Q _ _ _ _ _ _ _ _ ]
[ Q _ _ _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ Q _ _ _ _ _ _ _ _ _ ]
[ _ _ Q _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ Q _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ Q _ _ ]
[ _ _ _ _ _ _ _ _ Q _ _ _ _ _ ]
[ _ _ _ _ Q _ _ _ _ _ _ _ _ _ ]
[ _ _ Q _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ Q _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ _ _ Q ]
[ _ _ _ _ _ _ _ Q _ _ _ _ _ _ ]
[ _ _ _ _ Q _ _ _ _ _ _ _ _ _ ]
Successfully found solution using Min-Conflict in 170 steps.

Queens are located at:
[(0, 2), (1, 8), (2, 5), (3, 9), (4, 0), (5, 13), (6, 4), (7, 7), (8, 12), (9, 10), (10, 1), (11, 6), (12, 11), (13, 3)]

Solution:
[ _ _ Q _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ Q _ _ _ _ _ ]
[ _ _ _ _ _ Q _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ Q _ _ _ _ ]
[ Q _ _ _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ _ _ Q ]
[ _ _ _ _ Q _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ Q _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ _ Q _ ]
[ _ _ _ _ _ _ _ _ _ _ Q _ _ _ ]
[ _ Q _ _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ Q _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ Q _ _ ]
[ _ _ _ Q _ _ _ _ _ _ _ _ _ _ ]
```

```
Initial Board:
[ _ _ _ _ _ _ _ _ _ _ Q _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ _ _ Q ]
[ _ _ _ _ _ _ _ Q _ _ _ _ _ _ ]
[ _ _ _ _ _ Q _ _ _ _ _ _ _ _ ]
[ Q _ _ _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ Q _ _ _ _ ]
[ _ _ _ _ _ _ _ _ Q _ _ _ _ _ ]
[ Q _ _ _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ Q _ _ ]
[ _ _ Q _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ _ _ Q ]
[ _ _ _ _ _ _ _ _ _ _ _ Q _ _ ]
[ _ _ _ _ _ _ Q _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ Q _ _ _ _ _ _ ]
Successfully found solution using Min-Conflict in 105 steps.

Queens are located at:
[(0, 6), (1, 3), (2, 10), (3, 12), (4, 4), (5, 9), (6, 11), (7, 2), (8, 5), (9, 1), (10, 8), (11, 0), (12, 13), (13, 7)]

Solution:
[ _ _ _ _ _ _ Q _ _ _ _ _ _ _ ]
[ _ _ _ Q _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ Q _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ _ Q _ ]
[ _ _ _ _ Q _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ Q _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ Q _ _ ]
[ _ _ Q _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ Q _ _ _ _ _ _ _ _ ]
[ _ Q _ _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ Q _ _ _ _ _ ]
[ Q _ _ _ _ _ _ _ _ _ _ _ _ _ ]
[ _ _ _ _ _ _ _ _ _ _ _ _ _ Q ]
[ _ _ _ _ _ _ _ Q _ _ _ _ _ _ ]
```

## Analysis
The time it take for the min-conflicts algorithm is independent of the problem size. Due to the randomized nature of the algorithm the number of steps it takes to solve the N-Queens problem varies. To get an idea of the average number of steps a bootstrap simulation (b=10000) was run for board size of 4 to 15. The results are shown below

| N-Queen | Avg. No. Steps |
|---------|----------------|
| 4       |         19.2323|
| 5       |         12.9195|
| 6       |         75.6337|
| 7       |         40.5277|
| 8       |         59.4971|
| 9       |         67.2556|
| 10      |         120.4678|
| 11      |         137.0962|
| 12      |         133.4388|
| 13      |         134.8904|
| 14      |         146.123 |
| 15      |         144.5652|

## Running the Code

When running the code the default is to run the 8-Queens problem. This can be run using the following command:

```
python3 nqueens_csp.py 
```

To run with a different value of N, the command is:

```
python3 nqueens_csp.py --nqueen NQUEEN
```

When NQUEEN is the value of N. For example, to run the 10-Queen problem, the command is

```
python nqueens_csp.py --nqueen 10
```
