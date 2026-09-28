# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         n = len(nums)
#         i = 0
#         j = i+k
#         while(j<=n):
#             max= float('-inf')
#             for ele in range(i, j):
#                 if max<nums[ele]:
#                     max = nums[ele]
#             result.append(max)
#             i +=1
#             j+=1
#         return result

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []

        n = len(nums)

        i = 0
        j = i + k

        while j <= n:

            maximum = float('-inf')

            for ele in range(i, j):
                if maximum < nums[ele]:
                    maximum = nums[ele]

            result.append(maximum)

            i += 1
            j += 1

        return result
        