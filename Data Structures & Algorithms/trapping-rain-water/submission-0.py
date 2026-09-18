class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rightMax = [0 for i in range(0, n)]
        rightMax[-1] = height[-1]
        waterTrap = 0
        leftMax = 0
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        for i in range(0, n):
            leftMax = max(leftMax, height[i])
            possibleS = min(leftMax, rightMax[i])
            waterTrap += possibleS-height[i]
        return waterTrap


        