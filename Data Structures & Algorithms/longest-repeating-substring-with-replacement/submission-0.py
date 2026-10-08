class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force
        best = 0
        n = len(s)
        for left in range(n):
            count = {}
            for right in range(left, n):
                count[s[right]] = count.get(s[right], 0) +1

                max_freq = max(count.values())
                window_size = right-left+1
                replacement = window_size - max_freq
                if replacement<=k:
                    best = max(best, window_size)

        return best