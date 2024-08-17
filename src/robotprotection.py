from sys import stdin, stdout


# Read input and find area
def solution():
    while True:
        n = int(stdin.readline().strip())
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y = stdin.readline().strip().split()
            points.append((int(x), int(y)))

        hull = graham_scan(points)

        a = area(hull)

        stdout.write(f"{a}\n")

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

# Uses the shoelace theorem
def area(hull):
    n = len(hull)
    area = 0.0
    for i in range(n):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    area = abs(area) / 2.0
    return area

solution()