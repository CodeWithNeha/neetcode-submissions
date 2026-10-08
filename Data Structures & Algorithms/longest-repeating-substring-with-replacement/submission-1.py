class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # optimized
        best = 0
        n = len(s)
        count = {}
        max_freq = 0
        left = 0
        for right in range(n):
            char = s[right]
            count[char] = count.get(char, 0)+1
            max_freq = max(max_freq, count[char])
            window_size = right-left+1
            while window_size-max_freq > k:
                count[s[left]] -=1
                left+=1
                window_size = right-left+1
            best = max(best, window_size)

        return best