class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            num = i
            count = 0
            while(num!=0):
                count+=1
                num = num&(num-1)
            result.append(count)
        return result


        