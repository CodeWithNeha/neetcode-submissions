class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        n -= 1
        bit = 0

        while n:
            if x & (1 << bit) == 0:
                if n & 1:
                    result |= (1 << bit)
                n >>= 1

            bit += 1
        return result
