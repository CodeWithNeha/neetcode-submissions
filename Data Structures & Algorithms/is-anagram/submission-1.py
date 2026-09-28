class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in li:
                li[s[i]] +=1
            else:
                li[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in li:
                li[t[i]] -=1
                if li[t[i]] ==0:
                    li.pop(t[i])
            else:
                li[t[i]] = 1
           
        print(li)
        return len(li)==0