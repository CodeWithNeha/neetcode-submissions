class Solution:
    def binarySearch(self, matrix, row,start, end, target):
        while(start<=end):
            mid = (start+end)//2
            
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]>target:
                end = mid -1
            else:
                start = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(0, len(matrix)):
            result = self.binarySearch(matrix, row, 0, len(matrix[row])-1, target)
            if result:
                return True
        return False