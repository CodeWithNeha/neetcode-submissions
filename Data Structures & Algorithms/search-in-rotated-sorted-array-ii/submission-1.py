class Solution:
    def pivot(self, arr, start, end):

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                return i + 1

        return 0

    def binarySearch(self, nums, start, end, target):

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                end = mid - 1

            else:
                start = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> bool:

        start = 0
        end = len(nums) - 1

        if not nums:
            return False

        pivot = self.pivot(nums, start, end)

        result = self.binarySearch(
            nums, 0, pivot - 1, target
        )

        if result == -1:
            result = self.binarySearch(
                nums, pivot, end, target
            )

        return result != -1