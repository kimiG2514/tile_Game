"""
Assignment 1 - Uninformed Search 
CS480/580 Introduction to Artificial Intelligence

Authors: Kimberly Gonzales
         Patricia Ile-Mendoza
         Mckayla Hagerty
"""

import sys
import math
import timeit
import time
import numpy as np
import collections 
from collections import deque
from multiprocessing import Process
from math import*
from itertools import islice

#goal state lists as defined by dimension of the board
goal3 = ['1', '2', '3', '4', '5', '6', '7', '8', '_']
goal4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '_']
goal5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '_']


MaxDepth = 0

#possible move tuples as defined by the dimension of the board
possibleMoves3 = ( 
(1,3     ),  
(0,2,4),     
(1,5),       
(0,4,6),     
(1,3,5,7),   
(2,4,8),     
(3,7),       
(4,6,8),     
(5,7))

possibleMoves4 = ( 
(1,4     ),  
(0,5,2),     
(1,6,7),     
(2,7),       
(0,5,8),     
(1,4,6,9),   
(2,5,7,10),  
(3,6,11),    
(4,9,12),    
(5,8,10,13), 
(6,9,11,14), 
(7,10,15),   
(8,13),      
(9,12,14),   
(10,13,15),  
(11,14))     

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

  def __init__(self, board, key) :

    """
      Parameters
      ----------
      state : list
          a list of integers representing the game board
      goal : list
          a list of integers representing the solved board
      legalMoves : tuple
          a 2 dimensional tuple of integers that define the game moves

    """
    self.state = board
    self.goal = self.setGoal()
    self.legalMoves = self.setLegalMoves()
    self.depth = 0
    self.cost = 0
    self.key = key
    if self.state:
          self.map = ''.join(str(e) for e in self.state)


  def __eq__(self, other) -> bool:
      return self.map == other.map


  def __lt__(self, other) -> bool:
      return self.map < other.map


  def __str__(self) -> str:
      return str(self.map)
  

  def setGoal(self) -> list:
    """
      returns the goal state to the calling function which is determined by 
      the length of the object's state
       
    """
    if len(self.state) == 9:
      return goal3
    if len(self.state) == 16:
      return goal4
    if len(self.state) == 25:
      return goal5


  def setLegalMoves(self) -> tuple:
    """
      returns the tuple that defines the legal moves which is determined by
      the length of the object's state

    """
    if len(self.state) == 9:
      return possibleMoves3
    if len(self.state) == 16:
      return possibleMoves4
    if len(self.state) == 25:
      return possibleMoves5


  def changeMap(self):       
      self.map = ''.join(str(e) for e in self.state)



def printBoard(board):
  """
    prints the state of the board to the screen in a matrix form

    Parameters
    ----------
    board : list
      a list representing the state of the board

  """
  board = board.state
  if len(board) == 9:
      print("\n".join([" ".join(board[i:i+3]) for i in range(0,len(board),3)]),'\n')
  if len(board) == 16:
      print("\n".join([" ".join(board[i:i+4]) for i in range(0,len(board),4)]),'\n')
  if len(board) == 25:
      print("\n".join([" ".join(board[i:i+5]) for i in range(0,len(board),5)]),'\n')



def makeMatrix(boardList) -> list:
  """
  accepts a list and converts it to a 2 dimensional list,
  returns a two dimensional list

  Parameters
  ----------
  boardList : list
    a list representing the state of the board
 
  """
  if len(boardList) == 9:
      dimensions=[3, 3, 3]
      it = iter(boardList)
      return [list(islice(it, i)) for i in dimensions]

  if len(boardList) == 16:
    dimensions=[4, 4, 4, 4]
    it = iter(boardList)
    return [list(islice(it, i)) for i in dimensions]

  if len(boardList) == 25:
    dimensions=[5, 5, 5, 5, 5]
    it = iter(boardList)
    return [list(islice(it, i)) for i in dimensions] 



