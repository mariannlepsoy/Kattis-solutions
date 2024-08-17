from collections import defaultdict
from sys import stdin, stdout

def best_possible_value():
    n, k = stdin.readline().split()
    n, k = int(n), int(k)

    gallery = create_gallery(n)
    mem = defaultdict(int)
    
    total_value = sum(sum(room) for room in gallery)
    max_value = total_value - minimum_value(gallery, mem, k, n - 1, 0)
    return max_value

#Create gallery as list of lists
def create_gallery(n):
    gallery = []
    for _ in range(n):
        left, right = stdin.readline().split()
        gallery.append([int(left), int(right)])
    return gallery


def minimum_value(gallery, mem, rooms_to_close, room_index, last_closed):
    # Define constants for room closure status
    none, right, left = 0, 1, 2

    #Base cases
    if rooms_to_close == 0: #If no rooms need to close, minimum value is 0.
        return 0
    if room_index == -1: #If we run out of rooms, minimum value is largest possible value
        return 20000
    if (rooms_to_close, room_index, last_closed) in mem: #Returns current value if result for current value has been computed
        return mem[(rooms_to_close, room_index, last_closed)]
    
    min_value = minimum_value(gallery, mem, rooms_to_close, room_index - 1, none) #Value for not closing any room
    
    if last_closed == right: #If last room closed was right, close either a right or no room next
        min_value = min(min_value, minimum_value(gallery, mem, rooms_to_close - 1, room_index - 1, right) + gallery[room_index][1])
    elif last_closed == left: #If last room closed was left, close either a left or no room next
        min_value = min(min_value, minimum_value(gallery, mem, rooms_to_close - 1, room_index - 1, left) + gallery[room_index][0])
    else: #If no room was closed, can close either left, right or no room
        right_closed = minimum_value(gallery, mem, rooms_to_close - 1, room_index - 1, right) + gallery[room_index][1]
        left_closed = minimum_value(gallery, mem, rooms_to_close - 1, room_index - 1, left) + gallery[room_index][0]
        min_value = min(min_value, min(right_closed, left_closed))
    
    #Update mem with minimum value found
    mem[(rooms_to_close, room_index, last_closed)] = min_value
    return min_value

stdout.write(str(best_possible_value()))