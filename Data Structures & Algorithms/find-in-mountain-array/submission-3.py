class Solution:

    def findPeak(self, start, end, arr):
        while(start<end):
            mid = (start+end)//2
            if arr.get(mid)>arr.get(mid+1):
                end = mid
            else:
                start = mid+1
        return start

    def binarySearch(self, arr, start, end, target):
        asc = arr.get(start) < arr.get(end)
        while(start<=end):
            mid = (start + end)//2
            if (arr.get(mid) == target):
                return mid
            elif asc:
                if arr.get(mid) > target: 
                    end = mid - 1
                else:
                    start = mid + 1
            
            else:
                if arr.get(mid) < target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        peakEle = self.findPeak( 0, n-1, mountainArr)
        search = self.binarySearch(mountainArr, 0, peakEle, target)
        if search==-1:
            search = self.binarySearch(mountainArr, peakEle+1, n-1, target)
        return search
        
        