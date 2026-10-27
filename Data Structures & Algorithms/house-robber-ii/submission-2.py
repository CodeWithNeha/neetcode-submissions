class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        n = len(nums)
        ans1 = [0]*(n-1)
        ans2 = [0]*(n-1)
        ans1[0] = nums[0]
        ans1[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            ans1[i] = max(ans1[i-1], ans1[i-2]+nums[i])

        ans2[0] = nums[1]
        ans2[1] = max(nums[1], nums[2])
        for i in range(3, n):
            ans2[i-1] = max(ans2[i-2], ans2[i-3]+nums[i])
        print(ans1)
        print(ans2)
        return max(ans1[n-2], ans2[n-2])