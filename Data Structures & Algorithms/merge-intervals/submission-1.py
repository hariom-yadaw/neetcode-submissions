class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            newInterval = intervals[i]
            if newInterval[0] <= end: # overalp
                end = max(end, newInterval[1])
            else: # Not overap, merge the last interval and update start/end
                merged.append([start, end])
                start = newInterval[0]
                end = newInterval[1]
        
        merged.append([start, end])

        return merged

