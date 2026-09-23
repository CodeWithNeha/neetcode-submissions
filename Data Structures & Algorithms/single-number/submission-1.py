class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor = 0
        # for i in nums:
        #     xor ^= i
        # return xor
        nums.sort()
        i = 0
        while(i<len(nums)-1):
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[i]
