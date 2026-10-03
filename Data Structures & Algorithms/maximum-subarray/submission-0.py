class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        n = len(nums)

        for start in range(n):
            for end in range(start, n):
                total = 0
                for i in range(start, end+1):
                    total += nums[i]
                maxi = max(total, maxi)
        return maxi
        