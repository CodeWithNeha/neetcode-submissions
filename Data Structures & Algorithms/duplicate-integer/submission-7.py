class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in range(0, len(nums)):
            if nums[i] in freq:
                return True
            freq[nums[i]] = i
        return False