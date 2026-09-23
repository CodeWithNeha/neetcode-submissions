class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i]>nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums
        