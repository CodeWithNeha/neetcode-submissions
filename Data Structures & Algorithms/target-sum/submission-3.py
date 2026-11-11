class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0

        dp = {}

        def helper(ind, total):
            if ind == len(nums):
                return 1 if total == target else 0

            if (ind, total) in dp:
                return dp[(ind, total)]

            dp[(ind, total)] = (
                helper(ind + 1, total + nums[ind])
                + helper(ind + 1, total - nums[ind])
            )

            return dp[(ind, total)]

        return helper(0, 0)