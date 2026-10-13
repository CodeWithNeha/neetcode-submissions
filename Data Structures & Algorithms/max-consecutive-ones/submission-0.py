class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = float("-inf")
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                count = 0
            maxi = max(count, maxi)
        return maxi
        