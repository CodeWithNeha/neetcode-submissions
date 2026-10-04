class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # brute force
        maxi = float('-inf')
        n = len(nums)
        for start in range(n):
            current_sum = 0
            for length in range(n):
                index = (start+length)%n
                current_sum += nums[index]
                maxi = max(maxi, current_sum)
        return maxi
        