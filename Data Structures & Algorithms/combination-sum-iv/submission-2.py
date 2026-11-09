class Solution:
    def __init__(self):
        self.dp = [[-1]*201 for _ in range(1001)]
    def helper(self, nums, target, ind, summ):
        if summ == target:
            return 1
        if summ > target:
            return 0
        if ind >= len(nums):
            return 0
        if self.dp[summ][ind] !=-1:
            return self.dp[summ][ind]
        self.dp[summ][ind] = self.helper(nums, target, 0, summ + nums[ind]) + self.helper(nums, target, ind+1, summ)
        return self.dp[summ][ind]
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, 0)
        