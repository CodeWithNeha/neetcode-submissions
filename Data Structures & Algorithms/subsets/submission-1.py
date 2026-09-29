class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            newSubset = []
            for se in subsets:
                newSubset.append(se+[num])
            subsets.extend(newSubset)
        return subsets