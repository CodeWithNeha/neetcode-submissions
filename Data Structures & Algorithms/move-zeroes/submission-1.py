class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Optimized
        index = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index] = nums[i]
                index+=1
        while index<len(nums):
            nums[index] = 0
            index+=1