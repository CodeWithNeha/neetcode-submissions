class Solution:
   
    
    def helper(self, coins, amount, ind):
        if amount == 0:
            return 1
        if ind>=len(coins):
            return 0
        
        remaining = amount-coins[ind]
        ans = 0
        if self.dp[ind][amount]!=-1:
            return self.dp[ind][amount]
        if remaining >= 0:
            ans = self.helper(coins, remaining, ind) 
        ans += self.helper(coins, amount, ind+1)
        self.dp[ind][amount] = ans
        return ans

    def change(self, amount: int, coins: List[int]) -> int:
        self.dp = [
            [-1] * (amount + 1)
            for _ in range(len(coins))
        ]
        return self.helper(coins, amount, 0)
        