class Solution:

    def helper(self, nums, ind):
        if ind >= len(nums):
            return 0

        return max(nums[ind]+self.helper(nums, ind+2), self.helper(nums, ind+1))

    def rob(self, nums: List[int]) -> int:
        return self.helper(nums, 0)
        