class Solution:
    def __init__(self):
        self.dp = [[None]*101 for _ in range(5001)]
    def helper(self, nums, summ, ind):
        if ind >= len(nums):
            if summ * 2 == sum(nums):
                return True
            return False
        if self.dp[summ][ind] is not None:
            return True
        if summ * 2 == sum(nums):
                return True
        self.dp[summ][ind] = self.helper(nums, summ+nums[ind], ind+1) or self.helper(nums, summ, ind+1)
        return self.dp[summ][ind] 

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 !=0:
            return False
        return self.helper(nums, 0, 0)
        