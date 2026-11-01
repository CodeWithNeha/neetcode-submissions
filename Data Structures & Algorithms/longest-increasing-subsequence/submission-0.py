class Solution:
    def __init__(self):
        self.dp = [[-1] * 1001 for _ in range(1001)]

    def helper(self, nums, res, ind):
        if ind == len(nums):
            return 0
        add = 0
        # if self.dp[ind][len(res)] !=-1:
        #     return self.dp[ind][len(res)]
        if not res or nums[ind] > res[-1]:
            res.append(nums[ind])
            add = 1+ self.helper(nums, res, ind+1)
            res.pop()
        add2 = self.helper(nums, res, ind+1)

        # self.dp[ind][len(res)] = 
        return max(add, add2)

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(nums, [], 0)
        