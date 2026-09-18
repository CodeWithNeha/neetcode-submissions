class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookUp = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in lookUp:
                return [lookUp[compliment], i]
            lookUp[num] = i
        return [-1,-1]
        