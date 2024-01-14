import random
import sys

turns = 100000
ps = [0.7, 0.8, 0.85]
ks = [0, 2, 3]

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

def backtrack_tour(board, row, col, step, target_steps):
    if step >= target_steps:  # Target number of steps reached
        return True

    for next_row, next_col in get_possible_moves(board, row, col):
        board[next_row][next_col] = step
        if backtrack_tour(board, next_row, next_col, step + 1, target_steps):
            return True
        board[next_row][next_col] = -1  # Backtrack

    return False

#executes the tour
def execute_tour_part1(p, file):
    #initialize the board
    board = [[-1 for _ in range(8)] for _ in range(8)]
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

def execute_tour_part2(k, p):
    board = [[-1 for _ in range(8)] for _ in range(8)]
    row, col = random.randint(0, 7), random.randint(0, 7)
    board[row][col] = 0

    target_steps = round(64 * p)  # Calculate the target steps based on p

    # Perform k random steps first
    for i in range(k):
        moves = get_possible_moves(board, row, col)
        if not moves:
            return False  # Dead end reached during random steps
        row, col = random.choice(moves)
        board[row][col] = i + 1  # Set step count on the board

    # Now use backtracking from the current position
    return backtrack_tour(board, row, col, k + 1, target_steps)


def part1():
    for p in ps:
        success_count = 0
        with open(f'results_{p}.txt', 'w') as file:
            for i in range(turns): #run 100000 times
                file.write(f"Run {i+1}:\n")
                if execute_tour_part1(p, file): #if the tour is successful
                    success_count += 1 
                file.write("\n")
            probability = success_count / turns
            file.write(f"LasVegas Algorithm With p = {p}\n"
                       f"Number of successful tours: {success_count}\n"
                       f"Number of trials: {turns}\n"
                       f"Probability of a successful tour: {probability:.5f}")
            
def part2():
    results = {}

    for p in ps:
        for k in ks:
            success_count = 0
            for _ in range(turns):
                if execute_tour_part2(k, p):
                    success_count += 1
            probability = success_count / turns
            results[(p, k)] = (success_count, probability)

    for p in ps:
        print(f"--- p = {p} ---")
        for k in ks:
            success_count, probability = results[(p, k)]
            print(f"LasVegas Algorithm With p = {p}, k = {k}\n"
                  f"Number of successful tours: {success_count}\n"
                  f"Number of trials: {turns}\n"
                  f"Probability of a successful tour: {probability:.5f}\n")

#main function
def main():
    if len(sys.argv) != 2:
        print("Run format should be as: python knights_tour.py [part1|part2]\n")
        sys.exit(1)

    if sys.argv[1] == "part1":
        part1()
    elif sys.argv[1] == "part2":
        part2()
    else:
        print("Invalid argument.\n")
    

if __name__ == "__main__":
    main()
