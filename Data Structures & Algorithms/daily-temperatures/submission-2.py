class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i in range(n):
            while stack and temperatures[i]> stack[-1][-1]:
                stackI, stackT = stack.pop()
                ans[stackI] = i-stackI
            stack.append([i, temperatures[i]])
        return ans

        