# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
from typing import List

def maxProfit(prices: List[int]) -> int:
    
    i = 0
    j = 1
    max_profit = 0

    while j < len(prices):

        diff = prices[j] - prices[i]

        if diff < 0:
            i = j

        else:
            max_profit = max(max_profit,diff)

        j += 1

    return max_profit


prices = [7,1,5,3,6,4]
v1 = maxProfit(prices)
print(v1)