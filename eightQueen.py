

import time
import copy

set  = {}

NUMQUEENS = 8


class gameState(object):
    def __init__(self):
        self.board =  [[0 for x in range(NUMQUEENS)], [0 for y in (NUMQUEENS)]]
        self.queesPlace = 0

    def __repr__(self):
        return '\n'.join([''.join(['Q' if self.board[x][y]==1 else '.' if self.board[x][y]==-1 else '.' for x in range(NUMQUEENS)]) for y in range(NUMQUEENS)])

    def __get__(self,x,y):
        return self.board[x][y]

    def solve(self):
        for x in range(NUMQUEENS):
            for y in range(NUMQUEENS):
                if(self.board[x][y] == 1):
                    new_state = copy.deepcopy(self)
                    new_state.place_queen
