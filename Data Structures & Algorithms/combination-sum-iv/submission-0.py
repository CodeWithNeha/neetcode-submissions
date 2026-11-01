class Solution:
    def helper(self, nums, target, ind, summ):
        if summ == target:
            return 1
        if summ > target:
            return 0
        if ind >= len(nums):
            return 0
        summ += nums[ind]
        return self.helper(nums, target, 0, summ) + self.helper(nums, target, ind+1, summ-nums[ind])
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, 0)
        