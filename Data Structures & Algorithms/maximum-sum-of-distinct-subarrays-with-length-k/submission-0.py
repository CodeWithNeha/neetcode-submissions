class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        start = end = 0
        currSum = bestSum = 0
        size = 0
        freq = {}
        while(end<len(nums)):
            currSum += nums[end]
            size +=1
            freq[nums[end]] = freq.get(nums[end], 0)+1
            while(size>k or freq[nums[end]]>1):
                freq[nums[start]] -= 1
                if freq[nums[start]] == 0:
                    del freq[nums[start]]
                size -=1
                currSum -= nums[start]
                start+=1
            if size==k:
                bestSum = max(bestSum, currSum)
            end+=1
        return bestSum
            
        