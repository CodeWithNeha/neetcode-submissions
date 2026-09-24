class Solution:
    def reverse(self, nums, start, end):
        while(start<end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
            # print(end)
        
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        