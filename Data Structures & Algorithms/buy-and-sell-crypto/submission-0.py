class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        profit = 0
        for i in range(0, len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = max(profit, prices[i]-minPrice)
        return profit