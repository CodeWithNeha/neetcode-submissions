class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for ele in strs:
            original = ele

            sorted_ele = ''.join(sorted(ele))

            if sorted_ele in freq:
                if original not in freq[sorted_ele]:
                    freq[sorted_ele].append(original)
            else:
                freq[sorted_ele] = [original]

        return list(freq.values())