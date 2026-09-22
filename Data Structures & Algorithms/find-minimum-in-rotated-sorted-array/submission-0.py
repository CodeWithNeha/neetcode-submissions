class Solution:
    def findPivot(self, nums, start, end):
        while(start<end):
            mid = (start+end)//2
            if nums[mid]>nums[end]:
                start = mid+1
            else:
                end = mid
        return start

    def findMin(self, nums: list[int]) -> int:
        start = 0
        end = len(nums)-1
        pivot = self.findPivot(nums, start, end)
        if nums[pivot]<nums[start]:
            return nums[pivot]
        return nums[start]

        
        