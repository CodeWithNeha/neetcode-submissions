class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0]*n
        ans[0]=nums[0]
        ans[1] = nums[1]
        for i in range(2, n):
            ans[i] = max(nums[i]+ans[i-2], ans[i-1])
        return ans[n-1]
        