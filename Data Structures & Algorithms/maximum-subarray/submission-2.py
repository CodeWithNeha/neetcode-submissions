class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # optimized
        maxi = float('-inf')
        n = len(nums)

        for start in range(n):
            total = 0
            for end in range(start, n):
                total += nums[end]
                maxi = max(total, maxi)
        return maxi
        