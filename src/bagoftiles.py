from math import factorial
from sys import stdin, stdout

def solution():
    g = int(stdin.readline().strip())

    for i in range(g):
        # Read input
        total_tiles = int(stdin.readline().strip())
        tiles = list(map(int, stdin.readline().strip().split()))
        drawn_tiles, sum_tiles = map(int, stdin.readline().strip().split())

        # Calculate total number of unique combinations
        total_combinations = factorial(total_tiles) // (factorial(drawn_tiles) * factorial(total_tiles - drawn_tiles))

        # Initialize DP as a 2D list
        count_sums = [[0 for _ in range(sum_tiles + 1)] for _ in range(drawn_tiles + 1)]
        count_sums[0][0] = 1  # Base case

        for tile in tiles:
            for drawn in range(drawn_tiles, 0, -1): # Iterate in reverse to avoid counting a tile more than once
                for j in range(sum_tiles, tile - 1, -1): # Start from maximum sum
                    if count_sums[drawn - 1][j - tile] > 0: # Increment count for sum j using drawn tiles, relying on previously reachable sum j - tile with one less tile.
                        count_sums[drawn][j] += count_sums[drawn - 1][j - tile]
        
        # The number of valid combinations
        valid = count_sums[drawn_tiles][sum_tiles]
        
        # The number of invalid combinations
        invalid = total_combinations - valid

        stdout.write(f"Game {i+1} -- {valid} : {invalid}\n")

solution()