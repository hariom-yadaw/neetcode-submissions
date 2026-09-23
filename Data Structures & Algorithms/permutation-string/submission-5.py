class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowStart = 0
        matched = 0

        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1

        for windowEnd in range(len(s2)):
            rightChar = s2[windowEnd]

            if rightChar in s1_freq:
                s1_freq[rightChar] -= 1
                if s1_freq[rightChar] == 0:
                    matched += 1
            
            if matched == len(s1_freq):
                return True
            
            if windowEnd >= len(s1) - 1:
                leftChar = s2[windowStart]
                windowStart += 1

                if leftChar in s1_freq:
                    if s1_freq[leftChar] == 0:
                        matched -= 1
                    s1_freq[leftChar] += 1

        return False  