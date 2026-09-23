class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums[n - 1] += 1
        carry = nums[n - 1] // 10
        nums[n - 1] %= 10

        for i in range(n - 2, -1, -1):

            if carry == 1:
                nums[i] += 1

                carry = nums[i] // 10
                nums[i] %= 10

        if carry == 1:
            nums.insert(0, 1)

        return nums
        
            

        
        