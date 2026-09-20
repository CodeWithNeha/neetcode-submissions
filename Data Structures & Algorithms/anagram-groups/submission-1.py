class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for ele in strs:
            sorted_ele = ''.join(sorted(ele))

            if sorted_ele in freq:
                freq[sorted_ele].append(ele)
            else:
                freq[sorted_ele] = [ele]

        return list(freq.values())