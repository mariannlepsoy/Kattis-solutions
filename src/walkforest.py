from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin, stdout

def walkforest():
    output = []
    while True:
        edges = defaultdict(list)
        first_line = stdin.readline().strip()
        if first_line == "0":
            break
        n_intersections, n_paths = first_line.split()
        n_intersections, n_paths = int(n_intersections), int(n_paths)

        for _ in range(n_paths):
            path = stdin.readline().strip().split()

            a = int(path[0])
            b = int(path[1])
            value = int(path[2])

            edges[a].append((b, value))
            edges[b].append((a, value))

        distances = dijkstra(edges, n_intersections)

        mem = defaultdict(int)
        mem[2] = 1

        count = routes(1, edges, distances, mem)

        output.append(count)

    for i in output:
        stdout.write(f"{i}\n")

def routes(intersection, edges, distances, mem):
    if intersection in mem:
        return mem[intersection]
    
    count = 0

    for neighbour, _ in edges[intersection]:
        if isShorter(intersection, neighbour, distances):
            count += routes(neighbour, edges, distances, mem)

    mem[intersection] = count
    return mem[intersection]

# Find shortest path from home to all intersections
def dijkstra(edges, n_intersections):
    distances = {intersection: float('inf') for intersection in range(1, n_intersections + 1)} # Initialize all distances to infinity
    source = 2
    distances[source] = 0 # Set distance from source to source as 0
    priority_queue = [(0, source)] # Add source to priority queue. Queue will sort by distance.

    while priority_queue:
        current_distance, current_intersection = heappop(priority_queue)

        # If current distance is shorter than larger than saved distance, we have already found a shorter path and ignore current distance.
        if current_distance > distances[current_intersection]:
            continue
    
        # Loop through all neighbour of current intersection
        for neighbour, weight in edges[current_intersection]:
            distance = current_distance + weight # Calculate new distance if we go through current intersection
            if distance < distances[neighbour]: # If new distance is lower than saved distance, update it.
                distances[neighbour] = distance
                heappush(priority_queue, (distance, neighbour)) # Add neighbour to priority queue

    return distances
    

# Check if a path is progress
def isShorter(current, next, distances):
    if distances[next] < distances[current]:
        return True
    else:
        return False

walkforest()