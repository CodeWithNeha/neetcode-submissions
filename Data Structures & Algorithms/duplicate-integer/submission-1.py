class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = []
        for i in range(0, len(nums)):
            if nums[i] in li:
                return True
            li.append(nums[i])
        return False      