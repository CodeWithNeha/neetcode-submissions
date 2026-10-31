class Solution:
    def __init__(self):
        self.dp = [float('inf')]*100
    def helper(self, cost, ind):
        if ind >= len(cost):
            return 0
        if self.dp[ind] != float('inf'):
            return self.dp[ind]

        one_step =  cost[ind] + self.helper(cost, ind + 1)
        two_steps=  cost[ind] + self.helper(cost, ind + 2)

        self.dp[ind] = min(one_step, two_steps)
        return self.dp[ind]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.helper(cost, 0), self.helper(cost, 1))
        