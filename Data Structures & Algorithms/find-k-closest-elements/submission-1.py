class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        for num in arr:
            res.append(num)

        res.sort(key=lambda num: (abs(num-x), num))

        return sorted(res[:k])