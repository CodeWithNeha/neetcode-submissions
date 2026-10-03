class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Optimized
        max_profit = float('-inf')
        min_price = float('inf')
        for price in prices:
            min_price = min(price, min_price)
            profit = price-min_price
            max_profit = max(max_profit, profit)
            
        if max_profit<0:
            return 0
        return max_profit


        