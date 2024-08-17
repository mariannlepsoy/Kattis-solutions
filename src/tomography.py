from sys import stdin, stdout

def solution():
    # Read input
    n, m = map(int, stdin.readline().strip().split())

    rows = list(map(int, stdin.readline().strip().split()))
    columns = list(map(int, stdin.readline().strip().split()))

    # Sort in decreasing order
    rows.sort(reverse=True)
    columns.sort(reverse=True)

    # Check if matrix construction was possible
    if distribute(rows, columns):
        stdout.write("Yes")
    else:
        stdout.write("No")

# Distribute ones from the rows sums to the column sums
def distribute(rows, columns):
    for r in rows:
        for c in range(r):
            if columns[c] > 0:
                columns[c] -= 1
            else:
                return False # If a column sum goes below zero, the matrix is not possible
        columns.sort(reverse=True)

    if all(c == 0 for c in columns): # If all column sums are zero at the end, the matrix is possible
        return True
    else:
        return False

solution()