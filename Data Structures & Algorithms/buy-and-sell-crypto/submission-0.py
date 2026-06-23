class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices[i] = 1 NeetCoin
        #I could buy it today, tomorrow, etc, but I can only sell it after I buy it
        #Goal: return max profit you can achieve.
        #Cannot make any transactions in which profit = 0
        minimum_price = prices[0]
        potential_profit = 0
        for n in prices:
           minimum_price = min(n, minimum_price)
           potential_profit = max(n - minimum_price, potential_profit)
        
        return potential_profit

        