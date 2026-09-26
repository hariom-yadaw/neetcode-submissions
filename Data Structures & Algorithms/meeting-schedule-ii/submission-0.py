"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) < 2:
            return 1
        
        intervals.sort(key=lambda x: x.start)

        minRooms = 0
        minHeap = [] # To keep track of ending time of all meetings happening currently

        for interval in intervals:

            # remove all the meetings that have ended
            while minHeap and interval.start >= minHeap[0]:
                heapq.heappop(minHeap)

            # add the current meeting into minHeap
            heapq.heappush(minHeap, interval.end)

            # all the active meetings are in the minHeap, so we need rooms for all of them
            minRooms = max(minRooms, len(minHeap))
        
        return minRooms

        