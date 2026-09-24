class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        for i in range(n-1):
            result = (result+1)|x
        return result
        