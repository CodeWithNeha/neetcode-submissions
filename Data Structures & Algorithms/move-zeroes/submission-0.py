class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Brute Force
        non_zero = []
        for num in nums:
            if num !=0:
                non_zero.append(num)
        zeros = len(nums) - len(non_zero)
        nums[:] = non_zero + [0]*zeros