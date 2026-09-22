class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        windowStart = 0
        longestSubstr = 0

        for windowEnd in range(len(s)):
            while s[windowEnd] in charSet:
                charSet.remove(s[windowStart])
                windowStart += 1
            
            charSet.add(s[windowEnd])
            longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)
        
        return longestSubstr
