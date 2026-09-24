class Solution:
    def helper(self, num):
        result = 0
        while(num>0):
            rem = num % 10
            result += rem*rem
            num = num // 10
        return result

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        while((n%10!=n)):
            n = self.helper(n)
            print(n)
            if n == 1:
                return True
        return False

       
        