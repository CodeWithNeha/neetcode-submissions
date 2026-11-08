class Solution:
    def helper(self, target):
        if target == 0:
            return 0

        res = target

        for i in range(1, target + 1):
            if i * i > target:
                break

            res = min(
                res,
                1 + self.helper(target - i * i)
            )

        return res

    def numSquares(self, n: int) -> int:
        return self.helper(n)