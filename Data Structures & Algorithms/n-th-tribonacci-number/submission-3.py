class Solution:
    def __init__(self):
        self.dp = [-1]*38
    def tribonacci(self, n: int) -> int:
        if n <=1:
            return 0 if n!=1 else 1
        if self.dp[n] !=-1:
            return self.dp[n]
        self.dp[n]= self.tribonacci(n-1)+self.tribonacci(n-2)+ self.tribonacci(n-3)
        return self.dp[n]
        