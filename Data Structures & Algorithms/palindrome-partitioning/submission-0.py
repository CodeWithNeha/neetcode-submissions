class Solution:
    def __init__(self):
        self.ans = []
    
    def helper(self, s , current):
        if s == "":
            copi = current.copy()
            self.ans.append(copi)
            return
        for part in range(1, len(s)+1):
            prefix = s[0:part]
            remain = s[part:]
            if prefix == prefix[::-1]:
                current.append(prefix)
                self.helper(remain, current)
                current.pop()
    def partition(self, s: str) -> List[List[str]]:
        self.helper(s, [])
        return self.ans
        