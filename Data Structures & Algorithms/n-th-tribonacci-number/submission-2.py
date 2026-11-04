class Solution:
    def tribonacci(self, n: int) -> int:
        if n <=1:
            return 0 if n!=1 else 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+ self.tribonacci(n-3)
        