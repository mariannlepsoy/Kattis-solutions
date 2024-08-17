from sys import stdin, stdout
from collections import deque

#Bfs where you start with first input and check all clicks.
def bfs():
    start = stdin.readline().strip()
    end = stdin.readline().strip()
    start, end = letters_to_integer(start), letters_to_integer(end)
    visited = set()
    queue = deque([(start, 0)]) 

    while queue:
        current_word, rounds = queue.popleft()
        if current_word == end:
            return rounds

        for i in range(0,8):
            new_word = clicked(i, current_word[i], current_word)
            new_word_tuple = tuple(new_word)
            if new_word_tuple not in visited:
                visited.add(new_word_tuple)
                queue.append((new_word, rounds+1))
    return -1

# Turn string of letters into list of numbers, A=0 ... F=5.
def letters_to_integer(word):
    result = []
    for letter in word:
        number = ord(letter) - 65
        result.append(number)
    return result

# Performs rotations based on letter and index.
def clicked(index, letter, current_word):
    new_word = current_word.copy()

    if letter == 0:
        if index != 0:
            rotate(new_word, index-1)
        if index != 7:
            rotate(new_word, index+1)
            
    elif letter == 1:
        if index != 0 and index != 7:
            new_word[index+1] = new_word[index-1]

    elif letter == 2:
        rotate(new_word, 7-index)

    elif letter == 3:
        if index < 4:
            for i in range(0, index):
                rotate(new_word, i)
        elif index >= 4:
            for i in range(index+1, 8):
                rotate(new_word, i)

    elif letter == 4:
        if index != 0 and index != 7:
            if index < 4:
                y = index
                rotate(new_word, index - y)
                rotate(new_word, index + y)
            elif index >= 4:
                y = 7 - index
                rotate(new_word, index - y)
                rotate(new_word, index + y)

    elif letter == 5:
        i = index + 1
        if i % 2 == 1:
            rotate(new_word, ((i + 9) // 2) - 1)
        else:
            rotate(new_word, (i // 2) - 1)
    
    return new_word

# Increase number at index by 1. Mod 6 to make sure the number is never higher than 5 (F).            
def rotate(word, index):
    word[index] = (word[index]+1)%6
    
stdout.write(str(bfs()))