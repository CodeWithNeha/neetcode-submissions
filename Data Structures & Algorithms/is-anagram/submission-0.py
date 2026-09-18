class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li = {}

        for i in range(0, len(s)):
            if s[i] in li:
                li[s[i]] +=1
            else:
                li[s[i]] = 1
        
        for i in range(0, len(t)):
            if t[i] in li:
                li[t[i]] -=1
            else:
                li[t[i]] = 1
            if li[t[i]] == 0:
                li.pop(t[i])
        return len(li)==0
        