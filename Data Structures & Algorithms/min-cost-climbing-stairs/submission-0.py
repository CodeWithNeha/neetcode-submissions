class Solution:
    def helper(self, cost, ind):
        if ind >= len(cost):
            return 0

        one_step = cost[ind] + self.helper(cost, ind + 1)
        two_steps = cost[ind] + self.helper(cost, ind + 2)

        return min(one_step, two_steps)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.helper(cost, 0), self.helper(cost, 1))
        