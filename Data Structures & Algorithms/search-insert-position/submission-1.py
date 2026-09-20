class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        start = 0
        end = len(arr)-1
        while(start<=end):
            mid = (start+end)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid -1
            else:
                start =mid+1

        if(start!=0):
            return start
        else:
            return 0

        