class Solution:
    def __init__(self):
        self.dp = [float('inf')]*101
    def helper(self, cost, ind):
        if ind>=len(cost):
            return 0
        if self.dp[ind] != float('inf'):
            return self.dp[ind]
        one1 = cost[ind] + self.helper(cost, ind+1)
        two2 = cost[ind] + self.helper(cost, ind+2)
        self.dp[ind] = min(one1, two2)
        return self.dp[ind]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.helper(cost, 0), self.helper(cost, 1))
        