from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        windowStart = 0
        queue = deque() # to store the index only, not values
        result = []

        for windowEnd in range(len(nums)):
            # pop the smaller values and maintain decreasing order in queue
            # before inserting the new index, remove indices whose values are smaller than the new values
            # - they can not be the future maximums
            while queue and nums[queue[-1]] < nums[windowEnd]:
                queue.pop()

            # Append the smaller values at right
            queue.append(windowEnd) # if the queue became empty, this current value will be maximum

            if windowStart > queue[0]:
                queue.popleft()

            if windowEnd + 1 >= k:
                result.append(nums[queue[0]])
                windowStart += 1
            
        
        return result

                