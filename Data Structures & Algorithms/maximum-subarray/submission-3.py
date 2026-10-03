class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # optimized (Kedann's Algo)
        current = nums[0]
        maxi = nums[0]
        n = len(nums)

        for i in range(1,n):
            current = max(nums[i], current+nums[i])
            maxi = max(current, maxi)
        return maxi
        