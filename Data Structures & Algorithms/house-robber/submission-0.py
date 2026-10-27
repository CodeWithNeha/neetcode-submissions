class Solution:
    def __init__(self):
        self.maxi = float('-inf')

    def helper(self, nums, ind, ans):
        if ind >len(nums):
            self.maxi = max(ans, self.maxi)
            return
        if ind<=len(nums):
            self.maxi = max(ans, self.maxi)
        
        for i in range(ind,len(nums)):
            ans += nums[i]
            ind = i+ 2
            self.helper(nums, ind, ans)
            ans -= nums[i]

    def rob(self, nums: List[int]) -> int:
        self.helper(nums, 0, 0)
        return self.maxi
        