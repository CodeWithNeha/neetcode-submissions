class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force
        n = len(nums)
        res = []
        for i in range(n):
            ans = 1
            for j in range(n):
                if i!=j:
                    ans *= nums[j]
            res.append(ans)
        return res

        