class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in lookup:
                return [lookup[needed], i]
            lookup[num] = i
        return [-1, -1]
        