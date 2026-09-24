class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        n = len(nums)
        for i in range(0, n):
            if nums[i] in freq:
                freq[nums[i]] += 1
                if freq[nums[i]]>n//3 and nums[i] not in res:
                    res.append(nums[i])
            else:
                freq[nums[i]] = 1
        return res

        