def depth(board,f) -> bool:
  """
  attempts to reach the goal state using depth-first search,
  returns a boolean

  Parameters
  ----------
  board : list
    a list representing the state of the board
  f : IO
    output path

  """
  numStates, printed = 0, 0 
  start = timeit.default_timer()   
  visited = set()
  playStack = deque([Puzzle(board,0)])

  while playStack:

    node = playStack.pop()
    visited.add(node.map)
    numStates += 1

    if node.state == node.goal:
      print('Victory!')
      printBoard(node)     
      f.writelines('Puzzle Solved:\n' + str(numStates) + ' states visited\n')
      visited.add(node.map)
      return True

    index = node.state.index('_')

    if printed < 1:
      print('Example: ')
      printBoard(node)
      print('Possible Moves: ')
      printed += 1

    for path in node.legalMoves[index]:          
      tryMove = node.state[:]
      newNode = Puzzle(tryMove,0)      
      newNode.state[index] = newNode.state[path]
      newNode.state[path] = '_'      
      if printed < 5 :        
        printBoard(newNode)
        printed += 1 
      newNode.changeMap()      
        
      if newNode.map not in visited:
        #printBoard(newNode)
        playStack.append(newNode)
        visited.add(newNode.map)
        numStates += 1

    if (timeit.default_timer() - start) > 3600:
      f.writelines('Function timeout: ' + str(timeit.default_timer() - start) + ' seconds' + '\n' + str(numStates) + ' states visited\n')
      return False



def breadth(board,f) -> bool:
  """
  attempts to reach the goal state using breadth-first search,
  returns a boolean

  Parameters
  ----------
  board : list
    a list representing the state of the board
  f : IO
    output path
  """
  numStates, printed = 0, 0 
  start = timeit.default_timer()
  visited = set()
  playQueue = deque([Puzzle(board,0)])  

  while playQueue:

    node = playQueue.popleft()

    visited.add(node.map)
    numStates += 1

    if node.state == node.goal:
      print('Success!')
      f.writelines('Puzzle Solved:\n' + str(numStates) + ' states visited\n')
      visited.add(node.map)
      printBoard(node)
      return True

    index = node.state.index('_') 

    if printed < 1:
      print('Example: ')
      printBoard(node)
      print('Possible Moves: ')
      printed += 1
    
    for path in node.legalMoves[index]:          
      tryMove = node.state[:]
      newNode = Puzzle(tryMove,0)
      newNode.state[index] = newNode.state[path]
      newNode.state[path] = '_'
      if printed < 5 :        
        printBoard(newNode)
        printed += 1  
      newNode.changeMap()     
        
      if newNode.map not in visited:
        playQueue.append(newNode)
        visited.add(newNode.map)
        numStates += 1
    
    if (timeit.default_timer() - start) > 3600:
      f.writelines('Function timeout: ' + str(timeit.default_timer() - start) + ' seconds' + '\n' + str(numStates) + ' states visited\n')
      return False



def sumOfDistance(board,f) -> bool:
  """
  attempts to reach the goal state using A* search,
  returns a boolean

  Parameters
  ----------
  board : list
    a list representing the state of the board
  f : IO
    output path
  """

  global MaxDepth
  numStates, printed = 0, 0 
  start = timeit.default_timer()
  visited = set()
  playQueue = []
  

  node = Puzzle(board,0)
  node.key = manhattan(node)
  node.changeMap()

  playQueue.append(node)

  while(playQueue):

    playQueue.sort(key = lambda x: x.key)

    inPlay = playQueue.pop(0)
    visited.add(inPlay.map)

    if inPlay.state == inPlay.goal:
      print('Success!')
      f.writelines('Puzzle Solved:\n' + str(numStates) + ' states visited\n')
      printBoard(inPlay)
      return True

    index = inPlay.state.index('_')
    
    for path in inPlay.legalMoves[index]:          
      tryMove = inPlay.state[:]
      newNode = Puzzle(tryMove,0)
      newNode.state[index] = newNode.state[path]
      newNode.state[path] = '_'
      newNode.changeMap()    
      if printed < 5 :        
        printBoard(newNode)
        printed += 1         
        
      if newNode.map not in visited:
        key = manhattan(newNode)
        newNode.key = key + newNode.depth
        newNode.changeMap()   
        playQueue.append(newNode)
        visited.add(newNode.map)
        numStates += 1
        if newNode.depth > MaxDepth:
          MaxDepth+=1

      if (timeit.default_timer() - start) > 1800:
        f.writelines('Function timeout: ' + str(timeit.default_timer() - start) + ' seconds' + '\n' + str(numStates) + ' states visited\n')
        return False



