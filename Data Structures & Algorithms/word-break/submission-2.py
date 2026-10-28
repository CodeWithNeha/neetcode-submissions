class Solution:
    def __init__(self):
        self.dp = [None]*201
    def helper(self, s, wordDict, ind):
        if ind == len(s):
            self.dp[ind] = True
            return True
        if self.dp[ind] is not None:
            return self.dp[ind]
    
        for w in wordDict:
            if (ind+len(w)<=len(s)) and s[ind:ind+len(w)] == w:
                if self.helper(s, wordDict, ind+len(w)):
                    self.dp[ind] = True
                    return True
        self.dp[ind] = False
        return False
        

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, wordDict, 0)
        

        