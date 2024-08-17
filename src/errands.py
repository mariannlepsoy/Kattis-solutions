from collections import defaultdict
from sys import stdin, stdout
from math import dist

# Find distance between two points
def distance(x1, y1, x2, y2):
    return dist([x1, y1], [x2, y2])

# Initialize the graph with distances
def create_graph(places):
    graph = defaultdict(dict)  # The graph with place and distances
    for place1, x1, y1 in places:
        for place2, x2, y2 in places:
            if place1 != place2:
                graph[place1][place2] = distance(x1, y1, x2, y2)
    return graph

# The recursive function to find the best path
def find_best_path(graph, index_to_place, day, mem, bitmask, i):
    # If all places that needs to be visited has been visited already, return home
    if bitmask.bit_count() == (len(graph) - len(day)):
        home_index = index_to_place.index("home")
        return (graph[i][home_index], [])

    # Check memoization
    if (bitmask, i) in mem:
        return mem[(bitmask, i)]
    
    path_dist = float('inf')
    best_path = []

    for place in day: # Go through all places that needs to be visited
        j = index_to_place.index(place)
        
        if bitmask & (1 << j): # Check if place is unvisited
            distance = graph[i][j]

            new_dist, new_path = find_best_path(graph, index_to_place, day, mem, bitmask ^ (1 << j), j)
            new_dist += distance

            if new_dist < path_dist:
                path_dist = new_dist # Update distance
                best_path = [j] + new_path # Update best path

    # Store the result in memoization and return
    mem[(bitmask, i)] = (path_dist, best_path)
    return mem[(bitmask, i)]

# The main solution function
def solution():
    n = int(stdin.readline().strip())
    
    # Read input
    index_to_place = [] # Stores which index each place has, to get the name of places since graph stores them as integers
    places = [] # Stores places (as integers) and their coordinates
    for i in range(n):
        place, x, y = stdin.readline().strip().split()
        x, y = float(x), float(y)
        places.append((i, x, y))
        index_to_place.append(place)

    # Create graph
    graph = create_graph(places)
    
    # Loop through each day's errands
    while True:
        day = stdin.readline().strip().split()
        if day:
            mem = defaultdict(float)
            work_index = index_to_place.index("work")

            _, final_path = find_best_path(graph, index_to_place, day, mem, (1 << n) - 1, work_index)

            # Print result
            for place in final_path:
                stdout.write(f"{index_to_place[place]} ")
            stdout.write("\n")

            print(graph)

        else:
            break

solution()
