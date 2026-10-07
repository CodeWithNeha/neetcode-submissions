class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brute force
        n = len(nums)
        best = float("inf")
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum >= target:
                    best = min(best, end-start+1)
                    break
        return 0 if best == float("inf") else best
                