class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        curr = nums[0]
        i = 0
        streak = 0
        res = 0
        while(i<len(nums)):
            if nums[i]!=curr:
                curr = nums[i]
                streak = 0
            while i < len(nums) and curr == nums[i]:
                i+=1
            streak+=1
            curr+=1
            res = max(streak,res)
        return res
