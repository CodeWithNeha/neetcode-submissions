class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = 0
        ans = res = 0
        count = 0
        while(end<len(nums)):
            ans +=1
            if nums[end] == 0:
                count+=1
            while count>k:
                if nums[start]==0:
                    count-=1
                start+=1
                ans = end-start+1
            end+=1
            res = max(res, ans)
        return res
            
        