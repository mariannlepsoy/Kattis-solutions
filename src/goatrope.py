from sys import stdin, stdout

def find_x_y_distance(x, y, x1, y1, x2, y2):
    if x < x1:
        distance_x = x1 - x

    elif x > x2:
        distance_x = x - x2

    else:
        distance_x = 0

    if y < y1:
        distance_y = y1 - y

    elif y > y2:
        distance_y = y - y2

    else:
        distance_y = 0

    return distance_x, distance_y

def calculate_distance():
    x, y, x1, y1, x2, y2 = stdin.readline().strip().split()
    x, y, x1, y1, x2, y2 = int(x), int(y), int(x1), int(y1), int(x2), int(y2)

    distance_x, distance_y = find_x_y_distance(x, y, x1, y1, x2, y2)

    # Fence post is diagonally away from house
    if distance_x > 0 and distance_y > 0:
        minimum_distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
    
    # Fence post is directly horizontal or vertical to the house
    else:
        minimum_distance = distance_x + distance_y

    return minimum_distance

stdout.write(str(calculate_distance()))