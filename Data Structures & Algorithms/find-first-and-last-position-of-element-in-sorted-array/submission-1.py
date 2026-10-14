class Solution:
    def binarySearch(self, nums, target, left, right, startIndex):
        answer = -1
        while(left<=right):
            mid = left + (right-left)//2
            if nums[mid] == target:
                answer = mid
                if startIndex:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return answer

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # optimized
        first = self.binarySearch(nums, target, 0, len(nums)-1, True)
        last = self.binarySearch(nums, target, 0, len(nums)-1, False)
        return [first, last]