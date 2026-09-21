class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq_map = {}
        windowStart = 0
        
        for windowEnd in range(len(nums)):
            rightNum = nums[windowEnd]
            freq_map[rightNum] = freq_map.get(rightNum, 0) + 1

            while (windowEnd - windowStart ) > k:
                leftNum = nums[windowStart]
                windowStart += 1

                freq_map[leftNum] = freq_map.get(leftNum, 0 ) - 1
                if freq_map[leftNum] == 0:
                    del freq_map[leftNum]
            
            if windowEnd - windowStart + 1 > len(freq_map):
                return True

        return False   