class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = j = 0
        dq = deque()
        n = len(nums)
        ans = []
        while(j<n):
            while(dq and nums[dq[-1]]< nums[j]):
                dq.pop()
            dq.append(j)
            if dq and dq[0] < i:
                dq.popleft()
            if j-i+1 == k:
                ans.append(nums[dq[0]])
                i+=1
            j+=1
        return ans