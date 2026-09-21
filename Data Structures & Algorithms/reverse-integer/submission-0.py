class Solution:
    def reverse(self, x: int) -> int:
        MAX_VALUE = 2**31 - 1
        MIN_VALUE = -2**31
        rev = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        while(x!=0):
            rem = x%10
            if rev>MAX_VALUE/10 or rev<MIN_VALUE/10:
                return 0
            rev = rev*10+ rem
            x = int(x/10)

        return rev*sign
        