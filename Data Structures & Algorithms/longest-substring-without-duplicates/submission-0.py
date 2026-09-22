class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_freq = {}

        windowStart = 0
        longestSubstr = 0

        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            char_freq[rightChar] = char_freq.get(rightChar, 0) + 1

            while windowEnd - windowStart + 1 > len(char_freq):
                leftChar = s[windowStart]
                windowStart += 1
                char_freq[leftChar] = char_freq.get(leftChar, 0) - 1
                if char_freq[leftChar] == 0:
                    del char_freq[leftChar]
            
            longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)
        
        return longestSubstr
