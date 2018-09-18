

import time
import copy

set  = {}

NUMQUEENS = 8


class gameState(object):
    def __init__(self):
        self.board =  [[0 for x in range(NUMQUEENS)], [0 for y in (NUMQUEENS)]]
        self.numQueens = 0

    def __repr__(self):
        return '\n'.join([''.join(['Q' if self.board[x][y]==1 else '.' if self.board[x][y]==-1 else '.' for x in range(NUMQUEENS)]) for y in range(NUMQUEENS)])

    def __get__(self,x,y):
        return self.board[x][y]

    def solve(self):
        for x in range(NUMQUEENS):
            for y in range(NUMQUEENS):
                if(self.board[x][y] == 1):
                    new_state = copy.deepcopy(self)
                    new_state.place_queen(x,y)
                    return new_state.solve()

    def place_queen(x,y):
        assert x in  range(NUMQUEENS) and y in range(NUMQUEENS) and not self.board[x][y]
        self.board[x][y] = 1
        self.numQueens +=  1
        for i in range(NUMQUEENS):
            if not self.board[i][y]:
                self.board[i][y] = -1
            if not self.board[x][i]:
                self.board[x][i] = -1
            if x+i in range(NUMQUEENS) and y+i in range(NUMQUEENS) and not self.board[x+i][y+i] :
                self.board[x+i][y+i] = -1
            if x-i in range(NUMQUEENS) and y-i in range(NUMQUEENS) and not self.board[x-i][y-i] :
                self.board[x-i][y-i] = -1
            if x-i in range(NUMQUEENS) and y+i in range(NUMQUEENS) and not self.board[x-i][y+i] :
                self.board[x-i][y+i] = -1
            if x+ i in range(NUMQUEENS) and y-i in range(NUMQUEENS) and not self.board[x+i][y-i] :
                self.board[x+i][y-i] = -1
