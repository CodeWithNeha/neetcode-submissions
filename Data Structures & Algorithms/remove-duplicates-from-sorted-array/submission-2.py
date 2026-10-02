class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Brute force
        result = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != result[-1]:
                result.append(nums[i])
        nums[:len(result)] = result
        return len(result)

        
        