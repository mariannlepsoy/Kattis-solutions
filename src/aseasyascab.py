from sys import stdin, stdout

def print_alphabet():
    highest_letter, n = stdin.readline().split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    characters = alphabet[:alphabet.rfind(highest_letter)+1]
    all_lines = read_all_lines(n)
    prefix = [False]
    #Two graphs: outedges (children) and inedges (parents)
    outedges, inedges = create_graph_outedges(all_lines, n, characters, prefix)
    new_alphabet = []
    visited = []
    current_path = []
    cycle = [False]
    #All nodes without parents.
    roots = find_nodes(inedges)
    #All nodes without children.
    end_nodes = find_nodes(outedges)

    #Run dfs
    for root in roots:
        if root not in visited:
            dfs(root, outedges, visited, new_alphabet, current_path, cycle)

    new_alphabet_string = create_alphabet(new_alphabet)

    if cycle[0] == True or len(roots) == 0 or prefix[0] == True:
        return "IMPOSSIBLE"
    elif len(roots) > 1 or len(end_nodes) > 1 or len(characters) > len(new_alphabet_string):
        return "AMBIGUOUS"
    else:
        return new_alphabet_string

# Read all lines as a list
def read_all_lines(n):
    all_lines = []
    for _ in range(int(n)):
        line = stdin.readline()
        all_lines.append(line.strip())
    return all_lines

# Find first differing character between word1 and word2.
# Create outedge between the letters in a dictionary.
def create_graph_outedges(all_lines, n, characters, prefix):
    outedges = {char: [] for char in characters}
    inedges = {char: [] for char in characters}
    for i in range(int(n)-1):
        word1 = all_lines[i] 
        word2 = all_lines[i+1]

        #Checks if word1 is a prefix of word2, if so it should be impossible.
        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            prefix[0] = True
            break
        
        #Compare two and two characters until one differing one can be found.
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                outedges[word1[j]].append(word2[j])
                inedges[word2[j]].append(word1[j])
                break
    return outedges, inedges

# dfs search to create alphabet.
def dfs(letter, outedges, visited, new_alphabet, current_path, cycle):
    current_path.append(letter)
    visited.append(letter)
    if letter in outedges:
        for neighbor in outedges[letter]:
            #Check for cycle. If cycle it should be impossible.
            if neighbor in current_path:
                cycle[0] = True
            if neighbor not in visited:
                dfs(neighbor, outedges, visited, new_alphabet, current_path, cycle)
    new_alphabet.append(letter)
    current_path.remove(letter)

#Creates new alphabet.
def create_alphabet(new_alphabet):
    new_alphabet = new_alphabet[::-1]
    return ''.join(new_alphabet)

#Check for more than one key with empty list as value. Used for AMBIGUOUS case.
def find_nodes(edges):
    list = []
    for letter in edges:
        if len(edges[letter]) == 0:
            list.append(letter)
    return list

stdout.write(print_alphabet())