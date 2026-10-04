class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force
        maxi = float('-inf')
        n = len(nums)
        for start in range(n):
            product = 1
            for end in range(start, n):
                product *=nums[end]
                maxi = max(maxi, product)
        return maxi
        