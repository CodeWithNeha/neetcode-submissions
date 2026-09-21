class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for curr in range(0, 32):
            new_pos = 32-curr-1
            bit = (n>>curr)&1
            mask = bit<<new_pos
            ans = ans| mask
        return ans