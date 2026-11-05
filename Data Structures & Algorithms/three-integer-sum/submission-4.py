class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(0, n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = n-1
            while(start<end):
                summ = nums[i]+nums[start]+nums[end]
                if summ == 0:
                    ans.append([nums[i], nums[start], nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start] == nums[start-1]:
                        start +=1
                    while start<end and nums[end] == nums[end+1]:
                        end -=1
                elif summ > 0:
                    end -=1
                else:
                    start +=1
        return ans
                
        