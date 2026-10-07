class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        n = len(heights)
        maxi = 0
        for left in range(n):
            for right in range(left+1, n):
                width = (right-left)
                height = min(heights[left], heights[right])
                area = width*height
                maxi = max(maxi, area)
        return maxi

