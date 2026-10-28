class Solution:
    def __init__(self):
        self.dp = [-1]*45
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n<0:
            return 0
        rem1 = n-1
        ans1 = 0
        if self.dp[rem1] != -1:
            ans1 = self.dp[rem1]
        else:
            if rem1>=0:
                ans1 = self.climbStairs(rem1)
                self.dp[rem1] = ans1
        rem2 = n-2
        ans2 = 0
        if self.dp[rem2]!=-1:
            ans2 = self.dp[rem2]
        else:
            if rem2>=0:
                ans2 = self.climbStairs(rem2)
                self.dp[rem2] = ans2
        return ans1 + ans2
        