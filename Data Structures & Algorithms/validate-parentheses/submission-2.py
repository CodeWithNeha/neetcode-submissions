class Solution:
    def isValid(self, s: str) -> bool:
        # optimized
        stack = []
        pairs = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        for char in s:
            if char in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return len(stack)==0
        