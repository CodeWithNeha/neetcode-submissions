class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_subset = []
            for sub in result:
                new_subset.append(sub + [num])
            result.extend(new_subset)
        return result
        