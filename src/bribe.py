from sys import stdin, stdout

def solution():
    test_cases = int(stdin.readline().strip())
   
    for _ in range(test_cases):
        # Read input 
        n, c, m = map(int, stdin.readline().strip().split())
        henchmen_bribe = []
        henchmen_probability = []
        for _ in range(n):
            b, p = map(int, stdin.readline().strip().split())
            henchmen_bribe.append(b)
            henchmen_probability.append(p / 100)
        
        # Calculate probability using memoization
        mem = {}
        probability = highest_probability(mem, henchmen_bribe, henchmen_probability, c, m, (1 << n) - 1)

        stdout.write(f"{round(probability, 6)}\n")

def highest_probability(mem, henchmen_bribe, henchmen_probability, henchmen_to_bribe, money_left, bitmask):
    if (henchmen_to_bribe, bitmask) in mem:
        return mem[(henchmen_to_bribe, bitmask)]
    # Base cases
    if money_left < 0 or bitmask.bit_count() < henchmen_to_bribe: # If not enough money or not enough henchmen left
        return 0
    if henchmen_to_bribe == 0: # If we have bribed enough henchmen
        return 1
    
    probability = 0

    for i in range(len(henchmen_bribe)):
        if bitmask & (1 << i):  # Check if the ith henchman is available
            cost, probability_success = henchmen_bribe[i], henchmen_probability[i]
            
            # Probability if we successfully bribe this henchman
            bribe_success = probability_success * highest_probability(mem, henchmen_bribe, henchmen_probability, henchmen_to_bribe - 1, money_left - cost, bitmask ^ (1 << i))

            # Probability if the henchman takes the bribe and runs
            bribe_fail = (1 - probability_success) * highest_probability(mem, henchmen_bribe, henchmen_probability, henchmen_to_bribe, money_left - cost, bitmask ^ (1 << i))
            
            # Update probability considering both scenarios
            probability = max(probability, bribe_success + bribe_fail)

    mem[(henchmen_to_bribe, bitmask)] = probability

    return probability

solution()