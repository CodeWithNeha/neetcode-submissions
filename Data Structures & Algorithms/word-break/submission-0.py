class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for ele in wordDict:
            if ele in s:
                s = s.replace(ele,"")
        return len(s)==0
        