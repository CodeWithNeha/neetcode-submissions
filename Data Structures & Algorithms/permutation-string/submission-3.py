class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force
        target = sorted(s1)
        length = len(s1)
        for i in range(len(s2)-length+1):
            window = s2[i:i+length]
            if sorted(window) == target:
                return True
        return False