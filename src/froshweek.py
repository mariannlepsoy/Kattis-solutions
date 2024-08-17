from sys import stdin, stdout

n = int(stdin.readline().strip())

team = []

for _ in range(n):
    student_number = int(stdin.readline().strip())
    team.append(student_number)

def merge_sort(team):
    # The merge_sort function recursively splits and merges the array
    if len(team) > 1:
        mid = len(team) // 2
        left_half = team[:mid]
        right_half = team[mid:]

        # Recursive call on each half
        swaps = merge_sort(left_half) + merge_sort(right_half)

        # Iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        
        # Merge the two halves and count inversions
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                team[k] = left_half[i]
                i += 1
            else:
                team[k] = right_half[j]
                j += 1
                swaps += (len(left_half) - i) # Counting inversions
            k += 1

        # Copy the remaining elements of left_half
        while i < len(left_half):
            team[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half
        while j < len(right_half):
            team[k] = right_half[j]
            j += 1
            k += 1
        
        return swaps
    else:
        return 0


stdout.write(str(merge_sort(team)))
