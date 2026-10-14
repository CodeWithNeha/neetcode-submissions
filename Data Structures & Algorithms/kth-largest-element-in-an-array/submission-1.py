class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # optimized
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
        