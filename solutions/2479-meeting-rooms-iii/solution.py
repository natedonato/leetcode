class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counts = {}

        # room id, time
        unoccupied = []
    
        # time, room id
        occupied = []

        for i in range(n):
            unoccupied.append((i,0))
            counts[i] = 0

        meetings.sort()

        for [start_time, end_time] in meetings:
            while occupied and (occupied[0][0] <= start_time or not unoccupied):
                (time, room_id) = heapq.heappop(occupied)
                heapq.heappush(unoccupied, (room_id, time))

            (room_id, time) = heapq.heappop(unoccupied)
            counts[room_id] += 1
            
            if time > start_time:
                end_time += time - start_time
            
            heapq.heappush(occupied, (end_time, room_id))

        most_meetings = 0
        idx = 0
        
        for room, count in counts.items():
            if count > most_meetings:
                idx = room
                most_meetings = count
            elif count == most_meetings:
                idx = min(idx, room)

        return idx


