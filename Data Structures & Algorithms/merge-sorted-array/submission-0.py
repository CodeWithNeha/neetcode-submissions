class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = [0] * (m + n)

        nums1Ind = 0
        nums2Ind = 0
        i = 0

        while nums1Ind < m and nums2Ind < n:
            if nums1[nums1Ind] < nums2[nums2Ind]:
                result[i] = nums1[nums1Ind]
                nums1Ind += 1
            else:
                result[i] = nums2[nums2Ind]
                nums2Ind += 1

            i += 1

        while nums1Ind < m:
            result[i] = nums1[nums1Ind]
            nums1Ind += 1
            i += 1

        while nums2Ind < n:
            result[i] = nums2[nums2Ind]
            nums2Ind += 1
            i += 1

        nums1[:] = result
            