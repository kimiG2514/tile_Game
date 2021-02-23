CS480/580 Introduction to Artificial Intelligence
Assignment 1 - Uninformed Search

Authors
------- 
Kimberly Gonzales
Patricia Ile Mendoza

This is a programing assignment for uninformed search; breadth first search (BFS) and depth first search (DFS).

The assigned problem is a 25 tile slider puzzle that needs to follow ascending numerical order with the blank tile in the last spot.

This program has three otions to display functionality. First is the 8 count puzzle, second is the 15 count puzzle and lastly is the 24 count puzzle to demonstrate the full difference between BFS and DFS

--------------------------------------------------------------

Contents
--------
bfs_dfs.py
puzzle_a.txt : 3x3 board
puzzle_b.txt : 3x3 board
puzzle_c.txt : 4x4 board
test.txt : 5x5 board, assigned testing example
output.txt : text file containing execution times and number of unique
states visited during function runtime of bfs and dfs for each included
puzzle example)


Instructions
------------
-Ensure contents of package are saved in a single file location
-Enter, 'python3 bfs_dfs.py' into command line
-User will be prompted to entered the desired text file, enter,
'puzzle_a.txt' or 'puzzle_b.txt' or 'puzzle_c.txt' or 'test.txt'
-User will be prompted to choose bfs or dfs: for dfs, enter '1', for bfs, enter '2'

Expected Output
---------------
-Initial state and possible initial moves based on location of the "empty tile" will be printed to the terminal
-execution times, number of unique visited states, and solution success will be printed to output.txt 


Program Execution
-----------------
After the import of the neccesary libraries, we layed out the three possible goal states for all three slider puzzles in list form. 

Secondly after laying out the goals, we lay out the possible moves in tuples as defined by the dimesions of the board in the initial goal state. (This was achieved by converting a list of the length of the possible puzzle board (i.e., 0-8, 0-15, and 0-24) in matrix form and logically figuring out the possible moves)

A puzzle object is created using text file input and the state is represented by a list, "board."  After the user selects the desired search type, this state is compared to the pre-defined goal state to determine if they are equivalent.  If not, the "empty tile" is shifted around the "board" in an attempt to reach the goal state.

DFS - Depth first search is implemented using a data structure that emulates a stack (LIFO)

BFS - Breadth first search is implemented using a data structure that emulates a queue (FIFO)

Both searches were implemented with the use of a deque, .pop() for DFS, and .popleft() for the BFS.


Analysis
--------
**For the output file, all searches were limited to a 3 hour execution time 

3 x 3 Puzzle [ 8 number puzzle]
 input -> puzzle_a.txt 

(DFS)Depth-First Search:
Puzzle Solved:
5358 states visited
Length of execution time: 0.02959889998601284

(BFS)Breath-First Search:
Puzzle Solved:
721 states visited
Length of execution time: 0.005650999999488704

In this case, BFS won speed and won by visiting significantly less states!
-------------------------------------------------------------

3 x 3 Puzzle [ 8 number puzzle]
input -> puzzle_b.txt 

(DFS) Depth-First Search:
Puzzle Solved:
60253 states visited
Length of execution time: 0.29327430001285393

(BFS) Breath-First Search:
Puzzle Solved:
32652 states visited
Length of execution time: 0.1606772999948589

Precisely as the prior run, BFS won both speed and states visited.
------------------------------------------------------------

4 x 4 Puzzle [ 15 number puzzle]
input -> puzzle_c.txt 

(DFS)Depth-First Search:
Function timeout: 3611.422057100004 seconds
169034101 states visited

(BFS)Breath-First Search:
Puzzle Solved:
2227 states visited
Length of execution time: 0.018993700010469183 

The BFS algorithm successfuly reached the goal state, the DFS search timed out prior to completion
-------------------------------------------------------------

5 x 5 Puzzle [ 24 number puzzle]
input -> test.txt

(DFS) Depth-First Search:
Function timeout: 1829.9969628999988 seconds
126044529 states visited

(BFS) Breath-First Search:
Function timeout: 3622.275265099999 seconds
126831563 states visited

Initially, we attempted to run the searches overnight.  At around the 14 hour mark, the BFS consumed the available memory.  The DFS search is consistently killed at the 2 hour mark, hence the abbreviated function timeout as compared to the BFS timeout. 

In conclusion, it is observed that the breadth first search consistently performs better than the depth first search in both search success and execution time in the event of that success.