from collections import defaultdict
from sys import stdin, stdout

def best_value():
    y, x = stdin.readline().split()
    y, x = int(y), int(x)
    digits = stdin.readline().strip()
    digits_list = [int(digit) for digit in digits]
    digits_list.append(0)

    grid = []
    for _ in range(x):
        row = stdin.readline().strip()
        grid.append([int(digit) for digit in row])

    mem = defaultdict(int)

    min_value = minimum_value(grid, mem, digits_list, x-1, 0, 0) # Start in bottom left corner
    return min_value


def minimum_value(grid, mem, digits, row, col, key_index):
    # Base cases
    if row == 0 and col == len(grid[0])-1: # Reached end
        return grid[row][col]
    if (row, col, key_index) in mem: # If we already calculated value
        return mem[(row, col, key_index)]
    if row < 0 or col >= len(grid[0]) or key_index >= len(digits): # Out of bounds
        return 90000

    # Find minimum value of taking one step up, right, jumping up or jumping right
    value = min(minimum_value(grid, mem, digits, row, col + 1, key_index),
                minimum_value(grid, mem, digits, row, col + digits[key_index] + 1, key_index+1),
                minimum_value(grid, mem, digits, row-1, col, key_index),
                minimum_value(grid, mem, digits, row - digits[key_index] - 1, col, key_index+1))

    # Update mem with the found minimum value
    mem[(row, col, key_index)] = value + grid[row][col]
    return mem[(row, col, key_index)]

stdout.write(str(best_value()))