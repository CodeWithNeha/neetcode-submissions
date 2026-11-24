class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        n = len(nums)

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        result = [0] * n

        if zero_count > 1:
            return result

        for i in range(n):
            if zero_count == 1:
                if nums[i] == 0:
                    result[i] = product
            else:
                result[i] = product // nums[i]

        return result