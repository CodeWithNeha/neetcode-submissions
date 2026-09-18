class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1

        for i in range(len(nums)):
            while i <= end and nums[end] == val:
                end -= 1

            if i > end:
                break

            if nums[i] == val:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1

        return end + 1
                    

            