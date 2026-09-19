class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = [0]*(len(nums)*2)
        ind = 0
        for i in range(len(nums2)):
            if ind == len(nums):
                ind = 0
            nums2[i] = nums[ind]
            ind+=1
        return nums2
        