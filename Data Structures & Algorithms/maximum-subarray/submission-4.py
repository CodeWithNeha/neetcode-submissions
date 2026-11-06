class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            currSum =  max(nums[i], currSum+nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum

        