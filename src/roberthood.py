from sys import stdin, stdout
from math import sqrt

# Read input into list of coordinates
def read_input():
    n = int(stdin.readline().strip())
    points = []
    for _ in range(n):
        x, y = stdin.readline().strip().split()
        points.append((int(x), int(y)))
    return points

def graham_scan(points):
    points = sorted(set(points))
    s, hull = [], []

    for point in points:
        while len(s) >= 2 and leftturn(s[-2], s[-1], point):
            s.pop()
        s.append(point)
    hull += s

    s = []
    for point in reversed(points):
        while len(s) >= 2 and leftturn(s[-2], s[-1], point):
            s.pop()
        s.append(point)
    hull += s[1:-1]

    return hull

def leftturn(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    
    # Calculate the cross product
    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    
    # If cross product is positive, it is a left turn
    return cross_product > 0

# Find the two points in the convex hull with the biggest distance between them
def max_distance(hull):
    max_dist_sq = 0

    # Compare every pair of points in the convex hull to find maximum distance
    for i in range(len(hull)):
        for j in range(i + 1, len(hull)):
            x1, y1 = hull[i]
            x2, y2 = hull[j]
            dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2 # Find squared distance
            if dist_sq > max_dist_sq: # If new distance is larger than prev distance, replace it
                max_dist_sq = dist_sq

    return sqrt(max_dist_sq)  # Return the square root of the maximum distance found

stdout.write(str(max_distance(graham_scan(read_input()))))