class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # optimized
        count = 0
        current_sum = 0
        prefix_sum = {0:1}
        for num in nums:
            current_sum += num
            needed = current_sum - k
            if needed in prefix_sum:
                count += prefix_sum[needed]
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0)+1
        return count