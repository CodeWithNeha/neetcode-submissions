class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force
        count = 0
        for start in range(len(nums)):
            current_sum = 0
            for end in range(start, len(nums)):
                current_sum += nums[end]
                if current_sum == k:
                    count+=1
        return count