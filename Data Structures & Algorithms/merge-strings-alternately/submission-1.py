class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minL = min(len(word1), len(word2))
        st = ""
        i = 0
        while(len(st)!=(minL+minL)):
            st += word1[i]
            st += word2[i]
            i+=1
        while(i<len(word1)):
            st+=word1[i]
            i +=1
        while(i<len(word2)):
            st+=word2[i]
            i +=1
        return st