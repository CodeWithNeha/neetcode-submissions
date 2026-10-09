class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Optimized
        if len(s1)>len(s2):
            return False
        count1 = {}
        count2 = {}

        for char in s1:
            count1[char] = count1.get(char, 0)+1

        window_size = len(s1)

        for i in range(len(s2)):
            char = s2[i]
            count2[char] = count2.get(char, 0)+1

            if i>=window_size:
                left_char = s2[i-window_size]
                count2[left_char] -=1
                if count2[left_char] == 0:
                    del count2[left_char]

            if count1 == count2:
                return True

        return False
