class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        product = 1
        count = 0
        n = len(nums)
        for j in range(n):
            product *=nums[j]
            while(i <= j and product>=k):
                product //=nums[i]
                i+=1
            count+= (j-i +1)
        return count
        