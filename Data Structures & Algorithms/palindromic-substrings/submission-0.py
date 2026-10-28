class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            ans +=1
            firstPointer = i-1
            secondPointer = i+1
            while(firstPointer>=0 and secondPointer<n and s[firstPointer]==s[secondPointer]):
                firstPointer -=1
                secondPointer +=1
                ans+=1
            firstPointer = i
            secondPointer = i+1
            while(firstPointer>=0 and secondPointer<n and s[firstPointer]==s[secondPointer]):
                firstPointer -=1
                secondPointer +=1
                ans+=1
        return ans
            

        