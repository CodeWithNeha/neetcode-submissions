class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # optimized
        return len(nums)!=len(set(nums))