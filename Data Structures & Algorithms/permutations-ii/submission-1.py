class Solution:
    def __init__(self):
        self.ans = []
    def helper(self, nums, used, visited):
        if len(used) == len(nums):
            copied = used.copy()
            self.ans.append(copied)
            return

        for i in range(len(nums)):
            if visited[i] or (i>0 and nums[i]==nums[i-1] and not visited[i-1]):
                continue
            else:
                used.append(nums[i])
                visited[i] = True
                self.helper(nums, used, visited)
                used.pop()
                visited[i] = False
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False]*len(nums)
        self.helper(nums, [], visited)
        return self.ans

        