class Board:
    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for j in range(cols)] for i in range(rows)]

