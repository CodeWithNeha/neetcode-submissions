class Solution:
    def __init__(self):
        self.ans = []
    
    def helper(self,nums, target, used, start):
        if target == 0:
            copi = used.copy()
            self.ans.append(copi)
            return
        if target<0:
            return
        
        for i in range(start, len(nums)):
            used.append(nums[i])
            self.helper(nums, target-nums[i], used, i)
            used.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.helper(nums, target, [], 0)
        return self.ans
       

        