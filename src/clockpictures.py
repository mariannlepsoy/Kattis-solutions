from sys import stdin, stdout

def solution():
    clock = 360000

    hands = int(stdin.readline().strip())

    first_clock = list(map(int, stdin.readline().strip().split()))
    second_clock = list(map(int, stdin.readline().strip().split()))

    first_clock.sort()
    second_clock.sort()

    # Lists of angles for the hands of the two clocks
    first_angles = []
    second_angles = []

    for i in range(hands-1):
        first_angles.append(abs(first_clock[i] - first_clock[i + 1]))
        second_angles.append(abs(second_clock[i] - second_clock[i + 1]))

    first_angles.append((clock - first_clock[-1]) + first_clock[0])
    second_angles.append((clock - second_clock[-1]) + second_clock[0])

    second_angles_double = second_angles + second_angles

    if kmp(first_angles, second_angles_double):
        stdout.write("possible")
    else:
        stdout.write("impossible")
    

def kmp(first_angles, second_angles_double):
    n = len(first_angles)
    m = len(second_angles_double)
    
    # Find longest prefix sum
    longest_prefix_sum = [0] * n
    j = 0
    i = 1
    while i < n:
        if first_angles[i] == first_angles[j]:
            j += 1
            longest_prefix_sum[i] = j
            i += 1
        else:
            if j != 0:
                j = longest_prefix_sum[j - 1]
            else:
                longest_prefix_sum[i] = 0
                i += 1
    
    # Knut-Morris-Pratt algorithm
    i = 0 # First angles index
    j = 0 # Second angles index
    while i < m:
        if first_angles[j] == second_angles_double[i]:
            i += 1
            j += 1
        
        if j == n:
            return True
        elif i < m and first_angles[j] != second_angles_double[i]:
            if j != 0:
                j = longest_prefix_sum[j - 1]
            else:
                i += 1
    return False
    
solution()