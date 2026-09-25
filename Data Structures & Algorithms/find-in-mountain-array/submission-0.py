class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        for i in range(mountainArr.length()):
            if mountainArr.get(i) == target:
                return i
        return -1
        