from model.Board import Board
from model import hello_world

board = Board(5, 3)
print(board.rows, board.cols)
print(board.grid[4][2])

hello_world()

b = [2 for i in range(10)]
print(b)

c = [[i+j for i in range(3)] for j in range(3)]
print(c)
