class Solution:
    def __init__(self):
        self.ans = []
    
    def helper(self, nums, current, i):
        if i == len(nums):
            copy = current.copy()
            self.ans.append(copy)
            return
        current.append(nums[i])
        self.helper(nums, current, i+1)
        current.pop()
        self.helper(nums, current, i+1 )

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, [], 0)
        return self.ans

        