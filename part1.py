import random

count = 0
move_pairs = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

def isSafe(x, y, board):
    if x >= 0 and x < 8 and y >= 0 and y < 8 and board[x][y] == -1:
        return True
    return False

class State:
    def __init__(self, x, y, board):
        global count
        self.x = x
        self.y = y
        self.board = board
        count += 1
        self.moves  = list(self.possible_moves())
    
    def possible_moves(self):
        for (x, y) in move_pairs:
            if isSafe(self.x + x, self.y + y, self.board):
                yield [x, y]

def init(): # initialize board and pick a random starting position
    global count
    count = 0
    board = [[-1 for _ in range(8)]for _ in range(8)]
    states = []
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    board[x][y] = 0
    states.append(State(x, y, board))
    return  states

def move(states):
    last_state = states[count-1]
    if last_state.moves == []:
        return count
    x = last_state.x
    y = last_state.y
    board = last_state.board
    random_move = random.choice(last_state.moves)
    new_x = x + random_move[0]
    new_y = y + random_move[1]
    board[new_x][new_y] = count
    states.append(State(new_x, new_y, board))
    return move(states)
  
   




if __name__ == "__main__":
    total = 0
    p = 45
    for i in range(100000): # run 100000 times
        states = init()
        print("Run {}: starting from ({}, {})".format(i, states[0].x, states[0].y))
        filled_tiles = move(states)
        success = False
        if filled_tiles >= p:
            success = True
        print("{} - Tour length: {}".format( "Successful" if success else "Unsuccessful", filled_tiles))
        for i in range(8):
            print(states[filled_tiles-1].board[i])
       # print("percentage of board filled: ", filled_tiles/64*100, "%")
        total += filled_tiles
    print("average number of tiles filled: ", total/100000)