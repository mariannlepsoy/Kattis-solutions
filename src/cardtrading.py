from sys import stdin, stdout

def find_profit():
    #Number of cards in deck, T highest card in deck and K number of combos.
    n, t, k = stdin.readline().split()
    n, t, k = int(n), int(t), int(k)
    #Cards on Anthony's hand, in the form of list of integers.
    hand = list(map(int, stdin.readline().strip().split()))
    hand.sort()
    #Count amount of each card type
    n_per_card_type = count_each_card(hand, t)
    #Prices for selling and buying each card type
    card_prices = price(t, n_per_card_type)

    #Find maximum profit.
    max_profit = 0
    #Buy cards.
    for card in range(k):
        max_profit -= card_prices[card][0]
    #Sell cards.
    for card in range(k, t):
        max_profit += card_prices[card][1]

    stdout.write(str(max_profit))

#Find how many of each card exist in hand.
def count_each_card(hand, t):
    cards = [0] * t
    for i in hand:
        cards[i-1] += 1
    return cards

#Create a list of buy and sell price for each card type, taking into account how many cards of each type we have before.
def price(t, count):
    card_price = []
    for i in range(t):
        buy, sell = stdin.readline().split()
        card_price.append((int(buy) * (2 - count[i]), int(sell) * count[i]))
    #Sort cards by combined buy and sell price, indicating which items are cheaper to buy and most profitable to sell. If equal, sort by buy price.
    card_price = sorted(card_price, key=lambda x: (x[0] + x[1], x[0]))
    return card_price

find_profit()