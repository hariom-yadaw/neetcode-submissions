class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowStart, maxRepeatCharCount = 0, 0
        char_freq = {}

        longestSubstr = 0

        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            char_freq[rightChar] = char_freq.get(rightChar, 0) + 1

            maxRepeatCharCount = max(maxRepeatCharCount, char_freq[rightChar])

            while (windowEnd - windowStart + 1 - maxRepeatCharCount) > k:
                leftChar = s[windowStart]
                windowStart += 1

                char_freq[leftChar] = char_freq.get(leftChar, 0) - 1

            longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)

        return longestSubstr 