def sumOfMisplaced(board,f) -> bool:
  """
  attempts to reach the goal state using a number of misplaced tiles as a heuristic

  Parameters
  ----------
  board : list
    a list representing the state of the board
  f : IO
    output path
  """

  global MaxDepth
  numStates, printed = 0, 0 
  start = timeit.default_timer()
  visited = set()
  playQueue = []
  

  node = Puzzle(board,0)
  node.key = numMisplaced(node)
  node.changeMap()

  playQueue.append(node)

  while(playQueue):

    playQueue.sort(key = lambda x: x.key)

    inPlay = playQueue.pop(0)
    visited.add(inPlay.map)

    if inPlay.state == inPlay.goal:
      print('Success!')
      f.writelines('Puzzle Solved:\n' + str(numStates) + ' states visited\n')
      printBoard(inPlay)
      return True

    index = inPlay.state.index('_')
    
    for path in inPlay.legalMoves[index]:          
      tryMove = inPlay.state[:]
      newNode = Puzzle(tryMove,0)
      newNode.state[index] = newNode.state[path]
      newNode.state[path] = '_'
      newNode.changeMap()    
      if printed < 5 :        
        printBoard(newNode)
        printed += 1         
        
      if newNode.map not in visited:
        key = numMisplaced(newNode)
        newNode.key = key + newNode.depth
        newNode.changeMap()   
        playQueue.append(newNode)
        visited.add(newNode.map)
        numStates += 1
        if newNode.depth > MaxDepth:
          MaxDepth+=1

      if (timeit.default_timer() - start) > 1800:
        f.writelines('Function timeout: ' + str(timeit.default_timer() - start) + ' seconds' + '\n' + str(numStates) + ' states visited\n')
        return False



#calculate distance
def manhattan(node) -> int:
  """
  calculate the path cost of a move using the manhattan 
  search algorithm, returns an int

  Parameters
  ----------
  node : Puzzle object
    object representing a puzzle
 
  """
  distance = 0
  current_matrix = makeMatrix(node.state)
  goal_matrix = makeMatrix(node.goal)  

  for i in range(0,(len(current_matrix))):
      for j in range(0,(len(current_matrix))):
          if current_matrix[i][j] != '_':
              for item in goal_matrix:
                  if current_matrix[i][j] in item:
                      x = goal_matrix.index(item)
                      y = item.index(current_matrix[i][j])
              distance = distance + (abs(x - i) + abs(y - j))

  return distance




#calculate the number of misplaced tiles
def numMisplaced(graph):
  ofp = 0
  if len(graph.state) == 7:
    for x in range(0, 8):
      if graph.state[x] != graph.goal[x]: 
          ofp += 1

  if len(graph.state) == 15:
    for x in range(0, 16):
      if graph.state[x] != graph.goal[x]: 
          ofp += 1

  if len(graph.state) == 24:
    for x in range(0, 25):
      if graph.state[x] != graph.goal[x]: 
          ofp += 1

  return ofp
    
 

def main():

  #fileName = input("Enter name of a text file:\n")
  fileName = "test.txt"    
  game = ([line.rstrip('\n') for line in open(fileName)])
  selection = '0'
  f = open('out.txt', 'a')  

  selection = input('Select an option:\n1) Depth First Search\n2) Breadth First Search\n3) Distance Heuristic\n4)Misplaced Tiles Heuristics\n')    

  if selection == '1':
    f.writelines('\nDepth-First Search:\n')
    start = timeit.default_timer()     
    win = depth(game,f)
    if win:
      f.writelines("Length of execution time: " + str(timeit.default_timer() - start) + '\n')

  elif selection == '2':
    f.writelines('\nBreath-First Search:\n')
    start = timeit.default_timer()
    win = breadth(game,f)    
    if win:
      f.writelines("Length of execution time: " + str(timeit.default_timer() - start) + '\n') 
  elif selection == '3':    
    f.writelines('\nDistance Heuristics:\n')
    start = timeit.default_timer()
    win = sumOfMisplaced(game,f)    
    if win:
      f.writelines("Length of execution time: " + str(timeit.default_timer() - start) + '\n')
  elif selection == '4':    
    f.writelines('\nMisplaced Tile Heuristics:\n')
    start = timeit.default_timer()
    win = sumOfDistance(game,f)    
    if win:
      f.writelines("Length of execution time: " + str(timeit.default_timer() - start) + '\n')


  f.close()
  print('Thanks for Playing!')

  
if __name__=='__main__':
  main()
    