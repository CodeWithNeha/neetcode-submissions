class Solution:
    def findPivot(self, arr, start, end):
        while start<end:
            mid = start + (end-start)//2
            if arr[mid]>arr[end]:
                start = mid+1
            else:
                end = mid
        return start

    def binarySearch(self, nums, start, end, target):
        while(start<=end):
            mid = start + (end-start)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums, 0, len(nums)-1)
        search = self.binarySearch(nums, 0, pivot-1, target)
        if search ==-1:
            search = self.binarySearch(nums, pivot, len(nums)-1, target)
        return search
        