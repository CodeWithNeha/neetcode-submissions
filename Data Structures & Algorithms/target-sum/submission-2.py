class Solution:
    def __init__(self):
        self.dp = [[-1] * 40001 for _ in range(21)]

    def helper(self, nums, ind, total, target):
        if ind == len(nums):
            return total == target

        if self.dp[ind][total + 20000] != -1:
            return self.dp[ind][total + 20000]

        self.dp[ind][total + 20000] = (
            self.helper(nums, ind + 1, total + nums[ind], target)
            + self.helper(nums, ind + 1, total - nums[ind], target)
        )

        return self.dp[ind][total + 20000]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, 0, target)