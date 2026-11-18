class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        # ind, temp
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][-1]<temp:
                ind, tem = stack.pop()
                result[ind] = i-ind
            stack.append([i, temp])
        return result
