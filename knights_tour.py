import random

#checks if the move is valid
def is_valid_move(board, row, column):
    if row < 0 or row >= 8 or column < 0 or column >= 8:
        return False
    if board[row][column] != -1: #if the cell is already visited
        return False
    return True

#returns a list of possible moves
def get_possible_moves(board, row, column):
    moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
    valid_moves = []
    for move in moves:
        new_row, new_column = row + move[0], column + move[1]
        if is_valid_move(board, new_row, new_column):
            valid_moves.append((new_row, new_column))
    return valid_moves

#executes the tour
def execute_tour(p, file):
    #initialize the board
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(-1)
        board.append(row)
    row, column = random.randint(0, 7), random.randint(0, 7) #randomly choose a cell
    board[row][column] = 0 #mark the cell as visited
    step = 1 
    file.write(f"Run starting from ({row},{column})\n")

    while True:
        moves = get_possible_moves(board, row, column) #get possible moves
        if not moves: #if there is no possible move
            break
        row, column = random.choice(moves) #randomly choose a move
        board[row][column] = step #mark the cell as visited
        file.write(f"Stepping into ({row},{column})\n")
        step += 1 #increase the step

    success = step >= round(64 * p) 
    status = "Successful" if success else "Unsuccessful"
    file.write(f"{status} - Tour length: {step}\n")
    for row in board:
        file.write(" ".join(str(cell) for cell in row) + "\n")
    return success

#main function
def main():
    ps = [0.7, 0.8, 0.85]
    for p in ps:
        success_count = 0
        with open(f'results_{p}.txt', 'w') as file:
            for i in range(100000): #run 100000 times
                file.write(f"Run {i+1}:\n")
                if execute_tour(p, file): #if the tour is successful
                    success_count += 1 
                file.write("\n")
            probability = success_count / 100000
            file.write(f"LasVegas Algorithm With p = {p}\nNumber of successful tours: {success_count}\n"
                       f"Number of trials: 100000\nProbability of a successful tour: {probability:.5f}")

if __name__ == "__main__":
    main()
