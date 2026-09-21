class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n+1):
            xor = xor^i
        for i in range(n):
            xor = xor^nums[i]
        return xor