import sys
import math
import numpy as np
import collections 
from collections import deque

goal3 = ['1', '2', '3', '4', '5', '6', '7', '8', '_']
goal4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '_']
goal5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '_']

possibleMoves3 = ( 
(1,3     ),  
(0,4,2),     
(1,5),       
(0,4,6),     
(1,3,5,7),   
(2,4,8),     
(3,7),       
(4,6,8),     
(5,7))

possibleMoves4 = ( 
(1,4     ),  # square  0
(0,5,2),     # square  1
(1,6,7),     # square  2
(2,7),       # square  3
(0,5,8),     # square  4
(1,4,6,9),   # square  5
(2,5,7,10),  # square  6
(3,6,11),    # square  7
(4,9,12),    # square  8
(5,8,10,13), # square  9
(6,9,11,14), # square 10
(7,10,15),   # square 11
(8,13),      # square 12
(9,12,14),   # square 13
(10,13,15),  # square 14
(11,14))     # square 15

possibleMoves5 = (
(1, 5    ),  
(0, 2, 6),   
(1, 3, 7),
(2, 4, 8),
(3, 9),
(0, 6, 10),
(1, 5, 7, 11),
(2, 6, 8, 12),
(3, 7, 9, 13),
(4, 8, 14),
(5, 11, 15),
(6, 10, 12, 16),
(7, 11, 13, 17),
(8, 12, 14, 18),
(9, 13, 19),
(10, 16, 20),
(11, 15, 17,21),
(12, 16, 18, 22),
(13, 17, 19, 23),
(14, 18, 24),
(15, 21),
(16, 20, 22),
(17, 21, 23),
(18, 22, 24),
(19, 23))

class Puzzle :

    def __init__(self, board) :
      self.state = board
      self.goal = self.setGoal()
      self.legalMoves = self.setLegalMoves()
      if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map

    def __str__(self):
        return str(self.map)
    
    def setGoal(self) :
      if len(self.state) == 9:
        return goal3
      if len(self.state) == 16:
        return goal4
      if len(self.state) == 24:
        return goal5

    def setLegalMoves(self) :
      if len(self.state) == 9:
        return possibleMoves3
      if len(self.state) == 16:
        return possibleMoves4
      if len(self.state) == 25:
        return possibleMoves5

    def changeMap(self):       
        self.map = ''.join(str(e) for e in self.state)


def printBoard(board):
    board = board.state
    if len(board) == 9:
        print("\n".join([" ".join(board[i:i+3]) for i in range(0,len(board),3)]),'\n')
    if len(board) == 16:
        print("\n".join([" ".join(board[i:i+4]) for i in range(0,len(board),4)]),'\n')
    if len(board) == 25:
        print("\n".join([" ".join(board[i:i+5]) for i in range(0,len(board),5)]),'\n')





def breadth(board):

    visited = set()
    playQueue = deque([Puzzle(board)])
  
    while playQueue:

        node = playQueue.popleft()

        visited.add(node.map)

        if node.state == node.goal:
            print('You win!')
            visited.add(node.map)
            printBoard(node)
            return playQueue

        index = node.state.index('_') 
       
        for path in node.legalMoves[index]:          
            tryMove = node.state[:]
            newNode = Puzzle(tryMove)
            newNode.state[index] = newNode.state[path]
            newNode.state[path] = '_' 
            newNode.changeMap()     
            
            if newNode.map not in visited:
                playQueue.append(newNode)
                visited.add(newNode.map)




def main():

    fileName = input("Enter name of a text file: ")
        
    game = ([line.rstrip('\n') for line in open(fileName)])
    breadth(game)

  
if __name__=='__main__':
    main()
    