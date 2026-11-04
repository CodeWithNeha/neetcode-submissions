class Solution:
    def helper(self, cost, ind):
        if ind>=len(cost):
            return 0
        
        one1 = cost[ind] + self.helper(cost, ind+1)
        two2 = cost[ind] + self.helper(cost, ind+2)
        return min(one1, two2)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.helper(cost, 0), self.helper(cost, 1))
        