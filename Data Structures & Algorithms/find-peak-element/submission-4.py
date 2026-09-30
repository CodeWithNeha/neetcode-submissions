class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        # Binary Search
        end = len(arr)-1
        start = 0
        while(start<end):
            mid = (start+end)//2
            if arr[mid]>arr[mid+1]:
                end = mid
            else:
                start = mid+1
        return start
        