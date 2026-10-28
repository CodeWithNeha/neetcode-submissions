class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n<0:
            return 0
        rem1 = n-1
        ans1 = 0
        if rem1>=0:
            ans1 = self.climbStairs(n-1)
        rem2 = n-2
        ans2 = 0
        if rem1>=0:
            ans2 = self.climbStairs(n-2)
        return ans1 + ans2
        