from sys import stdin, stdout
from itertools import product

# Calculates the number of pieces on the current board that are out of place compared to the end board
def difference_count(current_board, end_board):
    diff_count = 0
    for (i, j) in product(range(5), range(5)):
        if end_board[i][j] == " ":
            continue
        elif current_board[i][j] != end_board[i][j]:
            diff_count += 1
    return diff_count

# Search function to find if the goal state is reachable within max_difference moves
def dfs(board, empty, max_moves, end_board, moves, swaps=0):
    distance_to_goal = difference_count(board, end_board)
    if distance_to_goal == 0:
        return True
    if distance_to_goal + swaps > max_moves:
        return False

    for move in moves:
        new_empty = (empty[0] + move[0], empty[1] + move[1])
        # Check that move is within bounds
        if 0 <= new_empty[0] < 5 and 0 <= new_empty[1] < 5:
            # Perform the move
            board[empty[0]][empty[1]], board[new_empty[0]][new_empty[1]] = board[new_empty[0]][new_empty[1]], board[empty[0]][empty[1]]
            # Recursive search
            result = dfs(board, new_empty, max_moves, end_board, moves, swaps + 1)
            # Undo the move
            board[new_empty[0]][new_empty[1]], board[empty[0]][empty[1]] = board[empty[0]][empty[1]], board[new_empty[0]][new_empty[1]]
            
            if result:
                return True
    return False

# Read input and output the result
def solve():
    # The final goal state as a 2D list
    end_board = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, " ", 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]

    # List of moves a knight can make
    moves = [(2, 1), (1, 2), (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (2, -1)]

    n = int(stdin.readline().strip())
    for _ in range(n):
        # Read input
        board = []
        empty = " "
        for i in range(5):
            row = list(stdin.readline().strip())
            if len(row) < 5:  # Check if row length is less than 5, meaning empty space is on the edge
                row.extend([" "])
            board.append([1 if x == '1' else 0 if x == '0' else " " for x in row])
            if " " in board[-1]:
                empty = (i, board[-1].index(" "))

        # Check if there is a solution
        for max_moves in range(11):
            if dfs(board, empty, max_moves, end_board, moves):
                stdout.write(f"Solvable in {max_moves} move(s).\n")
                break
        
        else:
            stdout.write("Unsolvable in less than 11 move(s).\n")

solve()