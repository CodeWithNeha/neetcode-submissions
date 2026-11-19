class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for i in range(0, len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
                return nums[i]
            else:
                freq[nums[i]] = 1
        return -1
        

        