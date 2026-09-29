class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        subsets = [[]]
        for num in nums:
            newSubset = []
            for se in subsets:
                newSubset.append(se+[num])
            subsets.extend(newSubset)
        total = 0

        for subset in subsets:
            xor = 0

            for num in subset:
                xor ^= num

            total += xor

        return total