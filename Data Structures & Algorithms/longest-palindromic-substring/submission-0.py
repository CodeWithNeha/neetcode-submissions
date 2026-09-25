class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        result = ""
        maxL = float('-inf')

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub==sub[::-1]:
                    # print(s[i:j])
                    if maxL<len(sub):
                        result = sub
                        maxL = len(sub)


        return result