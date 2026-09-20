class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in range(0, len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] +=1
            
        sorted_elements = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)
        return sorted_elements[:k]
        