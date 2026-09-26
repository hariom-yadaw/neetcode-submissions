class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        
        #intervals.sort()
        intervals.sort(key=lambda x: (x[0], x[1]))
        #intervals.sort(key=lambda x: x[1])
        minRemoved = 0
        
        prevInterval = intervals[0]
        prevEnd = prevInterval[1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                minRemoved += 1
                prevEnd = min(intervals[i][1], prevEnd)
            else:
                prevEnd = intervals[i][1]
        

        return minRemoved