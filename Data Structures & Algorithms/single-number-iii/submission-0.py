class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in range(0, len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
            else:
                freq[nums[i]] = 1

        result = []
        for curr in freq:
            if freq[curr] == 1:
                result.append(curr)
        return result
        