class Solution:
    def __init__(self):
        self.ans = []
    def helper(self, nums, n ):
        if n == -1:
            self.ans.append([])
            return
        self.helper(nums, n-1)
        copy = [subset[:] for subset in self.ans]

        for subset in copy:
            subset.append(nums[n])

        self.ans.extend(copy)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, len(nums)-1)
        return self.ans
      