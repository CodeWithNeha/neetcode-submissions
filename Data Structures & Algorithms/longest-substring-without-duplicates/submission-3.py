class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        ans = 0
        best = 0
        while(right< len(s)):
            ans+=1
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
                ans -=1
            seen.add(s[right])
            best = max(ans, best)
            right+=1

        return best