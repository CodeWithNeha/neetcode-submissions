class Solution:
    def findPivot(self, nums, start, end):
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return start
    def binarySearch(self, nums, start, end, target):
        while(start<=end):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        pivot = self.findPivot(nums, 0, end)
        print(pivot)
        search = self.binarySearch(nums, 0, pivot-1, target)
        if search == -1:
            search = self.binarySearch(nums, pivot, end, target)
        return search
        