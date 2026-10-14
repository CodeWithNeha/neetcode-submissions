class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force
        answer = 0
        while(answer+1)*(answer+1)<=x:
            answer+=1
        return answer
        