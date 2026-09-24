class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while(start<end):
            sum = numbers[start]+numbers[end]
            if sum == target:
                return [numbers[start], numbers[end]]
            elif sum>target:
                end -=1
            else:
                start+=1
        return [-1,-1]
        