class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force
        return sorted(s) == sorted(t)