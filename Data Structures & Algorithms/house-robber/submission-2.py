class Solution:
    def __init__(self):
        self.ans = [-1]*101

    def helper(self, nums, ind):
        if ind >= len(nums):
            return 0
        if self.ans[ind] != -1:
            return self.ans[ind]
        
        self.ans[ind] = max(nums[ind]+self.helper(nums, ind+2), self.helper(nums, ind+1))
        return self.ans[ind]

    def rob(self, nums: List[int]) -> int:
        return self.helper(nums, 0)
        