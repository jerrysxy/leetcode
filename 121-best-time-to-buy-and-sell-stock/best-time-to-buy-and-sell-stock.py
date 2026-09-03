class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        biggest_profit = 0

        for price in prices[1:]:
            if price < cheapest:
                cheapest = price

            profit = price - cheapest
            if profit > biggest_profit:
                biggest_profit = profit
        return biggest_profit
            