class Solution:
    def helper(self, s, wordDict, ind):
        if ind == len(s):
            return True
        
        for w in wordDict:
            if (ind+len(w)<=len(s)) and s[ind:ind+len(w)] == w:
                if self.helper(s, wordDict, ind+len(w)):
                    return True
        return False
        

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, wordDict, 0)
        

        