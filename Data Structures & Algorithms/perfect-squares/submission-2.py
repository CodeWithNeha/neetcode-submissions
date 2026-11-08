class Solution:
    def __init__(self):
        self.dp = [float('inf')]*10001
    def helper(self,target):
        if target ==0:
            return 0
        res = target
        if self.dp[target] != float('inf'):
            return self.dp[target]
        for i in range(1, target+1):
            if i*i > target:
                break
            res = min(res, 1+ self.helper(target-i*i))
        self.dp[target]= res
        return self.dp[target]
    def numSquares(self, n: int) -> int:
        return self.helper(n)
        
