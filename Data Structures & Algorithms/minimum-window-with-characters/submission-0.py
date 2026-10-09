class Solution:
    from collections import Counter

    def contains_all(self, window, t):
        window_count = Counter(window)
        required_count = Counter(t)

        for char, needed_count in required_count.items():
            if window_count.get(char, 0) < needed_count:
                return False

        return True
    def minWindow(self, s: str, t: str) -> str:
        # brute force
        best = ""
        for left in range(len(s)):
            for right in range(left, len(s)):
                window = s[left:right+1]
                if self.contains_all(s[left:right + 1], t):
                    if not best or len(window)<len(best):
                        best = window
        return best
        