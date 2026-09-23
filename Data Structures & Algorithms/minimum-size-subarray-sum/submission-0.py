class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowStart, windowSum  = 0, 0
        minSubarraylen = len(nums) + 1

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]

            while windowSum >= target:
                # record the window length
                minSubarraylen = min(minSubarraylen, windowEnd - windowStart + 1)

                windowSum -= nums[windowStart]
                windowStart += 1
        
        return minSubarraylen if minSubarraylen < len(nums) + 1 else 0
            
