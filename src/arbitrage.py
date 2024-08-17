from sys import stdin, stdout
import math

def arbitrage():
    output = [] #
    while True:
        edges = []
        number_currencies = int(stdin.readline().strip()) # Number of currencies in test case
        if number_currencies == 0: # No more test cases
            break
        currency_codes = stdin.readline().strip().split() # List of all currrency codes
        
        number_exchange_rates = int(stdin.readline().strip()) # Number of exchange rates in test case

        if number_exchange_rates == 1: # If there is only 1 exchange rate, read it but don't process for arbitrage
            stdin.readline().strip() # Read and discard this line
            output.append("Ok")

        elif number_exchange_rates == 0: # If there are no exchange rates
            output.append("Ok")

        else:
            for _ in range(number_exchange_rates): # Add all exchange rates as values (edges) to dictionary
                exchange_rates = stdin.readline().strip().split()
                from_currency = exchange_rates[0]
                to_currency = exchange_rates[1]
                exchange_rate = exchange_rates[2].split(':')
                weight = math.log(int(exchange_rate[0]) / int(exchange_rate[1]))

                edges.append((from_currency, to_currency, weight))

            if bellman_ford(edges, currency_codes, number_currencies, number_exchange_rates):
                output.append("Arbitrage")
            else:
                output.append("Ok")

    for word in output:
        stdout.write(f"{word}\n")

def bellman_ford(edges, currency_codes, number_currencies, number_exchange_rates):
    distances = {currency: float('inf') for currency in currency_codes} # Keep track of shortest distance from source to all other nodes, initialized as infinet.

    # Loop through all nodes.
    for v in range(number_exchange_rates):
        source_node = edges[v][0] # Choose current node from loop as source node
        distances[source_node] = 0
        for _ in range(number_currencies-1): # Find shortest path from source to all other nodes
            for e in range(number_exchange_rates): # Go through all edges
                if distances[edges[e][0]] + edges[e][2] < distances[edges[e][1]]: # If the path from currency + the weight of the edge to to_currency is less than the current path to to_currency, update the path.
                    distances[edges[e][1]] = distances[edges[e][0]]+ edges[e][2]
                
        # Check for negative weight cycles. 
        # If we have updated the shortest distance to each currency and if we can still find an edge that would make the distance to the currancy shorter, it indicates a negative cycle.
        # This is because we then have a loop that keeps reducing the path.
        for e in range(number_exchange_rates): 
            if distances[edges[e][0]] + edges[e][2] < distances[edges[e][1]]:
                return True

    return False # If no negative cycle is detected.

arbitrage()