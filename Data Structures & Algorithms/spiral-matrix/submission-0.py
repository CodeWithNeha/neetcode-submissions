class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []

        minR = 0
        maxR = m-1
        minC = 0
        maxC = n-1

        while(len(result)<(m*n)):
            ## top 
            for i in range(minC, maxC+1):
                result.append(matrix[minR][i])
            
            minR +=1
            if len(result)>=n*m:
                break

            ## right
            for j in range(minR, maxR+1):
                result.append(matrix[j][maxC])
            maxC-=1
            if len(result)>=n*m:
                break

            ## Bottom
            for k in range(maxC, minC-1, -1):
                result.append(matrix[maxR][k])
            
            maxR -= 1
            if len(result)>=n*m:
                break

            ## left
            for l in range(maxR, minR-1, -1):
                result.append(matrix[l][minC])
            minC += 1
            if len(result)>=n*m:
                break

        return result

        