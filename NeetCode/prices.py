# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

prices = [10,1,5,6,7,1]

def maxProfit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            potential_profit = price - min_price
            if potential_profit > max_profit:
                max_profit = potential_profit

    return max_profit




print(maxProfit(prices))