from sys import stdin, stdout
from itertools import combinations
    
# Checks orientation of three points. 
def orientation(i, j, k):
    value = (j[1] - i[1]) * (k[0] - j[0]) - (j[0] - i[0]) * (k[1] - j[1])
    if value == 0: # i, j and k are collinear (lie on a single straight line)
        return 0
    elif value > 0: # Clockwise turn (turning right)
        return 1
    else: # Counterclockwise turn (turning left)
        return 2

# Check if line1 and line2 intersect   
def intersect(line1, line2):
    (a, b), (c, d) = line1, line2

    oa = orientation(c, d, a)
    ob = orientation(c, d, b)
    oc = orientation(a, b, c)
    od = orientation(a, b, d)

    if oa != ob and oc != od:
        return True

    return False

# Find all intersections between two lines
def find_intersections(lines):
    intersections = []
    for line1, line2 in combinations(lines, 2):
        if intersect(line1, line2):
            intersections.append((line1, line2))
    return intersections

# Find all triangles
def find_triangles(intersections):
    triangles = set()
    for (line1, line2) in intersections:
        for line3 in lines:
            if line3 != line1 and line3 != line2:
                if intersect(line1, line3) and intersect(line2, line3):
                    # Sort the lines to avoid duplicates
                    triangle = tuple(sorted([line1, line2, line3]))
                    triangles.add(triangle)
    return len(triangles)

outputs = []
while True:

    n = int(stdin.readline().strip())

    if n == 0:
        break

    lines = []
    for _ in range(n):
        x1, y1, x2, y2 = stdin.readline().strip().split()
        lines.append(((float(x1), float(y1)), (float(x2), float(y2))))

    intersections = find_intersections(lines) # All intersections

    count = find_triangles(intersections) # Count of triangles

    outputs.append(count)

for i in outputs:
    stdout.write(f"{i}\n")