class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)-1
        while(start<end):
            mid = (start+end)//2
            if arr[mid]>arr[end]:
                start = mid+1
            else:
                end = mid
        return start-1
        