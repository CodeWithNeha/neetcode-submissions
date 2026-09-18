class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(',']':'[','}':'{'}
        stack = []
        for ch in s:
            if ch in mp.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != mp[ch]:
                    return False
        return not stack
        