class Solution:
    def __init__(self):
        self.dp = [[None]*101 for _ in range(5001)]
    def helper(self, nums, summ, ind):
        if summ * 2 == sum(nums):
            return True
        if ind >= len(nums):
            return False
        if self.dp[summ][ind] is not None:
            return self.dp[summ][ind]
        self.dp[summ][ind] = self.helper(nums, summ+nums[ind], ind+1) or self.helper(nums, summ, ind+1)
        return self.dp[summ][ind] 

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 !=0:
            return False
        return self.helper(nums, 0, 0)
        