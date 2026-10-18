class Solution:
    def __init__(self):
        self.ans = []
    
    def helper(self, nums, rest):
        if len(rest) == len(nums):
            copi = rest.copy()
            self.ans.append(copi)
            return
        
        for i in range(len(nums)):
            if nums[i] not in rest:
                rest.append(nums[i])
                self.helper(nums, rest)
                rest.pop()
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, [])
        return self.ans
        