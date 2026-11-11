class Solution:
    def helper(self, nums, ind, total, target):
        if len(nums) == ind:
            return total == target
        
        return self.helper(nums, ind+1, total+nums[ind], target)+ self.helper(nums, ind+1, total-nums[ind], target)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, 0, target)


        