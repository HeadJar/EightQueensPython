

#   I got bored
#   Tried the eight queens but in python
#   Think it works
#


import time
import copy

set  = {}

NUMQUEENS = 8
NUM = 0


class gameState(object):
    #Init constructor to set board and numQueens to 0

    def __init__(self):
        self.board = [[0 for x in range(NUMQUEENS)] for y in range(NUMQUEENS)]
        self.numQueens = 0

    #Built in function to print the solution
    def __repr__(self):
        return '\n'.join([''.join(['Q' if self.board[x][y]==1 else '.' if self.board[x][y]==-1 else '.' for x in range(NUMQUEENS)]) for y in range(NUMQUEENS)])

    #This returns the state of the board
    def get(self,x,y):
        return self.board[x][y]
    #
    def solve(self):
        for x in range(NUMQUEENS):
            for y in range(NUMQUEENS):
                if(self.board[x][y] == 1):
                    new_state = copy.deepcopy(self)
                    new_state.place_queen(x,y)
                    return new_state.solve()

    def place_queen(self, x,y):
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


    def copy(self):
        s= gameState()
        s.board = copy.deepcopy(self.board)
        s.numQueens = self.numQueens
        return s

def solve(state=gameState()):
    global NUM
    if state.numQueens == NUMQUEENS:  # Base condition
        #print ('Solution found:')
        #print (state)
        solution = str(state)
        if solution not in (set):
            set[str(state)] = None

            print ('Solution ', NUM +'\n' + solution + '\n\n')
            NUM = NUM + 1
    else:  # Time to recurse
        for x in range(NUMQUEENS):
            for y in range(NUMQUEENS):
                if not state.get(x,y):
                    new_state = state.copy()
                    new_state.place_queen(x, y)
                    solve(new_state)

start_time = time.time()

solve(gameState())

"""
for solution in set.keys():

    print('Solution', NUM)
    print (solution + '\n\n')
    NUM = NUM + 1
"""
print ('%d unique solutions found.' + len(set.keys()))

print ('Elapsed time: %.3fs' + (time.time() - start_time))
