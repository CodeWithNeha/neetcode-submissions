class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for left in range(len(words)):
            for right in range(len(words)):
                if left == right:
                    continue
                if words[left] in words[right]:
                    result.append(words[left])
                    break
        return result

        