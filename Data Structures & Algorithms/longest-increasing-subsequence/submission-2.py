class Solution:
    def __init__(self):
        self.dp = [[-1] * 1001 for _ in range(1001)]

    def helper(self, nums, ind, prev):
        if ind == len(nums):
            return 0
        add = 0
        if self.dp[ind][prev] !=-1:
            return self.dp[ind][prev]
        if prev  == -1 or nums[ind] > nums[prev]:
            add = 1+ self.helper(nums, ind+1, ind)
        add2 = self.helper(nums, ind+1, prev)

        self.dp[ind][prev] = max(add, add2)
        return self.dp[ind][prev]

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(nums, 0, -1)
        