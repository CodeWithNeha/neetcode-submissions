class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        count = 0

        while i < len(nums):
            j = i
            total = 0

            while j < len(nums):
                total += nums[j]

                if total == k:
                    count += 1

                j += 1

            i += 1

        return count
        