from sys import stdin, stdout

n = int(stdin.readline().strip())

sequence = stdin.readline().strip().split()
sequence = [int(i) for i in sequence]

count_triples = 0

# Create binary indexed trees for elements on left and right
larger_elements = [0] * (n + 1) # Larger elements to the left
smaller_elements = [0] * (n + 1) # Smaller elements to the right

# Function to update binary indexed tree
def update(tree, index, val):
    while index <= n:
        tree[index] += val
        index += index & -index

# Function to get count from tree
def count(tree, index):
    sum = 0
    while index > 0:
        sum += tree[index]
        index -= index & -index # Increment index by its least significant bit to navigate the binary indexed tree
    return sum

# Initialize tree counting smaller elements to the right of current number with the counts of each number
for num in sequence:
    update(smaller_elements, num, 1)

# Loop through each number in the sequence
for i, num in enumerate(sequence):
    # Remove count from right tree as the number is now at the current index
    update(smaller_elements, num, -1)
    # Count of numbers smaller than the current number to the right
    smaller_count = count(smaller_elements, num - 1)
    # Count of numbers larger than the current number to the left
    larger_count = count(larger_elements, n) - count(larger_elements, num)
    # Update left tree for the current number
    update(larger_elements, num, 1)
    # Add to the inversion count the product of left and right counts
    count_triples += larger_count * smaller_count

stdout.write(str(count_triples))