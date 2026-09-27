import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if n >= len(meetings):
            return 0
        
        meetings.sort(key=lambda x: x[0])
        
        # minHeap for available rooms, initilaized with room numbers in order
        availableRooms = [i for i in range(n)]
        usedRooms = [] # minheap for used rooms [(endTime, roomNumber)]
        roomBookedCount = [0] * n # Count of meetings for each room

        for start, end in meetings:
            # Finish meetings
            while usedRooms and usedRooms[0][0] <= start:
                _, room = heapq.heappop(usedRooms)
                heapq.heappush(availableRooms, room) 
            
            # not available ? => Pop once again and push into available rooms
            if not availableRooms:
                endTime, room = heapq.heappop(usedRooms) # get teh earliest ending meeting (forced)
                end = endTime + (end - start)
                heapq.heappush(availableRooms, room)

            room = heapq.heappop(availableRooms)
            heapq.heappush(usedRooms, (end, room))
            roomBookedCount[room]  += 1 
        
        return roomBookedCount.index(max(roomBookedCount))
