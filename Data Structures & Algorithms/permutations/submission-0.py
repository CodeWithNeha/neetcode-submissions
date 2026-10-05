class Solution:
    def __init__(self):
        self.ans = []
    
    def helper(self, arr, used):
        if len(used) == len(arr):
            copied = used.copy()
            self.ans.append(copied)
            return
        for i in range(len(arr)):
            if arr[i] not in used:
                used.append(arr[i])
                self.helper(arr, used)
                used.pop()
        
    def permute(self, arr: List[int]) -> List[List[int]]:
        self.helper(arr,[])
        return self.ans

        