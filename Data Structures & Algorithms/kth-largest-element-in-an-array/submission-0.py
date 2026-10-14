class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force
        nums = sorted(nums, reverse=True)
        return nums[k-1]
        