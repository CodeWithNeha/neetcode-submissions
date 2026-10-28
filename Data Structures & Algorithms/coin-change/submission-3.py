class Solution:


    def helper(self, coins, ind, amount):
       
        if amount == 0:
            return 0
        if ind>=len(coins):
            return float('inf')
        if self.dp[ind][amount]!=-1:
            return self.dp[ind][amount]
        remaining = amount - coins[ind]
        ans = float('inf')
        if remaining>=0:
            ans = 1+ self.helper(coins, ind, remaining)
            ans = min(1+self.helper(coins, ind+1, remaining), ans)
        ans = min(ans, self.helper(coins, ind+1, amount))
        self.dp[ind][amount] = ans
        return ans
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [
            [-1] * (amount + 1)
            for _ in range(len(coins))
        ]
        ans = self.helper(coins, 0, amount)
        if ans >= float('inf'):
            return -1
        return ans