class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1

        if n < 0:
            x = 1 / x
            n = -n

        for i in range(n):
            result *= x

        return result
        