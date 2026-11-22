class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimized
        n = len(nums)
        dic = {}
        for i, num in enumerate(nums):
            needed = target-num
            if needed in dic:
                return [dic[needed],i]
            dic[num] = i
    
        return [-1,-1]
        