class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        windowStart, matched, substr_start = 0, 0, 0
        minSubstrLen = len(s) + 1
        char_freq = {}

        for char in t:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for windowEnd in range(len(s)):
            rightchar = s[windowEnd]

            if rightchar in char_freq:
                char_freq[rightchar] -= 1
                if char_freq[rightchar] >= 0:
                    matched += 1
            
            while matched == len(t): # matched may not change if char_freq[leftChar] is -ve
                if minSubstrLen > windowEnd - windowStart + 1:
                    minSubstrLen = windowEnd - windowStart + 1
                    substr_start = windowStart

                leftChar = s[windowStart]
                windowStart += 1

                if leftChar in char_freq:
                    if char_freq[leftChar] == 0:
                        matched -= 1
                    char_freq[leftChar] += 1
            
        if minSubstrLen > len(s):
            return ""

        return s[substr_start: substr_start + minSubstrLen]    



