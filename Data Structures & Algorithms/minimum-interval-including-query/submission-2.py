import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort() # sort interval
        minHeap = [] # to track the sortest interval
        result_map = {} # store the result in a hash map
        i = 0
        for q in sorted(queries): # sorted queries
            # push all the eligible (start <= q) intervals for query q
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1

            # remove all invalid intrvals 
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            result_map[q] = minHeap[0][0] if minHeap else -1
        
        return [result_map[q] for q in queries]