class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # optimized
        best = 0
        left = 0
        n = len(s)
        seen = set()
        for right in range(n):

            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            best = max(best, right-left+1)
        return best
