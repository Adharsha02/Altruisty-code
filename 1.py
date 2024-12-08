def max_profit(prices):
    # If there are no prices, no profit can be made
    if not prices:
        return 0

    # Initialize variables to track the minimum price and maximum profit
    min_price = float('inf')
    max_profit = 0

    # Loop through the prices to calculate maximum profit
    for price in prices:
        # Update the minimum price seen so far
        if price < min_price:
            min_price = price

        # Calculate potential profit and update maximum profit if higher
        potential_profit = price - min_price
        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit

# Input handling
n = int(input("Enter the number of days: "))
if n <= 0:
    print(0)
else:
    print("Enter the prices:")
    prices = [int(input()) for _ in range(n)]
    # Output the maximum profit
    print(max_profit(prices))
