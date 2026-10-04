class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # brute force
        n = len(nums)
        for i in range(n):
            left_sum = 0
            right_sum = 0
            for j in range(i):
                left_sum += nums[j]
            for k in range(i+1, n):
                right_sum += nums[k]
            if left_sum == right_sum:
                return i
        return -1
        