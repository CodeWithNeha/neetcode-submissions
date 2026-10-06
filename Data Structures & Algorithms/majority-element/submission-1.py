class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        mEle = nums[0]
        count = 0
        for i in range(0, len(nums)):
            if nums[i] in dic:
                dic[nums[i]] +=1
            else:
                dic[nums[i]] = 1
            if count<dic[nums[i]]:
                count = dic[nums[i]]
                mEle = nums[i]
        return mEle