class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        # brute force 
        for i, num in enumerate(arr):
            if arr[i] >= target:
                return i
        return len(arr)

        