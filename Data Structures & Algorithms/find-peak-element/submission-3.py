class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        # Brute Force
        maxEle = float('-inf')
        maxInd = -1
        for i in range(len(arr)):
            if arr[i]>maxEle:
                maxEle = arr[i]
                maxInd = i
        return maxInd
            
        