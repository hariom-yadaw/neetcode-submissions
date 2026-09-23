class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        windowStart, result_start = 0, 0
        windowAbsSum = 0
        minWindowSum = math.inf
        result = []


        for windowEnd in range(len(arr)):
            windowAbsSum += abs(x - arr[windowEnd])

            #minWindowSum = min(minWindowSum, windowAbsSum)

            if windowEnd - windowStart + 1 >= k:
                if minWindowSum > windowAbsSum:
                    minWindowSum = windowAbsSum
                    result_start = windowStart

                windowAbsSum -= abs(x - arr[windowStart])
                windowStart += 1
        
        for i in range(result_start, result_start + k):
            result.append(arr[i])
        
        return result
                 