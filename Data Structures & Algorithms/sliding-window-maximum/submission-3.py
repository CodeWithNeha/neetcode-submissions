class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = j = 0
        dq = deque()
        n = len(nums)
        ans = []
        while(j<n):
            while(dq and dq[-1]< nums[j]):
                dq.pop()
            dq.append(nums[j])
            if j-i+1 == k:
                if dq:
                    ans.append(dq[0])
                else:
                    ans.append(0)
                i+=1
            j+=1
        return ans