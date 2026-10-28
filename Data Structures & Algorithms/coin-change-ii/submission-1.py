class Solution:
    def __init__(self):
        self.dp = [[-1]*10001 for i in range(0,11 )]
    
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
        return self.helper(coins, amount, 0)
        