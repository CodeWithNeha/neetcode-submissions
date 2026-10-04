class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # optimized kedann's algo
        total = current_max = current_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        for num in nums:
            total +=num

            current_max = max(current_max+num,num)
            max_sum = max(current_max, max_sum)

            current_min = min(current_min+num, num)
            min_sum = min(current_min, min_sum)
        if max_sum<0:
            return max_sum
        return max(max_sum, total-min_sum)

        