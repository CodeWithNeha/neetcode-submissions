class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        max_profit = float('-inf')
        n = len(prices)
        for buy in range(n):
            for sell in range(buy+1, n):
                profit = prices[sell]-prices[buy]
                max_profit = max(max_profit, profit)
                print(max_profit)
        if max_profit<0:
            return 0
        return max_profit


        