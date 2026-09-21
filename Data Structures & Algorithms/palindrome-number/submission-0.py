class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        rev = 0
        while(x>0):
            rem = x%10
            rev =rev*10+ rem
            x = x//10
            print(rev)
        return rev == original

        