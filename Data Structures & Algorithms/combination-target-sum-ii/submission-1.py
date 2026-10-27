class Solution:
    def __init__(self):
        self.ans = []

    def helper(self, nums, target, used, start):
        if target == 0:
            copied = used.copy()
            self.ans.append(copied)
            return 
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            if nums[i]>target:
                break
            used.append(nums[i])
            self.helper(nums, target-nums[i], used, i+1)
            used.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.helper(candidates, target, [], 0)
        return self.ans
        