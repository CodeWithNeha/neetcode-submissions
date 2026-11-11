class Solution:
    def __init__(self):
        self.dp = [[-1] * 21 for _ in range(1001)]

    def helper(self, nums, ind, total, target):
        if len(nums) == ind:
            return total == target

        if self.dp[ind][total] != -1:
            return self.dp[ind][total]

        self.dp[ind][total] = (
            self.helper(nums, ind + 1, total + nums[ind], target)
            + self.helper(nums, ind + 1, total - nums[ind], target)
        )

        return self.dp[ind][total]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, 0, target)