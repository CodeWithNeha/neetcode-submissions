class Solution:
    def romanToInt(self, s: str) -> int:
        symbolVal = {
            "I" :1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and symbolVal[s[i]] < symbolVal[s[i + 1]]:
                res -= symbolVal[s[i]]
            else:
                res += symbolVal[s[i]]
        return res
        