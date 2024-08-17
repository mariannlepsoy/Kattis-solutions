from collections import defaultdict
from sys import stdin, stdout

def solution():
    # Reads input
    n, m = stdin.readline().strip().split()
    n, m = int(n), int(m)

    pairs = defaultdict(list) 

    for _ in range(m):
        player1, player2 = stdin.readline().strip().split()
        player1, player2 = int(player1), int(player2)

        pairs[player1].append(player2)
        pairs[player2].append(player1)

    # Maximum bipartite matching

    target = [0] * (n+1) # List to keep track of each players target
    matches = 0 # Keep track of how many matches are made between players

    # Look for a match (target) for each player
    for player in pairs:
        visited = set()

        if dfs(pairs, visited, player, target):
            matches += 1

    if matches < n: # Not possible to get a target for everyone
        stdout.write("Impossible")

    else: # Possible to get a target for everyone
        for i in range(1, n+1):
            stdout.write(f"{target[i]}\n")

def dfs(pairs, visited, player1, target):
    
    for player2 in pairs[player1]: # Check players that player1 can see

        if player2 not in visited: # Check that player2 two has not already been visited by player1
            visited.add(player2)

            # Check that player2 is not matched with anyone or if player2 has been matched, check if player2's match can find a new match
            if player2 not in target or dfs(pairs, visited, target.index(player2), target):
                target[player1] = player2 # Assign player2 as a match for player1
                return True # True if a match was made
            
    return False # False if player1 cannot be matched

solution()